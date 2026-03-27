from fastapi import APIRouter


class ItemController:
    def __init__(self):
        self.router = APIRouter(prefix="/items", tags=["items"])
        self.router.add_api_route("/{item_id}", self.read_item, methods=["GET"])

    def read_item(self, item_id: int, q: str | None = None):
        return {"item_id": item_id, "q": q}
