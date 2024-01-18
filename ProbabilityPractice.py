l = [i for i in range(1,1000)]

count = 0
for i in l:
    if i % 3 != 0 or i % 5 != 0:
        count+= 1

print(count)