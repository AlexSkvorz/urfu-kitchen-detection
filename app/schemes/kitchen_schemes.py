from typing import List
from pydantic import BaseModel, Field


class ReadKitchenRequestSchema(BaseModel):
    ingredients: List[str] = Field(
        description="Список ингредиентов на английском",
        examples=[["plain flour", "ground pepper", "salt"], ["salt", "oil"]]
    )


class ReadKitchenResponseSchema(BaseModel):
    kitchen: str = Field(description="Кухня", examples=["greek", "filipino"])
