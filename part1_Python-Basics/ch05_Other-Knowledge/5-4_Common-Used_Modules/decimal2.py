from decimal import Decimal, getcontext

print(getcontext().prec)
getcontext().prec = 100
print(getcontext().prec)