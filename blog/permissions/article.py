from combojsonapi.permission.permission_system import (
    PermissionMixin,
    PermissionUser,
    PermissionForGet, PermissionForPatch,
)
from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user
from blog.models.models import Articles, Author


class ArticlePermissions(PermissionMixin):
    ALL_AVAILABLE_FIELDS = [
        "title",
        "text",
        "author",
        "tags"
    ]

    PATCH_AVAILABLE_FIELDS = [
        "title",
        "text",
        "tags"
    ]

    def get(self, *args, many=True, user_permission: PermissionUser = None, **kwargs) -> PermissionForGet:
        self.permission_for_get.allow_columns = (self.ALL_AVAILABLE_FIELDS, 10)
        return self.permission_for_get

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)
        return self.permission_for_patch

    def patch_data(self, permission_for_patch=None, *args, data=None, obj=None, user_permission: PermissionUser = None,
                   **kwargs) -> dict:
        permission_for_patch = user_permission.permission_for_patch_permission(model=Articles)
        article_id = data.get('id')
        article = Articles.query.filter_by(id=article_id).one_or_none()
        author_id = article.author_id
        author = Author.query.filter_by(id=author_id).one_or_none()
        if current_user.is_staff or current_user.id == author.user_id:
            return {
                i_key: i_val
                for i_key, i_val in data.items()
                if i_key in permission_for_patch.columns
            }
        else:
            raise AccessDenied("No access")
