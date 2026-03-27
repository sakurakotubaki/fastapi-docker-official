from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.auth import UserCreate, UserLogin, UserResponse, Token
from app.services.auth_service import AuthService
from app.dependencies.auth import get_current_user


class AuthController:
    def __init__(self):
        self.router = APIRouter(prefix="/auth", tags=["auth"])
        self.router.add_api_route(
            "/register",
            self.register,
            methods=["POST"],
            response_model=UserResponse,
            status_code=status.HTTP_201_CREATED,
        )
        self.router.add_api_route(
            "/login",
            self.login,
            methods=["POST"],
            response_model=Token,
        )
        self.router.add_api_route(
            "/me",
            self.get_me,
            methods=["GET"],
            response_model=UserResponse,
        )

    def register(
        self,
        user_data: UserCreate,
        db: Session = Depends(get_db),
    ) -> UserResponse:
        auth_service = AuthService(db)
        try:
            user = auth_service.register(user_data)
            return UserResponse.model_validate(user)
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=str(e),
            )

    def login(
        self,
        user_data: UserLogin,
        db: Session = Depends(get_db),
    ) -> Token:
        auth_service = AuthService(db)
        token = auth_service.login(user_data.email, user_data.password)
        if not token:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password",
            )
        return token

    def get_me(
        self,
        current_user: User = Depends(get_current_user),
    ) -> UserResponse:
        return UserResponse.model_validate(current_user)
