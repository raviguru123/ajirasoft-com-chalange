def calculate_min_cost(cache,arr,start,n,shirt,pant,boot):
    min_first=float("inf");
    min_second=float("inf");
    min_third=float("inf");
    if((start,n,shirt,pant,boot) in cache):
        return cache.get((start,n,shirt,pant,boot));
    if(shirt==True and pant==True and boot==True):
        return 0;
    if(start>n):
        return float("inf");
    if(shirt==False):
        include=arr[start][0]+calculate_min_cost(cache,arr,start+1,n,True,pant,boot);
        exclude=calculate_min_cost(cache,arr,start+1,n,shirt,pant,boot);
        min_first=min(include,exclude);
        
    if(pant==False):
        include=arr[start][1]+calculate_min_cost(cache,arr,start+1,n,shirt,True,boot);
        exclude=calculate_min_cost(cache,arr,start+1,n,shirt,pant,boot);
        min_second=min(include,exclude);
    
    if(boot==False):
        include=arr[start][2]+calculate_min_cost(cache,arr,start+1,n,shirt,pant,True);
        exclude=calculate_min_cost(cache,arr,start+1,n,shirt,pant,boot);
        min_third=min(include,exclude);

    value=min(min(min_first,min_second),min_third);
    cache[(start,n,shirt,pant,boot)]=value;
    return value;

        








test_cases=int(input());
output=[];
for i in range(test_cases):
    shops=[];
    shops_count=int(input());
    for i in range(shops_count):
        arr=list(map(int,input().split()));
        shops.append(arr);
    cache={};
    output.append(calculate_min_cost(cache,shops,0,shops_count-1,False,False,False));

for i in output:
    print(i);  
        
    
