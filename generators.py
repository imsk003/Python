# def gencubes(n):
#     for num in range(n):
#         yield num**3

# for x in gencubes(10):
#     print(x)




def genfibon(n):
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b


for num in genfibon(10):
    print(num)

