from typing import Callable

from lib.bottles import CountdownSong
from lib.conftest import VerseFake


def test_plays_verse_role():
    assert isinstance(type(getattr(VerseFake, 'lyrics')), Callable)


def test_verse():
    expected = 'This is verse 500.\n'
    assert CountdownSong(VerseFake).verse(500) == expected


def test_verses():
    expected = 'This is verse 99.\n' \
               '\n' \
               'This is verse 98.\n' \
               '\n' \
               'This is verse 97.\n'
    assert CountdownSong(VerseFake).verses(99, 97) == expected


def test_song():
    expected = 'This is verse 47.\n' \
               '\n' \
               'This is verse 46.\n' \
               '\n' \
               'This is verse 45.\n' \
               '\n' \
               'This is verse 44.\n' \
               '\n' \
               'This is verse 43.\n'
    assert CountdownSong(VerseFake, 47, 43).song() == expected
