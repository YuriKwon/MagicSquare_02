"""User entity for MagicSquare domain."""

from dataclasses import dataclass
from uuid import UUID


@dataclass(frozen=True, slots=True)
class User:
    """Represent a user in the domain layer.

    This entity owns user identity and domain-level validation rules.

    Attributes:
        user_id: Unique identifier of the user.
        username: Unique display name in the domain.
        email: Contact email of the user.
        is_active: Whether the user is active in the system.
    """

    user_id: UUID
    username: str
    email: str
    is_active: bool = True

    def __post_init__(self) -> None:
        """Validate invariants required by the domain."""
        self._validate_username(self.username)
        self._validate_email(self.email)

    def deactivate(self) -> "User":
        """Return a new user entity marked as inactive.

        Returns:
            User: A copied user instance with `is_active` set to False.
        """
        return User(
            user_id=self.user_id,
            username=self.username,
            email=self.email,
            is_active=False,
        )

    @staticmethod
    def _validate_username(username: str) -> None:
        """Validate username against basic domain rules.

        Args:
            username: Candidate username string.

        Raises:
            ValueError: If username is blank after trimming.
        """
        if not username.strip():
            raise ValueError("username must not be blank")

    @staticmethod
    def _validate_email(email: str) -> None:
        """Validate email format for domain safety.

        Args:
            email: Candidate email string.

        Raises:
            ValueError: If email does not include exactly one '@'.
        """
        if email.count("@") != 1:
            raise ValueError("email must contain a single '@'")
