from fastapi import FastAPI, APIRouter


class RootController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.read_root, methods=["GET"])

    def read_root(self):
        return {"Hello": "FastAPI"}


class ItemController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/items/{item_id}", self.read_item, methods=["GET"])

    def read_item(self, item_id: int, q: str | None = None):
        return {"item_id": item_id, "q": q}


app = FastAPI()
app.include_router(RootController().router)
app.include_router(ItemController().router)