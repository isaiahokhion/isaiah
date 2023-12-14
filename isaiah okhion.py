p = float(input("Enter initial principal: "))

r = int(input("Enter interest rate: "))

n = float(input("Enter number of times interest applied: "))

t = float(input("Enter time period: "))

SI = str(p * (1+r*t))
CI = str(p * (1 + r/n) ** r * t)
print("Yusuf and sons")
print("SIMPLE INTEREST = " + SI)
print("COMPOUND INTEREST = " + CI)