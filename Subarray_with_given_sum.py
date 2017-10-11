#code
import types;

def main():
    output={};
    numtest=int(input());
    for i in range(numtest):
        sizenm=[];
        sizenm=list(map(int, input().split()))
        sumcount=sizenm[1];
        arr=[];
        arr=list(map(int, input().split()))
        start_index=0;
        end_index=0;
        sum=0;
        found=0;
        for index,val in enumerate(arr):
            sum=sum+val;
            if(sum>sumcount):
                while(sum>sumcount and start_index<=end_index):
                    sum=sum-arr[start_index];
                    start_index+=1;
                    if(start_index>end_index):
                        end_index+=1;

                    
            if(sum==sumcount):
                end_index=index;
                found=1;
                break;
        if(found==1):
            output[i]=(start_index+1,end_index+1);
        else:
            output[i]=-1;
        
        
    for i in output.keys():
            if(type(output[i])==type(())):
                print(output[i][0],output[i][1]);
            else:
                print(output[i]);



if __name__=='__main__':
    main();