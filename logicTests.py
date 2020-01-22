from unittest.mock import MagicMock
import pytest

from Logic import GameLogic


def test_logic_init():
    from Controller import Controller
    controller = Controller()
    logic = GameLogic(controller)


def test_generate_values():
    from Controller import Controller
    controller = Controller()
    logic = GameLogic(controller)
    logic.generate_mines(10,10)
    assert len(logic.field_values) == 10
    assert len(logic.field_values[0]) == 10
