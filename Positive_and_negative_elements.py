
def swap(list1,index,find_index):
    
    if(find_index>index):
        begin=index;
        last=find_index;
    else:
        begin=find_index;
        last=index;
    
    while(last>begin):
        temp=list1[last-1];
        list1[last-1]=list1[last];
        list1[last]=temp;
        last-=1;
    

def Positive_and_negative_elements(list1):
    find_index=0;
    set_sign=1;
    index=1;
    while(index<len(list1) and find_index<len(list1)):
        
        if(set_sign==1 and list1[find_index]>0):
            find_index+=1;
            if(index<find_index):
                index=find_index+1;    
            
            set_sign=-1;
            continue;
                
        elif(set_sign==-1 and list1[find_index]<0):
            find_index+=1;
            if(index<find_index):
                index=find_index+1;    
            set_sign=1;
            continue;
        
        if(set_sign==1 and list1[index]>0):
            swap(list1,index,find_index);
            find_index+=1;
            index+=1;
            set_sign=-1;
        elif(set_sign==-1 and list1[index]<0):
            swap(list1,index,find_index);
            find_index+=1;
            index+=1;
            set_sign=1;
        else:
            index+=1;
    return list1;        



def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=input();
        arr=list(map(int,input().split()));
        output.append(Positive_and_negative_elements(arr));
    
    print('----------------------');
    for arr in output:
        for i in arr:
            print(i,end=' ');
        print();


if(__name__=='__main__'):
    main();