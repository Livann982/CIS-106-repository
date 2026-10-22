a, b = 1, 1
print("First 20 numbers in the Fibonacci sequence:")
for i in range(21):
    print(a, end=", " if i < 19 else "\n")
    a, b = b, a + b