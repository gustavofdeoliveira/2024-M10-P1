from sqlalchemy.orm import Session

from app.model.order import Order
from app.repository.base_repository import BaseRepository


class OrderRepository(BaseRepository):
    def __init__(self, session_factory):
        self.session_factory = session_factory
        super().__init__(session_factory, Order)
