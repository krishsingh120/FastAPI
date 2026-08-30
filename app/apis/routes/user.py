from fastapi import APIRouter, HTTPException

from app.schemas.user import (
    UserCreate,
    UserResponse,
    UserUpdate,
)
from app.services.user import (
    create_user,
    get_users,
    get_user,
    update_user,
    delete_user,
)

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create(user: UserCreate):
    return create_user(user)


@router.get("/", response_model=list[UserResponse])
def read_all():
    return get_users()


@router.get("/{user_id}", response_model=UserResponse)
def read_one(user_id: str):

    user = get_user(user_id)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    return user


@router.put("/{user_id}")
def update(user_id: str, user: UserUpdate):

    updated = update_user(user_id, user)

    if updated == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User updated"}


@router.delete("/{user_id}")
def delete(user_id: str):

    deleted = delete_user(user_id)

    if deleted == 0:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted"}
