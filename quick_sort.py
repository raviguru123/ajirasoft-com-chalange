def swap(arr,index1,index2):
    temp=arr[index1];
    arr[index1]=arr[index2];
    arr[index2]=temp;

def partition(arr,low,high):
    i=low-1;
    pivot=arr[high];
    for j in range(low,high,1):
        if(arr[j]<pivot):
            i+=1;
            swap(arr,i,j);
    
    swap(arr,i+1,high);
    return i+1;


def quick_sort(arr,low,high):
    if(low<high):
        piv=partition(arr,low,high);
        quick_sort(arr,low,piv-1);
        quick_sort(arr,piv+1,high);


a=[10,6,7,8,9,1];
quick_sort(a,0,len(a)-1);
print(a);

