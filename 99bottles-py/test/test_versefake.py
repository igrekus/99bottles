from lib.conftest import VerseFake

from typing import Callable


def test_plays_verse_role():
    assert isinstance(type(getattr(VerseFake, 'lyrics')), Callable)
