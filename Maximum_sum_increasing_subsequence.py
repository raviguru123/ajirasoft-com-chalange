#code
def Maximum_sum_increasing_subsequence(list1):
    if(len(list1)==0):
        return 0;
    sum_list=[];
    sum_list.append(list1[0]);
    for index,value in enumerate(list1[1:]):
        index+=1;
        sum_value=value;
        max=0;
        for i in range(index-1,-1,-1):
            if(list1[index]>list1[i] and max<sum_list[i]):
                max=sum_list[i];
               
        sum_value+=max;   
        sum_list.append(sum_value);  
    
    max=0;
    # print(sum_list);
    for i in sum_list:
        if(max<i):
            max=i;
    return max;
    
def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=input();
        arr=list(map(int,input().split()));
        output.append(Maximum_sum_increasing_subsequence(arr));
           
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();