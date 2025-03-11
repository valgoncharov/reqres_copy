from fastapi import APIRouter, HTTPException, Query, Path, status
from typing import List, Optional
from datetime import datetime
from ...models.user import UserCreate, UserUpdate, UserResponse, UserListResponse, UserInDB, Support
from ...core.exceptions import UserNotFoundException, ValidationError

router = APIRouter()

# Simulated database (replace with actual database later)
users_db = {
    2: {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg",
        "created_at": datetime.now(),
        "updated_at": None
    }
}

support_info = {
    "url": "https://contentcaddy.io",
    "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
}


@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int = Path(..., description="The ID of the user to get", ge=1)
) -> UserResponse:
    """
    Get a specific user by ID.
    """
    if user_id not in users_db:
        raise UserNotFoundException(user_id)

    return {
        "data": users_db[user_id],
        "support": support_info
    }


@router.get("/users", response_model=UserListResponse)
async def list_users(
    page: int = Query(1, ge=1, description="Page number"),
    per_page: int = Query(6, ge=1, le=20, description="Items per page"),
    email: Optional[str] = Query(None, description="Filter users by email"),
    name: Optional[str] = Query(
        None, description="Filter users by first or last name")
) -> UserListResponse:
    """
    Get a list of users with pagination and filtering options.
    """
    # Filter users based on query parameters
    filtered_users = users_db.values()

    if email:
        filtered_users = [
            u for u in filtered_users if email.lower() in u["email"].lower()]

    if name:
        name = name.lower()
        filtered_users = [
            u for u in filtered_users
            if name in u["first_name"].lower() or name in u["last_name"].lower()
        ]

    # Convert to list for pagination
    filtered_users = list(filtered_users)
    total = len(filtered_users)
    total_pages = (total + per_page - 1) // per_page

    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page

    if page > total_pages and total > 0:
        raise ValidationError(
            f"Page {page} does not exist. Total pages: {total_pages}")

    page_users = filtered_users[start_idx:end_idx]

    return {
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages,
        "data": page_users,
        "support": support_info
    }


@router.post("/users", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate) -> UserResponse:
    """
    Create a new user.
    """
    # Check if email already exists
    if any(u["email"] == user.email for u in users_db.values()):
        raise ValidationError("Email already registered")

    # Simulate ID generation
    new_id = max(users_db.keys()) + 1 if users_db else 1

    new_user = {
        "id": new_id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "avatar": user.avatar,
        "created_at": datetime.now(),
        "updated_at": None
    }

    users_db[new_id] = new_user

    return {
        "data": new_user,
        "support": support_info
    }


@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int = Path(..., description="The ID of the user to update", ge=1),
    user: UserUpdate = None
) -> UserResponse:
    """
    Update a user's information.
    """
    if user_id not in users_db:
        raise UserNotFoundException(user_id)

    stored_user = users_db[user_id]

    # Check if new email already exists
    if user.email and user.email != stored_user["email"]:
        if any(u["email"] == user.email for u in users_db.values()):
            raise ValidationError("Email already registered")

    if user.email is not None:
        stored_user["email"] = user.email
    if user.first_name is not None:
        stored_user["first_name"] = user.first_name
    if user.last_name is not None:
        stored_user["last_name"] = user.last_name
    if user.avatar is not None:
        stored_user["avatar"] = user.avatar

    stored_user["updated_at"] = datetime.now()

    return {
        "data": stored_user,
        "support": support_info
    }


@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int = Path(..., description="The ID of the user to delete", ge=1)
):
    """
    Delete a user.
    """
    if user_id not in users_db:
        raise UserNotFoundException(user_id)

    del users_db[user_id]


@router.get("/users/{user_id}/avatar", response_model=dict)
async def get_user_avatar(
    user_id: int = Path(...,
                        description="The ID of the user to get avatar for", ge=1)
) -> dict:
    """
    Get a user's avatar URL.
    """
    if user_id not in users_db:
        raise UserNotFoundException(user_id)

    return {"avatar_url": users_db[user_id]["avatar"]}
