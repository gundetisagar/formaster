

REQUEST_BODY_JSON = """
{
    "username": "string",
    "password": "string"
}
"""


RESPONSE_200_JSON = """
{
    "user_id": 1,
    "access_token": "string",
    "refresh_token": "string",
    "expires_in": 1
}
"""

RESPONSE_401_JSON = """
{
    "response": "string",
    "http_status_code": 1,
    "res_status": "INVALID_USERNAME"
}
"""

