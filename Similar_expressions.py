
def first(list1,index1,index2,sign):
    while(index1<index2 and sign=='-'):
        # print('index1<index2',index1,index2);
        if(list1[index1]=='-'):
            list1[index1]='+';
        elif(list1[index1]=='+'):
            list1[index1]='-';
        index1+=1;


def find_and_replace(list1,index1,index2,sign):
    # print('before',list1,index1,index2,sign);
    temp_index1=index1;
    temp_index2=index2;
    while(index1<index2 and sign=='-'):
        # print('index1<index2',index1,index2);
        if(list1[index1]=='-'):
            list1[index1]='+';
        elif(list1[index1]=='+'):
            list1[index1]='-';
        index1+=1;

    list1.pop(temp_index1);
    list1.pop(temp_index2-1);
    # print('after',list1);

def Similar_expressions(arr1,arr2):
    countlist=[];
    countlist.append(arr1);
    countlist.append(arr2);
    first(arr1,0,len(arr1)-1,arr1[0]);
    first(arr2,0,len(arr2)-1,arr2[0]);
    for i in range(2):
        list1=countlist[i];
        temp=0;
        while(temp<10):
            temp+=1;
            index1=-1;
            index2=-1;
            if('(' in list1):
                index1=list1.index('(');
            else:
                break;

            if(')' in list1):    
                index2=list1.index(')');
            else:
                break;
            
            if(index2>0 and index1>=0):
                find_and_replace(list1,index1,index2,list1[index1-1]);
                # find_and_replace(list1,index1,index2,'+','-');
            # print("index1,index2",index1,index2,list1);
        countlist[i]=list1;   
    print();
    print(countlist[0]);
    print(countlist[1]);
           
    if(countlist[0]==countlist[1]):
        return 'YES';
        
    return 'NO';



def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        arr1=list(input());
        arr2=list(input());
        output.append(Similar_expressions(arr1,arr2));
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();