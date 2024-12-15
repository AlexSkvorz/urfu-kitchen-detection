from fastapi import APIRouter, Body
from typing import Annotated

from app.schemes.kitchen_schemes import ReadKitchenRequestSchema, ReadKitchenResponseSchema


kitchen_router = APIRouter(
    prefix="/kitchen",
    tags=["kitchen"]
)


@kitchen_router.post(
    path="/",
    description="Получить тип кухни",
    response_model=ReadKitchenResponseSchema
)
async def read_kitchen(
        ingredient_list: Annotated[ReadKitchenRequestSchema, Body(...)]
) -> ReadKitchenResponseSchema:
    ingredients = ", ".join(ingredient_list.ingredients)

    return ReadKitchenResponseSchema(kitchen="russian")
