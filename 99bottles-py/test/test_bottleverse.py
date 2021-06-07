from typing import Callable

from lib.bottles import BottleVerse


def test_plays_verse_role():
    assert isinstance(type(getattr(BottleVerse, 'lyrics')), Callable)


def test_verse_general_rule_upper_bound():
    expected = '99 bottles of beer on the wall, ' \
               '99 bottles of beer.\n' \
               'Take one down and pass it around, ' \
               '98 bottles of beer on the wall.\n'
    assert BottleVerse.lyrics(99) == expected


def test_verse_general_rule_lower_bound():
    expected = '3 bottles of beer on the wall, ' \
               '3 bottles of beer.\n' \
               'Take one down and pass it around, ' \
               '2 bottles of beer on the wall.\n'
    assert BottleVerse.lyrics(3) == expected


def test_verse_7():
    expected = '7 bottles of beer on the wall, ' \
               '7 bottles of beer.\n' \
               'Take one down and pass it around, ' \
               '1 six-pack of beer on the wall.\n'
    assert BottleVerse.lyrics(7) == expected


def test_verse_6():
    expected = '1 six-pack of beer on the wall, ' \
               '1 six-pack of beer.\n' \
               'Take one down and pass it around, ' \
               '5 bottles of beer on the wall.\n'
    assert BottleVerse.lyrics(6) == expected


def test_verse_2():
    expected = '2 bottles of beer on the wall, ' \
               '2 bottles of beer.\n' \
               'Take one down and pass it around, ' \
               '1 bottle of beer on the wall.\n'
    assert BottleVerse.lyrics(2) == expected


def test_verse_1():
    expected = '1 bottle of beer on the wall, ' \
               '1 bottle of beer.\n' \
               'Take it down and pass it around, ' \
               'no more bottles of beer on the wall.\n'
    assert BottleVerse.lyrics(1) == expected


def test_verse_0():
    expected = 'No more bottles of beer on the wall, ' \
               'no more bottles of beer.\n' \
               'Go to the store and buy some more, ' \
               '99 bottles of beer on the wall.\n'
    assert BottleVerse.lyrics(0) == expected
