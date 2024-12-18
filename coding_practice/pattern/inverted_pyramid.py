# Inverted Pyramid Star Pattern


n = 5

# Outer loop runs N times, once for each row
for i in range(1, n+1):
    # Inner loop prints 'i - 1' spaces
    for j in range(1, i):
        print(" ", end="")
    # Inner loop prints '2 * (N - i) + 1' stars
    for j in range(1, 2 * (n - i) + 2): # (8+2)=10 , (1,10) = 9 stars
        print("*", end="")

    print()

