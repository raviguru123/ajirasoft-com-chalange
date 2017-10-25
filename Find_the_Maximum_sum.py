mod = 10**9 + 7
cases = int(input())
for t in range(cases):
    n = int(input())
    arr = list(map(int,input().split()))
    pos,neg = [],[]
    for i in arr:
        if i>=0: pos.append(i)
        else: neg.append(i)
    neg.sort()
    pos.sort(reverse=True)
    ans = 0
    for i in range(0,len(neg)-1,2):
        ans += neg[i]*neg[i+1]
        
    for i in range(0,len(pos)-1,2):
        ans += pos[i]*pos[i+1]
        ans %= mod
        
    if len(pos)&1 and len(neg)&1:
        ans += pos[-1]*neg[-1]
        
    elif len(pos)&1: ans += pos[-1]
    elif len(neg)&1: ans += neg[-1]
    
    if ans>0: ans %= mod
    print(ans)