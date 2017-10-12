def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        arr=input().split(' ');
        found=False;
        for _char in arr[0]:
            if(_char in arr[1]):
                Found=True;
                break;
        if(Found==True):
            output.append(1);
        else:
            output.append(-1);

    for i in output:
        print(i);
             
        
    


if(__name__=='__main__'):
    main();