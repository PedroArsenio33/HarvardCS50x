from cs50 import get_int

# prompts user for a size
while True:
    size = get_int("Size: ")
    if size <= 8 and size > 0:
        break

# builds structure based on size
for i in range(size):
    n = i+1
    print(" "*(size-n) + "#"*n + "  " + "#"*n)
