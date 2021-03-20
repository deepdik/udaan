from django.contrib.auth.mixins import AccessMixin


class IsSuperuserMixin(AccessMixin):
    """Verify that the current user is_superuser or not."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class IsAuthenticatedMixin(AccessMixin):
    """Verify that the request has permission to access the view or not."""
    def dispatch(self, request, *args, **kwargs):
        user = request.user
        user_perms_lst = list(user.groups.values_list(
            'permissions__codename', flat=True))
        required_perms = self.permission_required

        if not set(required_perms).issubset(user_perms_lst):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
