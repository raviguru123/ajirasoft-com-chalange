def sum(arr,first,last):
    total_sum=0;
    
    arr1=arr[first:last+1];
    for i in arr1:
        total_sum+=i;
    return total_sum;

def calculate_sum(arr,first,last,find):
    if(first>last):
        return -1;
    sum_value=sum(arr,first,last);
    if(sum_value!=find):
        found_size1=calculate_sum(arr,first+1,last,find);
        found_size2=calculate_sum(arr,first,last-1,find);
        if(found_size1!=-1 and found_size2!=-1):
            if(found_size1>found_size2):
                return found_size1;
            else:
                return found_size2;
        elif(found_size1!=-1):
            return found_size1;
        elif(found_size2!=-1):
            return found_size2;
        else:
            return -1;
        
    else:
        return last-first+1;

testcase=int(input());
output=[];
for i in range(testcase):
    size=int(input());
    arr=list(map(int,input().split()));
    output.append(calculate_sum(arr,0,len(arr)-1,0));

for i in output:
    print(i);


    

    