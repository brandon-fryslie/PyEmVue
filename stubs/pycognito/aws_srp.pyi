from .exceptions import ForceChangePasswordException as ForceChangePasswordException, SMSMFAChallengeException as SMSMFAChallengeException, SoftwareTokenMFAChallengeException as SoftwareTokenMFAChallengeException
from _typeshed import Incomplete

N_HEX: str
G_HEX: str
INFO_BITS: Incomplete
WEEKDAY_NAMES: Incomplete
MONTH_NAMES: Incomplete

def hash_sha256(buf): ...
def hex_hash(hex_string): ...
def hex_to_long(hex_string): ...
def long_to_hex(long_num): ...
def get_random(nbytes): ...
def pad_hex(long_int): ...
def compute_hkdf(ikm, salt): ...
def calculate_u(big_a, big_b): ...
def generate_hash_device(device_group_key, device_key): ...

class AWSSRP:
    SMS_MFA_CHALLENGE: str
    SOFTWARE_TOKEN_MFA_CHALLENGE: str
    NEW_PASSWORD_REQUIRED_CHALLENGE: str
    PASSWORD_VERIFIER_CHALLENGE: str
    DEVICE_SRP_CHALLENGE: str
    DEVICE_PASSWORD_VERIFIER_CHALLENGE: str
    username: Incomplete
    password: Incomplete
    pool_id: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    client: Incomplete
    device_key: Incomplete
    device_group_key: Incomplete
    device_password: Incomplete
    big_n: Incomplete
    val_g: Incomplete
    val_k: Incomplete
    small_a_value: Incomplete
    large_a_value: Incomplete
    access_token: Incomplete
    device_name: Incomplete
    cognito_idp_url: Incomplete
    def __init__(self, username, password, pool_id, client_id, pool_region: Incomplete | None = None, client: Incomplete | None = None, client_secret: Incomplete | None = None, device_key: Incomplete | None = None, device_group_key: Incomplete | None = None, device_password: Incomplete | None = None) -> None: ...
    def generate_random_small_a(self): ...
    def calculate_a(self): ...
    def get_password_authentication_key(self, username, password, server_b_value, salt): ...
    def get_device_authentication_key(self, device_group_key, device_key, device_password, server_b_value, salt): ...
    def get_auth_params(self): ...
    @staticmethod
    def get_secret_hash(username, client_id, client_secret): ...
    @staticmethod
    def get_cognito_formatted_timestamp(input_datetime): ...
    def process_challenge(self, challenge_parameters, request_parameters): ...
    def process_device_challenge(self, challenge_parameters): ...
    def authenticate_user(self, client: Incomplete | None = None, client_metadata: Incomplete | None = None): ...
    def set_new_password_challenge(self, new_password, client: Incomplete | None = None): ...
    def confirm_device(self, tokens, device_name: Incomplete | None = None): ...
    def update_device_status(self, is_remembered, access_token, device_key): ...
    def forget_device(self, access_token, device_key): ...
