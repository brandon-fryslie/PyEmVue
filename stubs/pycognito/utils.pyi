import requests
import requests.auth
from . import Cognito as Cognito
from _typeshed import Incomplete
from enum import Enum

class TokenType(str, Enum):
    ID_TOKEN = 'id_token'
    ACCESS_TOKEN = 'access_token'

class RequestsSrpAuth(requests.auth.AuthBase):
    cognito_client: Incomplete
    username: Incomplete
    http_header: Incomplete
    http_header_prefix: Incomplete
    token_type: Incomplete
    def __init__(self, username: str = None, password: str = None, user_pool_id: str = None, user_pool_region: str = None, client_id: str = None, cognito: Cognito = None, http_header: str = 'Authorization', http_header_prefix: str = 'Bearer ', auth_token_type: TokenType = ..., boto3_client_kwargs: Incomplete | None = None) -> None: ...
    def __call__(self, request: requests.Request): ...
