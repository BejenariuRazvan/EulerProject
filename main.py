def problema1():
    sum = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)

def problema2():
    x = 1
    y = 2
    sum = 0
    while y <= 4000000:
        if y % 2 == 0:
            sum += y
        x, y = y, x
        y += x
    print(sum)

if __name__=="__main__":
    problema1()
    problema2()