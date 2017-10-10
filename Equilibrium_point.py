#code
def Equilibrium_point(arr):
    if(len(arr)==1):
        return 1;
    elif(len(arr)==2):
        return -1;
    elif(len(arr)==3):
        if(arr[0]==arr[2]):
            return arr[1];
        else:
            return -1;
    else:
        first_index=0;
        last_index=len(arr)-1;
        last_sum=0;
        first_sum=0;
        first_sum+=arr[first_index];
        last_sum+=arr[last_index];
        
        while(first_index+1<last_index):
            #print(first_sum,last_sum,first_index,last_index);
            if(first_sum==last_sum and first_index+2==last_index):
                return first_index+2;
                
            elif(first_sum!=last_sum and first_index+2==last_index):
                return -1;
                
            elif(first_sum<last_sum):
                first_index+=1;
                first_sum+=arr[first_index];
                
            elif(first_sum>last_sum):
                last_index-=1;
                last_sum+=arr[last_index];
                
            else:
                first_index+=1;
                last_index-=1;
                first_sum+=arr[first_index];
                last_sum+=arr[last_index];
                
        return -1;
        
def main():
    output=[];
    testcase=int(input());
    for i in range(testcase):
        length=int(input());
        list1=list(map(int,input().split()));
        output.append(Equilibrium_point(list1));
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();