
def max_list(arr):
    max=0;
    for i in arr:
        if(max<i):
            max=i;
    return max;


def max(value1,value2):
    if(value1>value2):
        return value1;
    return value2;



def Longest_Increasing_Subsequence(arr):
    output=[];
    for i in range(len(arr)):
        output.append(1);
        
    for index,value in enumerate(arr):
        if(index==0):
            continue;
        index2=index-1;
        max_value=output[index];
        while(index2>=0):
            if(value>arr[index2]):
                max_value=max(max_value,output[index2]+1);
            index2-=1;

        output[index]=max_value;
    return max_list(output);
        

def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=input();
        arr=list(map(int,input().split()));
        output.append(Longest_Increasing_Subsequence(arr));
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();