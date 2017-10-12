
def Star_elements(list1):
    list2=[];
    max=-999999;
    superstars=0;
    for i in reversed(list1):
        if(max<i):
            list2.insert(0,i);
            max=i;
            superstars=max;
        elif(superstars==i):
            superstars=-1;

    list2.insert(0,superstars);
    # print('list=',list2);
    return list2;


def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=input();
        arr=list(map(int,input().split()));
        output.append(Star_elements(arr));
        
    for stars in output:
        for star in stars[1:]:
            print(star,end=' ');
        print();
        print(stars[0]);


if(__name__=='__main__'):
    main();