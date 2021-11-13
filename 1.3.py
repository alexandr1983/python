n = input("Enter number: ")

while n <= '0':
    n = input("!=0 or <0: ")

print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n +n)}")
