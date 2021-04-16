row1=int(input("enter the numbr of row of 1st matrix: "))
col1=int(input("enterthe number of columns of 1st matrix: "))
max1=[[[]for j in range(col1)]for i in range(row1)]
for i in range(row1):
    for j in range(col1):
        max1[i][j]=int(input("enter the element: "))
print(max1)

