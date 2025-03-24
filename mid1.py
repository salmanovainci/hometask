l = []
start = ord('a') - 1

for i in range(4):
    a1 = []
    for j in range(4):
        if i == 0:
            if j == 0:
                value = '*'
            else:
                value = str(j)
        else:
            if j == 0:
                value = chr(start + i)
            else:
                value = 'x'
        a1.append(str(value))
    l.append(a1)

for i in l:
    print(' '.join(i))