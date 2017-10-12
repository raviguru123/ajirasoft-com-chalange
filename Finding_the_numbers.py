
def Finding_the_numbers(list1):
    xor=0;
    output=[];
    for i in list1:
        xor=xor^i;
    pos=0;
    num=1;
    while(num & xor==0):
        num=num<<1;
    first_set=[];
    second_set=[];
    
    for i in list1:
        if(num & i==0):
            first_set.append(i);
    # print('num',num);

    for i in list1:
        
        if(num & i!=0):
            second_set.append(i);
    num1=0;
    num2=0;
    
    # print('first_set',first_set);
    # print('second_set',second_set);

    for i in second_set:
        num1=num1^i;
        
    for i in first_set:
        num2=num2^i;
    
    # for i in list1:
    #     if(i==num1):
    #         output.append(num1);
    #         output.append(num2);
    #         break;
    #     elif(i==num2):
    #         output.append(num2);
    #         output.append(num1);
    #         break;
    if(num1>num2):
        output.append(num2);
        output.append(num1);
    else:
        output.append(num1);
        output.append(num2);
        
    
    
    return output;

def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=input();
        arr=list(map(int,input().split()));
        output.append(Finding_the_numbers(arr));
    for out in output:
            for i in out:
                print(i,end=' ');
            print();        
        


if(__name__=='__main__'):
    main();