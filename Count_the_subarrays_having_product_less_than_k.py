import sys

def Count_the_subarrays_having_product_less_than_k(arr,num):
    output=[];
    output1=[];
    count=0;
    for i,value in enumerate(arr):
        output=output1[:];
        for j in range(i,len(arr),1):
            if(i==0):
                output1.append(arr[j]);
                if(arr[j]<num):
                    count+=1;
            else:
                output1[j]=arr[j]*output[j-1];
                if(output1[j]<num):
                    count+=1;

            

    return count;

testcase=int(input());
output=[];
for i in range(testcase):
    # size=int(input());
    arr1=list(map(int,input().split()));
    arr=list(map(int,input().split()));
    output.append(Count_the_subarrays_having_product_less_than_k(arr,arr1[1]));

for i in output:
    print(i);