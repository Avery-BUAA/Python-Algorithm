import math
def divide(dividend, divisor):
    # Write your code here
    m = dividend/divisor
    res = list(math.modf(m))
    a = res[0]
    b = res[1]
    b = str(b)
    for i in range(len(b)):
