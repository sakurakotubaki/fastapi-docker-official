from fastapi import APIRouter


class RootController:
    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.read_root, methods=["GET"])

    def read_root(self):
        return {"Hello": "FastAPI"}
