#min number of coins are required to make given sum
import sys;

coins=[1,2,3];
sum=20;

c=[None]*(sum+1);
c[0]=0;
for  i in range(1,sum+1,1):
    min_req=sys.maxsize;
    for j in coins:
        if((i-j)>=0):
            min_req=min(c[i-j],min_req);
    c[i]=min_req+1;

print(c[sum]);

    
