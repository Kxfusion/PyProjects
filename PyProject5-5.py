def Converter(Str, Ints, N):
    Added = 0
    Base = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    Ints[len(Ints)-1] = Ints[len(Ints)-1]*10 + int(Str[N])
    if(N != len(Str) - 1): 
        for y in range(10):
            if(Str[N+1] == Base[y]):
                Ints, Added = Converter(Str, Ints, N+1)
    Added += 1
    return Ints, Added

Base = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
print("Give a set of random numbers")
Num = input()
Nums = []
Used = 0
for n in range(len(Num)):
    if(Used > 0):
        Used -= 1
        continue
    for x in range(10):
        if(Num[n] == Base[x]):
            Nums.append(int(Num[n]))
            if(n != len(Num) - 1): 
                for y in range(10):
                    if(Num[n+1] == Base[y]):
                        Nums, Used = Converter(Num, Nums, n+1)
                        break
Nums = sorted(Nums)
print("Numbers in order: ")
print(Nums)
