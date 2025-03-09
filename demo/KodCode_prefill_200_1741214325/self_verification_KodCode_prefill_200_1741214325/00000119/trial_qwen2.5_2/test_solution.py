from solution import *

import re

def test_replace_surrounded_substring():
    assert replace_surrounded_substring("hello world, world is great", "world", "earth") == "hello earth, earth is great"
    assert replace_surrounded_substring("hello  world, world is great", "world", "planet") == "hello  planet, planet is great"
    assert replace_surrounded_substring("hello_world, world is great", "world", "planet") == "hello_world, world is great"
    assert replace_surrounded_substring("hello  world world, world is great", "world", "planet") == "hello  planet planet, planet is great"
    assert replace_surrounded_substring("hello world", "world", "planet") == "hello planet"
    assert replace_surrounded_substring("hello world", "planet", "world") == "hello world"
    assert replace_surrounded_substring("hello  world  world  world", "world", "") == "hello  2"