prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

stocks ={
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15

}
for key in prices:
    print(key)
    print("price :",prices[key])
    print("stock :",stocks[key],)
    print('*'*14)

total = 0
for key , value in prices.items():

    print(prices[key]*stocks[key])

    total = total+(prices[key]*stocks[key])
print("Total money : ", total)