


def Non_Overlapping_SubArrays(list1,num):
    found=False;
    count=0;
    start_index=-1;
    for index,value in enumerate(list1):
        if(num==value):
            found=True;
            if(start_index==-1):
                start_index=index;

        elif(value<num and start_index==-1):
            start_index=index;
            
        elif(value>num):
           if(found==True):
                count+=index-start_index;
                start_index=index+1;
                found=False;
           else:
                start_index=-1;
        if(found==True and len(list1)-1==index):
            count+=index-start_index+1;
        # print('count=',count);
    return count;
def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=input();
        arr=list(map(int,input().split()));
        num=int(input());
        output.append(Non_Overlapping_SubArrays(arr,num));
        # print('<-------------------->');
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();