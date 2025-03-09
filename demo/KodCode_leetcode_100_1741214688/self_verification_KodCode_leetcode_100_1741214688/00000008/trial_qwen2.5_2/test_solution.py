from solution import *

from solution import min_swaps_to_target

def test_min_swaps_to_target():
    assert min_swaps_to_target(["abc","def","ghi"], "defabcghi") == 2
    assert min_swaps_to_target(["foo","bar","baz"], "barbazfoo") == 3
    assert min_swaps_to_target(["hello","world","hello"], "helloworldhello") == -1  # Duplicate of "hello" and "world" in source and target creates an error
    assert min_swaps_to_target(["a","b","c"], "cba") == -1
    assert min_swaps_to_target(["one","two","three"], "threeonetwo") == 2
    assert min_swaps_to_target(["cat","dog","mouse"], "catdogmouse") == 0