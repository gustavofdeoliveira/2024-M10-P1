from sqlmodel import Field

from app.model.base_model import BaseModel


class Order(BaseModel, table=True):
    user_token: str = Field()
    user_name: str = Field()
    user_email: str = Field()
    description: str = Field(default=None, nullable=True)
