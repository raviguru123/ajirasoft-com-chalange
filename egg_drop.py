import sys;
def max(a,b):
    if(a>b):
        return a;
    return b;


def Egg_Dropping_Puzzle(n,k):
    if(k == 1 or k == 0 or n==1):
        return k;
    
    min_value=sys.maxsize;
    for x in range(1,k+1,1):
        res=1+max(Egg_Dropping_Puzzle(n-1,x-1),Egg_Dropping_Puzzle(n,k-x));
        if(res<min_value):
            min_value=res;
    return min_value;


def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        arr=list(map(int,input().split()));
        output.append(Egg_Dropping_Puzzle(arr[0],arr[1]));
        
    
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();