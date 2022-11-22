class hash:
    def __init__(self,maxSize,maxCollision):
        self.table = [None] * maxSize
        self.size = 0
        self.maxSize = maxSize
        self.maxCollision = maxCollision
        self.threshold = 0
        self.percent = 0

    def getthreshold(self,num):
        self.threshold = num

    def getpercent(self,num):
        self.percent = num

    def add(self,key,lst,i=0,):

        index = (key + (i*i)) % self.maxSize
        # print(self.threshold)
        if (self.table[index] == None) and (i < self.maxCollision) and (self.size < self.threshold):
            self.table[index] = key
            self.size += 1
            return

        elif self.table[index] != None and i < self.maxCollision:
            print("collision number {0} at {1}".format(i+1,index))
            self.add(key,lst,i+1)
            return

        elif i >= self.maxCollision :
            print("****** Max collision - Rehash !!! ******")
            self.size = 0
            self.rehashing(lst)
            # print(self.table)
            self.getthreshold(self.percenmaxsize(self.percent))
            self.add(key,lst)
            return
        
        elif self.size >= self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.size = 0
            self.rehashing(lst)
            # print(self.table)
            self.getthreshold(self.percenmaxsize(self.percent))
            self.add(key,lst)
            return

    def add2(self,key,i=0):
        index = (key + (i*i)) % self.maxSize
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
            return self.add2(key,i+1)
        elif i >= self.maxCollision :
            return 

    def percenmaxsize(self ,num):
        (result) = (self.maxSize) * (num/100)
        return int(result)

    def primntinit(self):
        print("Initial Table :")
        for i in range(len(self.table)):
            print("#"+str(i+1)+"	"+str(self.table[i]))

    def printhash(self):
        for i in range(len(self.table)):
            print("#"+str(i+1)+"	"+str(self.table[i]))

    def rehashing(self,lst):
        temp = self.maxSize
        temp = toprime(temp*2)
        self.maxSize = temp
        self.table = [None] * temp

        for i in range(len(lst)):
            self.add2(int(lst[i]))
        # print(self.table)


def checkPrime(num):
    if num < 1:
        return False
    else:
        for i in range(2,num):
            if num % i == 0:
                return False
        else:
            return True

def toprime(num):
    if checkPrime(num) == False:
        num += 1
        return toprime(num)
    else:
        return num


print(" ***** Rehashing *****")
inp = input("Enter Input : ").split("/")

inp[0] = inp[0].split(" ")
inp[1] = inp[1].split(" ")

h = hash(int(inp[0][0]),int(inp[0][1]))
h.getthreshold(h.percenmaxsize(int(inp[0][2])))

h.getpercent(int(inp[0][2]))

h.primntinit()
print("----------------------------------------")
lst= []
for i in range(len(inp[1])):
    print("Add : "+inp[1][i])
    h.add(int(inp[1][i]),lst)
    h.printhash()
    lst.append(inp[1][i])
    # print(lst)
    print("----------------------------------------")

# print(6%47)