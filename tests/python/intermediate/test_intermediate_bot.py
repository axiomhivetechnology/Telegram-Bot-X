import pytest
from unittest.mock import AsyncMock, MagicMock
from templates.python.intermediate.bot import start, gender, cancel
from telegram.ext import ConversationHandler

@pytest.mark.asyncio
async def test_start_conversation():
    update = MagicMock()
    update.message.reply_text = AsyncMock()
    context = MagicMock()

    result = await start(update, context)
    assert result == 0  # GENDER state
    update.message.reply_text.assert_called()

@pytest.mark.asyncio
async def test_gender_selection():
    update = MagicMock()
    update.message.text = "Boy"
    update.message.from_user.first_name = "Alice"
    update.message.reply_text = AsyncMock()
    context = MagicMock()

    result = await gender(update, context)
    assert result == 1  # PHOTO state
    update.message.reply_text.assert_called()

@pytest.mark.asyncio
async def test_cancel_conversation():
    update = MagicMock()
    update.message.from_user.first_name = "Alice"
    update.message.reply_text = AsyncMock()
    context = MagicMock()

    result = await cancel(update, context)
    assert result == ConversationHandler.END
    update.message.reply_text.assert_called()
