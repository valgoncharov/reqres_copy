from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Support(BaseModel):
    url: str
    text: str


class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UserResponse(BaseModel):
    data: UserData
    support: Support


@app.get("/api/users/2", response_model=UserResponse)
async def get_user():
    return {
        "data": {
            "id": 2,
            "email": "janet.weaver@reqres.in",
            "first_name": "Janet",
            "last_name": "Weaver",
            "avatar": "https://reqres.in/img/faces/2-image.jpg"
        },
        "support": {
            "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
            "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
