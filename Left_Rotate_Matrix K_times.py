
def swap(list1,index1,index2):
    temp=list1[index1];
    list1[index1]=list1[index2];
    list1[index2]=temp;

def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        arr1=list(map(int,input().split()));
        rows=arr1[0];
        columns=arr1[1];
        iteration=arr1[2];
        iteration=iteration%columns;
        print('iteration',iteration);
        arr=list(map(int,input().split()));
        
        for row in range(rows):
            temp_iteration=iteration;
            
            while(temp_iteration>0):
                start_index=row*columns;
                end_index=start_index+columns;
                while(start_index<end_index-1):
                    swap(arr,start_index,start_index+1);
                    start_index+=1;
                temp_iteration-=1;
        output.append(arr);    
        
    for el in output:
        for i in el:
            print(i,end=' ');
        print();


if(__name__=='__main__'):
    main();