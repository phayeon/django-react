import os
import sys
from fastapi_sqlalchemy.middleware import DBSessionMiddleware

from .env import DB_url

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
baseurl = os.path.dirname(os.path.abspath(__file__))

from fastapi import FastAPI, APIRouter
from .routers.user import router as user_router
from .routers.post import router as post_router

router = APIRouter()
router.include_router(user_router, prefix="/users", tags=["users"])
router.include_router(post_router, prefix="/posts", tags=["posts"])

app = FastAPI()
app.include_router(router)
app.add_middleware(DBSessionMiddleware, db_url=DB_url)


@app.get("/")
async def root():
    return {"message ": " Welcome Fastapi"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
