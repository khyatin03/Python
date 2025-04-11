from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float
    quantity: int

items = [
    {"id": 1, "name": "Apple", "price": 0.5, "quantity": 100},
    {"id": 2, "name": "Banana", "price": 0.3, "quantity": 120},
    {"id": 3, "name": "Orange", "price": 0.4, "quantity": 90},
    {"id": 4, "name": "Grapes", "price": 1.2, "quantity": 75},
    {"id": 5, "name": "Mango", "price": 1.5, "quantity": 60},
    {"id": 6, "name": "Pineapple", "price": 2.0, "quantity": 30},
    {"id": 7, "name": "Kiwi", "price": 1.0, "quantity": 50},
    {"id": 8, "name": "Watermelon", "price": 3.0, "quantity": 20},
    {"id": 9, "name": "Papaya", "price": 1.3, "quantity": 25},
    {"id": 10, "name": "Strawberry", "price": 2.5, "quantity": 40},
]


@app.get("/items")
def get_items():
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items")
def create_item(item: Item):
    for existing in items:
        if existing["id"] == item.id:
            raise HTTPException(status_code=400, detail="Item with this ID already exists")
    items.append(item.dict())
    return item

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            items[index] = updated_item.dict()
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item["id"] == item_id:
            deleted = items.pop(index)
            return {"message": "Item deleted", "item": deleted}
    raise HTTPException(status_code=404, detail="Item not found")

