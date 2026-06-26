import pytest
import os
from unittest.mock import AsyncMock, MagicMock, patch

# Mocking aiosqlite before importing the bot module
@pytest.fixture(autouse=True)
def mock_db():
    with patch('aiosqlite.connect') as mock:
        mock.return_value.__aenter__.return_value = AsyncMock()
        yield mock

from templates.python.advanced.bot import cmd_start, cmd_stats

@pytest.mark.asyncio
async def test_cmd_start():
    message = AsyncMock()
    message.from_user.id = 123
    message.from_user.username = "testuser"
    message.from_user.first_name = "Test"
    message.answer = AsyncMock()

    await cmd_start(message)
    message.answer.assert_called()

@pytest.mark.asyncio
async def test_cmd_stats():
    message = AsyncMock()
    message.answer = AsyncMock()

    # Setup the mock for fetching count
    with patch('aiosqlite.connect') as mock_conn:
        db = AsyncMock()
        cursor = AsyncMock()
        cursor.fetchone = AsyncMock(return_value=(5,))
        cursor.close = AsyncMock()
        db.execute = AsyncMock(return_value=cursor)
        mock_conn.return_value.__aenter__.return_value = db

        await cmd_stats(message)
        message.answer.assert_called_with("Total registered users: 5")
