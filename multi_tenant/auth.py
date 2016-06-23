from braces.views._access import AccessMixin
from .exceptions import IncorrectTenantException


def belongs_to_tenant(username, tenant):
    """
    This function checks if the user belongs to the given Tenant.
    """
    user_exists = tenant.users.filter(username=username).exists()
    if not user_exists:
        raise IncorrectTenantException()


class TenantRequiredMixin(AccessMixin):
    """
    View mixin which verifies that there is a tenant in the request, that the
    user is authenticated and that the user belongs to the tenant.

    NOTE:
        This should be the left-most mixin of a view, except when
        combined with Django-Braces CsrfExemptMixin - which in that case
        should be the left-most mixin.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.tenant:
            return self.handle_no_permission(request)

        if not request.user.is_authenticated():
            return self.handle_no_permission(request)

        try:
            belongs_to_tenant(request.user.username, request.tenant)
        except IncorrectTenantException:
            return self.handle_no_permission(request)

        return super(TenantRequiredMixin, self).dispatch(
            request, *args, **kwargs)
