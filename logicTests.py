from unittest.mock import MagicMock
import pytest

from Logic import GameLogic


def test_logic_init():
    from Controller import Controller
    controller = Controller()
    logic = GameLogic(controller)
