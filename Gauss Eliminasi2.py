print("==============================")
print("====== GAUSS ELIMINASION =======")
print("==============================")
print("Nama     : Bayu Wicaksono")
print("NIM      : 23106050002")
print("Prodi    : Informatika")
print("==============================")
print("Hasil x, y, z adalah : ")

#start
matrix = [[3, -0.1, -0.2, 7.85],
          [0.1, 7, -0.3, -19.3],
          [0.3, -0.2, 10, 71.4]]

(columns, rows) = (len(matrix), len(matrix[0]))
for y in range(0, columns):
    maxrow = y

    for y2 in range(y + 1, columns):
        if abs(matrix[y2][y]) > abs(matrix[maxrow][y]):
            maxrow = y2
    (matrix[y], matrix[maxrow]) = (matrix[maxrow], matrix[y])

    for y2 in range(y + 1, columns):
        c = matrix[y2][y] / matrix[y][y]
        for x in range(y, rows):
            matrix[y2][x] -= matrix[y][x] * c    

for y in range(columns - 1, 0 - 1, -1):
    c = matrix[y][y]
    for y2 in range(0, y):
        for x in range(rows - 1, y - 1, -1):
            matrix[y2][x] -= matrix[y][x] * matrix[y2][y] / c
    matrix[y][y] /= c
    for x in range(columns, rows):
        matrix[y][x] /= c
#end
for row in matrix:
    print (row[3])