from dataclasses import dataclass
from typing import List, Optional


@dataclass()
class UserAuthTokensDto:
    user_id: int
    access_token: str
    refresh_token: str
    expires_in: int


@dataclass()
class UserDetailsDto:
    user_id: int
    username: str
    is_admin: bool
