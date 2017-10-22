def memoize(arr,first1,last1,first2,last2):
    output=[];
    start=first1;
    end=last2;
    while(first1<=last1 and first2<=last2):
        if(arr[first1]>=arr[first2]):
            output.append(arr[first2]);
            first2+=1;
        else:
            output.append(arr[first1]);
            first1+=1;

    while(first1<=last1):
        output.append(arr[first1]);
        first1+=1;

    while(first2<=last2):
        output.append(arr[first2]);
        first2+=1;

    index=0;
    while(start<=end):
        arr[start]=output[index];
        start+=1;
        index+=1;



def check_swap(arr,first,last):
    if(arr[first]>arr[last]):
        temp=arr[first];
        arr[first]=arr[last];
        arr[last]=temp;

def merge(arr,first,last):
    if(first>=last):
        return;
    if(first+1==last):
        check_swap(arr,first,last);
        return;
    
    mid=int((first+last)/2);
    merge(arr,first,mid);
    merge(arr,mid+1,last);
    memoize(arr,first,mid,mid+1,last);







arr=[7,6,5,36,3,2,1];
merge(arr,0,len(arr)-1);
print(arr);