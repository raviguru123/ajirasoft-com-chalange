#code

def Leaders_in_an_array(list1):
    length=len(list1)-1;
    max=-9999;
    leaders=[];
    
    while(length>=0):
        if(max<list1[length]):
            max=list1[length];
            leaders.append(max);
        length-=1;
    return reversed(leaders);
        
def main():
    numtest=int(input());
    output={};
    for i in range(numtest):
        sizea=input();
        arr=list(map(int,input().split()));
        output[i]=Leaders_in_an_array(arr);
           
    for leaders in output.keys():
        for leader in output[leaders]:
            print(leader,end=' ');
        print();


if(__name__=='__main__'):
    main();