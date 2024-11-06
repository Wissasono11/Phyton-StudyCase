#Diamond Pattern

print("\n👉👉👉Diamond Pattern👈👈👈")
rows = 8
#Upper Pyramid
for i in range(1, rows):
    for j in range(1, rows - i):
        print(' ', end=' ')
    for j in range(0, 2*i-1):
        print('*', end=' ')
    print()
#Lower Pyramid
for i in range(rows - 2, 0, -1):
    for j in range(1, rows - i):
        print(' ', end=' ')
    for j in range(1, 2 * i):
        print('*', end=' ')
    print()