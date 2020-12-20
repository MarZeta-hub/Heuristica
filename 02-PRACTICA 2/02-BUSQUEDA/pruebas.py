a = [1, 0, 0, 0]
b = [0, 1, 0, 0]
c = []
for i in range(len(a)):
    print (a[i], b[i])
    if a[i] != b[i]:
        print(i)
        a[i] = 0
        b[i] = 0


print (a, b)