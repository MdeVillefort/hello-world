import time, random

items = [chr(i) for i in range(0x30a1, 0x30ff + 1)] #katakana

for i in range(1,11): #adds variable spaces and numbers 1-10 to items list
    items.append(str(i))
    items.append(" "*i)

def rain(row, column):
    for i in range(row): #for every row
        s = ''          #new string
        for j in range(column): #for every column (or character)
            ri = random.randrange(len(items)) #random index
            s += items[ri]
        
        print(s)
        time.sleep(0.2) #change this to whatever gives rain good speed

#main program call
while True:
	rain(50,50)