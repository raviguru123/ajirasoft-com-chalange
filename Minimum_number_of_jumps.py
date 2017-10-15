import math

def min(num1,num2):
    if(num1<num2):
        return num1;
    return num2;

def Minimum_number_jumps(arr):
    jumps=[];
    jumps.append(0);
    
    for i in range(1,len(arr)):
        jumps.append(math.inf);
    
    for index,num in enumerate(arr):
        index1=index+1;
        while(num>0 and index1<len(jumps)):
            jumps[index1]=min(jumps[index1],jumps[index]+1);
            num-=1;
            index1+=1;
            
            
    return jumps[-1:][0];

def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=input();
        arr=list(map(int,input().split()));
        output.append(Minimum_number_jumps(arr));
    
    for i in output:
        if(i==math.inf):
            print(-1);
        else:
            print(i);


if(__name__=='__main__'):
    main();