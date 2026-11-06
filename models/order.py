from pydantic import BaseModel, ConfigDict
from typing import Literal
from datetime import datetime

class Order(BaseModel):
    model_config = ConfigDict(extra='forbid')

    id: int | None = None
    petId: int | None = None
    quantity: int | None = None
    shipDate: datetime | None = None
    status: Literal["placed", "approved", "delivered"] | None = None
    complete: bool | None = None