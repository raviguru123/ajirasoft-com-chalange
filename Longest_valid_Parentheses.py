
def Longest_valid_Parentheses(arr):
    open=0;
    close=0;
    list1=[];
    count=0;
    max=0;
    for i in arr:
        if(i=='('):
            list1.append(i);
            open+=1;
        else:
            close+=1;
            
        if(i == ')' and len(list1)>0 and list1[len(list1)-1]=='('):
            count+=2;
            list1.pop();
        elif(i==')'):
            open=0;
            close=0;
            list1=[];
        if(max<count):
            max=count;
    return max;



def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        arr=input();
        arr=list(arr);
        output.append(Longest_valid_Parentheses(arr))
        
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();