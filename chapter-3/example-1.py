import pytest

def average(L):
    if not L:
        return none
    return sum(L)/len(L)


# if __name__ == "__main__":
#     L=[1,2,3,4,5]
#     print(average(L))


'''better option'''
# if __name__=="__main__":
#     L =[1,2,3,4,5]
#
#     expected_result =3.0
#     result = average(L)
#
#     if expected_result == result:
#         print("test passed")
#     else:
#         print("test failed!","received:", result, "expected:", expected_result)


'''Using Assert'''

# if __name__ == "__main__":
#     L=[1,2,3,4,5]
#     expected_result = 4.0
#     assert expected_result == average(L), "average() produced incorrect result"

def test_average():
    assert 3.0 == average([1, 2, 3, 4, 5])


# def test_average():
#     test_cases = [
#         {
#             "name":"simple case 1",
#             "input":[1, 2, 3],
#             "expected":2.0
#         },
#         {
#             "name":"simple case 2",
#             "input":[1, 2, 3, 4],
#             "expected":2.0
#         },
#         {
#             "name": "list with one item",
#             "input":[100],
#             "expected":100.0
#         },
#         {
#             "name":"empty list",
#             "input":[],
#             "expected":None
#         }
#     ]
#
#     for test_case in test_cases:
#         assert  test_case["expected"] == average(test_case["input"], test_case["name"])
