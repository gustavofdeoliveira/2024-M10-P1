from dependency_injector import containers, providers

from app.core.config import configs
from app.core.database import Database
from app.repository import *
from app.services import *


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoints.auth",
            "app.api.v1.endpoints.order",
            "app.api.v1.endpoints.user",
            "app.core.dependencies",
        ]
    )

    db = providers.Singleton(Database, db_url=configs.DATABASE_URI)


    order_repository = providers.Factory(OrderRepository, session_factory=db.provided.session)
    user_repository = providers.Factory(UserRepository, session_factory=db.provided.session)

    auth_service = providers.Factory(AuthService, user_repository=user_repository)
    order_service = providers.Factory(OrderService, order_repository=order_repository)
    user_service = providers.Factory(UserService, user_repository=user_repository)
