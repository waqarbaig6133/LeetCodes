class Solution:
    def __init__(self):
        pass
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        a = [int(y) for y in str(x)]
        if x % sum(a) == 0:
            return sum(a)
        else:
            return -1
#31 ms with 16.5mb ram usage
