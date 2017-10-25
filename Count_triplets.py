def Count_triplets(arr,k):
    arr.sort();
    length=len(arr);
    count=0;
    i=0;
    while(i<length-2):
        first=i+1;
        last=length-1;
        while(first<last):
            if(arr[i]+arr[first]+arr[last]<k):
                count+=last-first;
                first+=1;
            elif(arr[i]+arr[first]+arr[last]>=k):
                last-=1;
        i+=1;
    return count;



def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        arr1=list(map(int,input().split()));
        arr=list(map(int,input().split()));
        output.append(Count_triplets(arr,arr1[1]));
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();