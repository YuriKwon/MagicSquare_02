"""Tests for User entity."""

from uuid import uuid4

import pytest

from src.entity.user import User


def test_create_user_with_valid_data() -> None:
    """Create user when all domain inputs are valid."""
    # Arrange
    user_id = uuid4()

    # Act
    user = User(
        user_id=user_id,
        username="alice",
        email="alice@example.com",
    )

    # Assert
    assert user.user_id == user_id
    assert user.username == "alice"
    assert user.email == "alice@example.com"
    assert user.is_active is True


def test_create_user_raises_when_username_blank() -> None:
    """Raise ValueError when username is blank."""
    # Arrange
    user_id = uuid4()

    # Act
    with pytest.raises(ValueError) as exc_info:
        User(
            user_id=user_id,
            username="   ",
            email="alice@example.com",
        )

    # Assert
    assert str(exc_info.value) == "username must not be blank"


def test_create_user_raises_when_email_invalid() -> None:
    """Raise ValueError when email is malformed."""
    # Arrange
    user_id = uuid4()

    # Act
    with pytest.raises(ValueError) as exc_info:
        User(
            user_id=user_id,
            username="alice",
            email="alice.example.com",
        )

    # Assert
    assert str(exc_info.value) == "email must contain a single '@'"


def test_deactivate_returns_inactive_user() -> None:
    """Return copied inactive user on deactivate."""
    # Arrange
    user = User(
        user_id=uuid4(),
        username="alice",
        email="alice@example.com",
    )

    # Act
    deactivated = user.deactivate()

    # Assert
    assert deactivated.is_active is False
    assert deactivated.user_id == user.user_id
    assert deactivated.username == user.username
    assert deactivated.email == user.email
