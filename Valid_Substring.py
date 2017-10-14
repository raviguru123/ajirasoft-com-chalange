def max(first,second):
    if(first>second):
        return first;
    return second;

def Valid_Substring(list1):
    max_count=0;
    count=0;
    output=[];
    for i in list1:
        if(i=='('):
            output.append(count);
            count=0;
        elif(i==')' and len(output)>0):
            count+=output.pop()+2;
            max_count=max(count,max_count);
        else:
            count=0;

    return max_count;      
            
def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        arr=list(input());
        output.append(Valid_Substring(arr));
        
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();