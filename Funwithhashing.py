class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

def asscii(key):
    t = 0
    for i in range(len(key)):
        t += ord(key[i])
    return t

class hash:
    def __init__(self,maxSize,maxCollision):
        self.table = [None] * maxSize #สร้างตามจำนวน maxSize
        self.size = 0
        self.maxSize = maxSize
        self.maxCollision = maxCollision

    def add(self,key,i):
        # key ที่เข้ามาจะเหมือนชุดข้อมูลที่มี key,value เป็นก้อนๆนึงที่อยู่บน table เลย key.key, key.value เอาไว้ใช้
        # การแก้การชนแบบ quadratic คือการที่เราเอาตัวนับ collision มายกกำลังสองแล้วบวกกับ key จากนั้นจึงจะ mod อีกที
        index = (((asscii(key.key)) + (i*i)) % self.maxSize)
        # print(index)  
        if self.size == 0:
            self.table[index] = key
            self.size += 1
            return

        elif (self.table[index] == None) and (i < self.maxCollision):
            self.table[index] = key
            self.size += 1
            return

        elif self.table[index] != None and i < self.maxCollision:
            print("collision number {0} at {1}".format(i+1,index))
            return self.add(key,i+1)

        elif i >= self.maxCollision :
            return print("Max of collisionChain")
          

print(" ***** Fun with hashing *****")
inp = input('Enter Input : ').split('/')

inp[0] = list(map(int,inp[0].split(" ")))
inp[1] = inp[1].split(",")

for i in range(len(inp[1])):
    inp[1][i] = inp[1][i].split(" ")

MAXsize = inp[0][0]
Maxcollosion = inp[0][1]

h = hash(MAXsize,Maxcollosion)

for i in range(len(inp[1])):
    if h.size != MAXsize:
        h.add(Data(inp[1][i][0],inp[1][i][1]),0)
        for j in range(len(h.table)):
            print("#"+str(j+1)+"	"+h.table[j].__str__())
        print("---------------------------")
    else:
        break
print("This table is full !!!!!!")

# print(inp[0])
# print(inp[1])
