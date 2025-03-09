from solution import *

def test_frequent_itemsets():
    transactions = [
        ['apple', 'banana', 'cherry'],
        ['banana', 'cherry'],
        ['apple', 'banana'],
        ['apple', 'banana', 'cherry'],
        ['banana', 'cherry']
    ]
    result = frequent_itemsets(transactions, 2)
    assert ['banana', 'cherry'] in result, "Missed frequent item ['banana', 'cherry']"
    assert ['apple', 'cherry'] in result, "Missed frequent item ['apple', 'cherry']"
    assert ['apple', 'banana'] in result, "Missed frequent item ['apple', 'banana']"
    assert ['banana'] in result, "Missed frequent item ['banana']"
    assert ['cherry'] in result, "Missed frequent item ['cherry']"
    assert ['apple'] in result, "Missed frequent item ['apple']"