from fastapi.middleware.cors import CORSMiddleware
from fastapi import Depends, FastAPI
from routers.UserRouter import router as router_users
from routers.ClientRouter import router as router_client
from routers.ProductRouter import router as router_product

api = FastAPI()

api.include_router(router_client)
api.include_router(router_product)
api.include_router(router_users)
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    # "https://informationmanagementuig3m3e10.herokuapp.com/"
]
api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)
