'''
Duara Internship Code Challenge

Task 2

Write a function that divides two numbers and returns their quotient.
Use recursive subtraction to find the quotient.
The function should only take two arguments.
'''


def quotient(numerator, denominator):
    if 0 <= numerator < denominator:
        return 0
    if numerator >= denominator:
        return quotient(numerator - denominator, denominator) + 1
    if numerator < 0:
        return quotient(numerator + denominator, denominator) - 1

print quotient(23.6,5.6)
