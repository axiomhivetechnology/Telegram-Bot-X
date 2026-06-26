import pytest
from unittest.mock import MagicMock, patch
from templates.python.agent_system.agent import should_continue

def test_should_continue_end():
    state = {'messages': [MagicMock(tool_calls=[])]}
    assert should_continue(state) == "end"

def test_should_continue_continue():
    message = MagicMock()
    message.tool_calls = [{'name': 'test_tool'}]
    state = {'messages': [message]}
    assert should_continue(state) == "continue"
