
coin = open("coins2.in")
string = coin.read(10);
coin.close()

list0 = string.split(" ")
list = [int(s) for s in list0]

list.remove(list[0])

largest1 = max(list)

list.remove(largest1)
largest2 = max(list)

list.remove(largest2)
largest3 = max(list)

smallest = 1

list1 = string.split(" ")
list = [int(s) for s in list1]
money = list[0]

#smallest coin using largest
aa = 0
while aa*largest1 <= money:
    aa+=1
money = money - ((aa-1)*largest1)

bb = 0
while bb*largest2 <= money:
    bb+=1
money = money - ((bb-1)*largest2)

cc = 0
while cc*largest3 <= money:
    cc+=1
money = money - ((cc-1)*largest3)

dd = 0
while dd*smallest <= money:
    dd+=1
money = money - ((dd-1)*smallest)

fewest_coin = aa+bb+cc+dd-4

#smallest coin using second largest
money = list[0]
aa = 0
while aa*largest2 <= money:
    aa+=1
money = money - ((aa-1)*largest2)

bb = 0
while bb*largest3 <= money:
    bb+=1
money = money - ((bb-1)*largest3)

cc = 0
while cc*smallest <= money:
    cc+=1
money = money - ((cc-1)*smallest)

temp = aa+bb+cc-3
if temp < fewest_coin:
    fewest_coin = temp

#smallest coin using third largest
money = list[0]
aa = 0
while aa*largest3 <= money:
    aa+=1
money = money - ((aa-1)*largest3)

bb = 0
while bb*smallest <= money:
    bb+=1
money = money - ((bb-1)*smallest)


temp = aa+bb-2
if temp < fewest_coin:
    fewest_coin = temp


coin1 = open("coins2.out","w+")
coin1.write(str(fewest_coin))
coin1.close
