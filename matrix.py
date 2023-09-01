# Sum of two matrix
x=[[10,20,30],
    [40,50,60],
    [70,80,90]]

y=[[70,80,90],
    [40,50,60],
    [10,20,30]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[i][j]= x[i][j]+y[i][j]
for r in result:
    print(r)
    




