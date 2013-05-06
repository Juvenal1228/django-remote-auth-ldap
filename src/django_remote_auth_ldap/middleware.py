from django.contrib.auth import middleware
from django_remote_auth_ldap.conf import settings


class RemoteUserMiddleware(middleware.RemoteUserMiddleware):
    @property
    def HEADER(self):
        return settings.HEADER
