import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from templates.python.beginner.bot import start, echo

@pytest.mark.asyncio
async def test_start_command():
    update = MagicMock()
    update.effective_chat.id = 12345
    context = MagicMock()
    context.bot.send_message = AsyncMock()

    await start(update, context)
    context.bot.send_message.assert_called_with(
        chat_id=12345,
        text="I'm a bot, please talk to me!"
    )

@pytest.mark.asyncio
async def test_echo_handler():
    update = MagicMock()
    update.effective_chat.id = 12345
    update.message.text = "Hello World"
    context = MagicMock()
    context.bot.send_message = AsyncMock()

    await echo(update, context)
    context.bot.send_message.assert_called_with(
        chat_id=12345,
        text="Hello World"
    )

def test_run_bot_missing_token():
    with patch('templates.python.beginner.bot.TOKEN', None):
        from templates.python.beginner.bot import run_bot
        # Should print error and return
        run_bot()
