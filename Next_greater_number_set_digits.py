def swap(arr,index1,index2):
    temp=arr[index1];
    arr[index1]=arr[index2];
    arr[index2]=temp;
    
def Next_greater_number_set_digits(arr):
    found=False;
    index1=-1;
    index2=-1;
    num=arr[len(arr)-1];
    
    for j in range(len(arr)-2,-1,-1):
        if(ord(arr[j])<ord(num)):
            index2=j;
            found=True;
            break;
        else:
            num=arr[j];
            
    if(found==False):
        return 'not possible';
    min_num=None;
    
    
    for index in range(index2+1,len(arr),1):
        value=arr[index];
        if(min_num==None):
            min_num=value;
            index1=index;
        elif(min_num>value and value>arr[index2]):
            min_num=value;
            index1=index;
            
    swap(arr,index1,index2);
    return ''.join(arr[0:index2+1]+sorted(arr[index2+1:]));
        



def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        num=list(input());
        output.append(Next_greater_number_set_digits(num));
        
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();