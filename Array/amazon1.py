def min_cost(arr,low,high,x,y,dict):
   min_value=float("inf");
   
   if((low,high) in dict):
       return dict.get((low,high));
   elif(low+1==high):
       return 0;
   elif(low+2==high):
       return x*(arr[low+1]-arr[low])+y*(arr[high]-arr[low+1]);

   else:
       for i in range(low+1,high,1):
           cost=x*(arr[i]-arr[low])+y*(arr[high]-arr[i]);
           value=cost+min_cost(arr,low,i,x,y,dict)+min_cost(arr,i,high,x,y,dict);
           min_value=min(min_value,value);
   dict[(low,high)]=min_value;
   return min_value;
        


test=int(input());
output=[];
for i in range(test):
    arr=list(map(int,input().split()));
    x=arr[0];
    y=arr[1];
    size=input();
    arr1=list(map(int,input().split()));
    dict={};
    output.append(min_cost(arr1,0,len(arr1)-1,x,y,dict));
    

for i in output:
    print(i);


