from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError

from app.database import engine, Base
from app.controllers import RootController, ItemController, AuthController
from app.exceptions.handlers import (
    AppException,
    app_exception_handler,
    validation_exception_handler,
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(
    title="FastAPI JWT Auth",
    description="FastAPI with JWT Authentication and PostgreSQL",
    version="1.0.0",
)

# Register exception handlers
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

# Register routers
app.include_router(RootController().router)
app.include_router(ItemController().router)
app.include_router(AuthController().router)
