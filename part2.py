
coin = open("coins.in")
coin2 = coin.read(10);
coin.close()

money = float(coin2)*100

quarter = 25
dime = 10
nickel = 5
penny = 1
aa = 0
bb = 0
cc = 0
dd = 0

while aa*quarter <= money:
    aa+=1
money = money - ((aa-1)*25)


while bb*dime <= money:
    bb+=1
money = money - ((bb-1)*10)


while cc*nickel <= money:
    cc+=1
money = money - ((cc-1)*5)


while dd*penny <= money:
    dd+=1

total = str(aa+bb+cc+dd-4)

coin3 = open("coins.out","w+")
coin3.write(total)
coin3.close
