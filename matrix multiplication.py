row1=int(input("enter the numbr of row of 1st matrix: "))
col1=int(input("enterthe number of columns of 1st matrix: "))
max1=[[[]for j in range(col1)]for i in range(row1)]
for i in range(row1):
    for j in range(col1):
        max1[i][j]=int(input("enter the element: "))
print(max1)
row2=int(input("enter the number of rows in 2nd matrix"))
col2=int(input("enter the number of columns of 2nd matrix"))
max2=[[[]for j in range(col2)]for i in range(row2)]
for i in range(row2):
    for j in range(col2):
        max2=int(input("enter the element"))
print(max2)
