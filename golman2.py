def subset_sum(arr,index,sum):
    if(sum==0):
        return True;
    if(index==0 and sum!=0):
        return False;
    if(arr[index]>sum):
        subset_sum(arr,index-1,sum);
    
    return subset_sum(arr,index-1,sum) or subset_sum(arr,index-1,sum-arr[index])


def main():
    arr=list(map(int,input().split()));
    sum=int(input());
    print(subset_sum(arr,len(arr)-1,sum));
    


if(__name__=='__main__'):
    main();