
Data = [5,2,10]
def maxProfit(price,start,end):
    if (end <= start):
        return 0
    profit = 0

    for i in range(start, end, 1):
        for j in range(i+1, end+1):
            if (price[j] > price[i]):
                curr_profit = price[j] - price[i] +maxProfit(price,start, i - 1)+maxProfit(price,j + 1, end)
                profit = max(profit, curr_profit)
 
    return profit

start = 0
end=len(Data)-1
result=maxProfit(Data,start,end)
print(result)