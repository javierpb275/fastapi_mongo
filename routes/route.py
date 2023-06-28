from fastapi import APIRouter
from pymongo import ReturnDocument

from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial, individual_serial
from bson import ObjectId

router = APIRouter()


# GET Request Method
@router.get("/")
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


# POST Request Method
@router.post("/")
async def create_todo(todo: Todo):
    inserted_result = collection_name.insert_one(dict(todo))
    inserted_id = inserted_result.inserted_id
    inserted_todo = collection_name.find_one({"_id": inserted_id})
    return individual_serial(inserted_todo)


# PUT Request Method
@router.put("/{id}")
async def update_todo(id: str, todo: Todo):
    updated_todo = collection_name.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(todo)},
        return_document=ReturnDocument.AFTER
    )
    return individual_serial(updated_todo)


# DELETE Request Method
@router.delete("/{id}")
async def delete_todo(id: str):
    deleted_todo = collection_name.find_one({"_id": ObjectId(id)})
    collection_name.delete_one({"_id": ObjectId(id)})
    return individual_serial(deleted_todo)

