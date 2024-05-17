from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.core.dependencies import get_current_active_user
from app.model.user import User
from app.schema.base_schema import Blank
from app.schema.order_schema import FindOrder, FindOrderResult, Order, UpsertOrder
from app.services.order_service import OrderService

router = APIRouter(
    prefix="/pedidos",
    tags=["pedidos"],
)


@router.get("", response_model=FindOrderResult)
@inject
async def get_order_list(
    find_query: FindOrder = Depends(),
    service: OrderService = Depends(Provide[Container.order_service]),
):
    return service.get_list(find_query)


@router.get("/{order_id}", response_model=Order)
@inject
async def get_order(
    order_id: int,
    service: OrderService = Depends(Provide[Container.order_service]),
):
    return service.get_by_id(order_id)


@router.post("/novo", response_model=Order.id)
@inject
async def create_order(
    order: UpsertOrder,
    service: OrderService = Depends(Provide[Container.order_service]),
    current_user: User = Depends(get_current_active_user),
):  
    print(order)
    return order[0].id


@router.patch("/{order_id}", response_model=Order)
@inject
async def update_order(
    order_id: int,
    order: UpsertOrder,
    service: OrderService = Depends(Provide[Container.order_service]),
    current_user: User = Depends(get_current_active_user),
):
    return service.patch(order_id, order)


@router.delete("/{order_id}", response_model=Blank)
@inject
async def delete_order(
    order_id: int,
    service: OrderService = Depends(Provide[Container.order_service]),
    current_user: User = Depends(get_current_active_user),
):
    return service.remove_by_id(order_id)
