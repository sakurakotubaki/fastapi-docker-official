from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.config import settings
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.auth import UserCreate, Token


class AuthService:
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def __init__(self, db: Session):
        self.db = db
        self.user_repository = UserRepository(db)

    def hash_password(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, user_id: int) -> str:
        expire = datetime.utcnow() + timedelta(minutes=settings.jwt_expire_minutes)
        payload = {"sub": str(user_id), "exp": expire}
        return jwt.encode(
            payload, settings.jwt_secret_key, algorithm=settings.jwt_algorithm
        )

    def register(self, user_data: UserCreate) -> User:
        if self.user_repository.exists_by_email(user_data.email):
            raise ValueError("Email already registered")

        hashed_password = self.hash_password(user_data.password)
        return self.user_repository.create(user_data.email, hashed_password)

    def authenticate(self, email: str, password: str) -> User | None:
        user = self.user_repository.get_by_email(email)
        if not user:
            return None
        if not self.verify_password(password, user.hashed_password):
            return None
        return user

    def login(self, email: str, password: str) -> Token | None:
        user = self.authenticate(email, password)
        if not user:
            return None
        access_token = self.create_access_token(user.id)
        return Token(access_token=access_token)

    def get_user_by_id(self, user_id: int) -> User | None:
        return self.user_repository.get_by_id(user_id)
