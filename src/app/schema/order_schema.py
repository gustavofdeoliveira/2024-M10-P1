# many to many schemas must be contained at one schema file to prevent cyclic reference
from typing import List, Optional

from pydantic import BaseModel

from app.schema.base_schema import FindBase, ModelBaseInfo, SearchOptions
from app.util.schema import AllOptional

class BaseOrder(BaseModel):
    user_token: str
    user_name: str
    user_email: str
    description: str

    class Config:
        orm_mode = True


class Order(ModelBaseInfo, BaseOrder, metaclass=AllOptional):
    ...


class FindOrder(FindBase, BaseOrder, metaclass=AllOptional):
    id__in: str


class UpsertOrder(BaseOrder, metaclass=AllOptional):
    ...


class FindOrderResult(BaseModel):
    founds: Optional[List[Order]]
    search_options: Optional[SearchOptions]


