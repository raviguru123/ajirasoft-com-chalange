def min(a,b):
    if(a<b):
        return a;
    return b;

def max(a,b):
    if(a>b):
        return a;
    return b;

def Maximum_Index(list1):
    left_min=[];
    left_min.append(list1[0]);
    
    right_max=[];
    right_max.append(list1[-1:][0]);
    for index,value in enumerate(list1[1:]):
        # print(index,value);
        left_min.append(min(left_min[index],value));
       
    list1.reverse();
    for index,value in enumerate(list1[1:]):
        right_max.append(max(right_max[index],value)); 
        
    right_max.reverse();
    
    
    i=0;j=0;
    max_value=-1;
    # print(left_min,right_max)
    
    while(i<len(left_min) and j<len(right_max)):
        
        if(max_value<j-i and  right_max[j]>=left_min[i]):
            max_value=j-i;
        
        if(left_min[i]<=right_max[j]):
            j+=1;
        else:
            i+=1;
        
    return max_value;


def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=input();
        arr=list(map(int,input().split()));
        output.append(Maximum_Index(arr));
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();