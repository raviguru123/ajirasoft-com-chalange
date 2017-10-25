# we have infinite supply of coin how many ways to make sum

def count(coins,sum,index):
    if(index<0 or sum<0):
        return 0;
    if(sum==0):
        return 1;

    return count(coins,sum-coins[index],index)+count(coins,sum,index-1);


coins=[1,2,3];
sum=4;

print(count(coins,sum,len(coins)-1));