from solution import *

def test_string_to_int():
    assert string_to_int("42") == 42
    assert string_to_int("   -42") == -42
    assert string_to_int("4193 with words") == 4193
    assert string_to_int("words and 987") == 0
    assert string_to_int("-91283472332") == -2147483648 #超出int范围的负数转换为最小int值
    assert string_to_int("+1") == 1
    assert string_to_int("") == 0
    assert string_to_int("    ") == 0
    assert string_to_int("+-2") == 0 # 混合符号，应该视为0
    assert string_to_int("2147483647") == 2147483647
    assert string_to_int("-2147483648") == -2147483648 # 按照32位整数范围调整
    assert string_to_int("2147483648") == 2147483647 # 超出范围的正数转换为最大int值