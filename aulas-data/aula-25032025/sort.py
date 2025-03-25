ls = [7, 2, 4, 5]
chavetroca = 1
while (chavetroca == 1):
    chavetroca = 0
    for i in range(0, 3):
        if ls[i] > ls[i+1]:
            temp = ls[i]
            ls[i] = ls[i+1]
            ls[i+1] = temp
            chavetroca = 1
print(ls)