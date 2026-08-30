from bson import ObjectId
from app.db.mongodb import users_collection
from app.schemas.user import UserCreate, UserUpdate


# create user
def create_user(user: UserCreate):

    result = users_collection.insert_one(user.model_dump())

    return {"id": str(result.inserted_id), **user.model_dump()}


# get all user
def get_users():

    users = users_collection.find()

    return [
        {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"],
            "age": user["age"],
        }
        for user in users
    ]


# get user by Id
def get_user(user_id: str):

    user = users_collection.find_one({"_id": ObjectId(user_id)})

    if user is None:
        return None

    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age": user["age"],
    }


# update user
def update_user(user_id: str, user: UserUpdate):

    update_data = user.model_dump(exclude_none=True)

    result = users_collection.update_one(
        {"_id": ObjectId(user_id)}, {"$set": update_data}
    )

    return result.modified_count


# delete user
def delete_user(user_id: str):

    result = users_collection.delete_one({"_id": ObjectId(user_id)})

    return result.deleted_count
