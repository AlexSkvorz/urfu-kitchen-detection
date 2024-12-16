import joblib
from fastapi import APIRouter, Body
from typing import Annotated
from sklearn.feature_extraction.text import TfidfVectorizer

from app.schemes.kitchen_schemes import ReadKitchenRequestSchema, ReadKitchenResponseSchema


kitchen_router = APIRouter(
    prefix="/kitchen",
    tags=["kitchen"]
)


model = joblib.load("whats_cooking.pkl")

tfidf = joblib.load("tfidf_vectorizer.pkl")

label_encoder = joblib.load("label_encoder.pkl")


@kitchen_router.post(
    path="/",
    description="Получить тип кухни",
    response_model=ReadKitchenResponseSchema
)
async def read_kitchen(
        ingredient_list: Annotated[ReadKitchenRequestSchema, Body(...)]
) -> ReadKitchenResponseSchema:
    ingredients_str = " ".join(ingredient_list.ingredients)

    ingredients = tfidf.transform([ingredients_str])
    predictions = model.predict(ingredients)
    kitchen = label_encoder.inverse_transform(predictions)

    return ReadKitchenResponseSchema(kitchen=kitchen[0])
