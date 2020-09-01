def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True

    cur = 2
    while cur < num:
        if num % cur == 0:
            return False
        cur += 1

    return True

# num = int(input(f"Enter a number to test: "))
# print(is_prime(num))


prim = []
num = int(input(f"Enter max number to test: "))
for i in range(num):
    if is_prime(i):
        prim.append(i)

print(prim)
