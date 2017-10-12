def Subarray_with_given(list1,total_sum):
    first_index=0;
    last_index=0;
    req_sum=0;
    output=[];
    flag=False;
    for index,value in enumerate(list1):
        req_sum+=value;
        if(req_sum==total_sum):
            output.append(first_index+1);
            output.append(index+1);
            flag=True;
            break;
        if(req_sum>total_sum):
            while(req_sum>total_sum):
                req_sum-=list1[first_index];
                first_index+=1;
            if(req_sum==total_sum):
                output.append(first_index+1);
                output.append(index+1);
                flag=True;
                break;
    if(flag==False):
        output.append(-1);
    return output;           
        



def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=arr=list(map(int,input().split()));
        arr=list(map(int,input().split()));
        req_sum=sizea[1];
        output.append(Subarray_with_given(arr,req_sum));
    
    for o in output:
        for i in o:
            print(i,end=' ');
        print();
        


if(__name__=='__main__'):
    main();