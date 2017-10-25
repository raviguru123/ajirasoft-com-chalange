import sys
def min_s(arr):
    min_value=sys.maxsize;
    for i in arr:
        if(i<min_value):
            min_value=i;
    return min_value;

def Knight_Walk(chess,row,col,s1,s2,d1,d2,count):
    if(s1>row or s2>col or s1<0 or s2<0):
        return sys.maxsize;
    
    if(s1==d1 and s2==d2):
        return count+1;
    
    if(chess[s1][s2]<sys.maxsize):
        if(chess[s1][s2]<=count+1):
            return sys.maxsize;#this is not the path.
        
    if(chess[s1][s2]>count+1):
        chess[s1][s2]=count+1;
        arr=[];
        for i in range(8):
            arr.append(sys.maxsize);  

        arr[0]=Knight_Walk(chess,row,col,s1-2,s2+1,d1,d2,count+1);
        arr[1]=Knight_Walk(chess,row,col,s1-2,s2-1,d1,d2,count+1);
        
        arr[2]=Knight_Walk(chess,row,col,s1+2,s2-1,d1,d2,count+1);
        arr[3]=Knight_Walk(chess,row,col,s1+2,s2+1,d1,d2,count+1);
        
        arr[4]=Knight_Walk(chess,row,col,s1-1,s2+2,d1,d2,count+1);
        arr[5]=Knight_Walk(chess,row,col,s1+1,s2+2,d1,d2,count+1);
        
        arr[6]=Knight_Walk(chess,row,col,s1-1,s2-2,d1,d2,count+1);
        arr[7]=Knight_Walk(chess,row,col,s1+1,s2-2,d1,d2,count+1);
        # print(arr);        
        return min_s(arr);
    

    


def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        arr1=list(map(int,input().split()));
        row=arr1[0];
        col=arr1[1];
        arr=list(map(int,input().split()));
        s1=arr[0];
        s2=arr[1];
        d1=arr[2];
        d2=arr[3];
        chess=[];
        for i in range(26):
            chess.append([sys.maxsize]*26);
        output.append((Knight_Walk(chess,row,col,s1,s2,d1,d2,0))-1);
        
        
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();