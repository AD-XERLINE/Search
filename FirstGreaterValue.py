def FGV(lst,key):
    for i in range(len(lst)):

        if int(lst[i]) > int(key):
            return print(lst[i])    
        if i == len(lst)-1:
            return print("No First Greater Value")

inp = input('Enter Input : ').split('/')
for i in range(len(inp)):
    inp[i] = inp[i].split(" ")

inp[0] = map(int,inp[0])
# print(inp)
inp[0] = sorted(inp[0])


for j in range(len(inp[1])):
    FGV(inp[0],inp[1][j])