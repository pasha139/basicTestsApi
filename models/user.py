from pydantic import BaseModel, ConfigDict

class User(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id: int | None = None
    username: str | None = None
    firstName: str | None = None
    lastName: str | None = None
    email: str | None = None
    password: str | None = None
    phone: str | None = None
    userStatus: int | None = None

