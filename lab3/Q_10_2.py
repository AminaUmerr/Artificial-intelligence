m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
result = []

for i in range(m):
    row = []
    for j in range(n):
        row.append(i * j)  
    result.append(row)

# Print the result in the expected format
print("[", end="")
for i in range(m):
    if i > 0:
        print(" ", end="")  
    print("[", end="")
    for j in range(n):
        print(result[i][j], end="")
        if j < n - 1:
            print(", ", end="")  s
    print("]", end="")
    if i < m - 1:
        print(",", end="")  
print("]")
