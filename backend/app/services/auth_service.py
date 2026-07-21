from sqlalchemy.orm import Session

from app.core.logger import logger
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserRegister
from app.utils.security import hash_password, verify_password
from app.utils.jwt_handler import create_access_token


class AuthService:

    @staticmethod
    def register_user(db: Session, user: UserRegister):

        logger.info(
            f"Registration attempt for email: {user.email}"
        )

        existing_user = UserRepository.get_user_by_email(
            db,
            user.email
        )

        if existing_user:
            logger.warning(
                f"Registration failed. Email already exists: {user.email}"
            )
            raise ValueError("Email already registered.")

        hashed_password = hash_password(user.password)

        new_user = UserRepository.create_user(
            db=db,
            email=user.email,
            password=hashed_password
        )

        logger.info(
            f"User registered successfully: {new_user.email}"
        )

        return new_user

    @staticmethod
    def login_user(
        db: Session,
        email: str,
        password: str
    ):

        logger.info(
            f"Login attempt for email: {email}"
        )

        existing_user = UserRepository.get_user_by_email(
            db,
            email
        )

        if not existing_user:
            logger.warning(
                f"Login failed. User not found: {email}"
            )
            raise ValueError("Invalid email or password.")

        if not verify_password(
            password,
            existing_user.password
        ):
            logger.warning(
                f"Login failed. Incorrect password for: {email}"
            )
            raise ValueError("Invalid email or password.")

        token = create_access_token(
            {
                "sub": existing_user.email
            }
        )

        logger.info(
            f"User logged in successfully: {existing_user.email}"
        )

        return {
            "access_token": token,
            "token_type": "bearer"
        }