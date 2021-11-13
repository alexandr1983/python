n = int(input("Enter number: "))
while n <= 0:
    n = int(input("!=0 or <0: "))
n1 = n
i = 0
while n > 0:
    k = n % 10
    if k > i:
        i = k
        if i == 9:
            break
    n = n // 10

print(f"Maximum in {n1} = {i}")
