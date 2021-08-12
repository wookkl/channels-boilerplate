from urllib.parse import parse_qs

import jwt
from channels.auth import AuthMiddlewareStack
from channels.exceptions import StopConsumer
from django.conf import settings


class InstanceTokenAuthWrapper:
    def __init__(self, scope):
        self.scope = dict(scope)

    @property
    def parsed_qs(self):
        return parse_qs(self.scope['query_string'].decode())

    @property
    def auth_token(self):
        return self.parsed_qs.get('token', [''])[0]

    @property
    def user_id(self):
        if 'user_id' in self.decoded_auth_token:
            return self.decoded_auth_token['user_id']
        raise StopConsumer('Invalid token')

    @property
    def decoded_auth_token(self):
        try:
            return jwt.decode(
                self.auth_token,
                settings.SECRET_KEY,
                algorithms='HS256',
                options={"verify_exp": False}
            )
        except jwt.DecodeError:
            raise StopConsumer('Invalid token')

    async def set_scope(self):
        """
        필요한 scope 세팅
        """
        pass


class TokenAuthMiddleware:
    def __init__(self, inner):
        self.inner = inner

    async def __call__(self, scope, receive, send):
        wrapper = InstanceTokenAuthWrapper(scope)
        if wrapper.auth_token:
            await wrapper.set_scope()
        return await self.inner(wrapper.scope, receive, send)


def TokenAuthMiddlewareStack(inner):
    return TokenAuthMiddleware(AuthMiddlewareStack(inner))
