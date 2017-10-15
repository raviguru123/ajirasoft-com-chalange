
def Count_Possible_Decodings(arr):
    if(arr[0]=='0'):
        return 0;
    output=[];
    for i in range(len(arr)+1):
        output.append(0);
    output[0]=1;
    output[1]=1;

    for index in range(len(arr)-1):
        index+=2;
        if(arr[index-1]>'0'):
            output[index]=output[index-1];
        if(arr[index-2]=='1' or (arr[index-2]=='2' and arr[index-1]<'7')):
            output[index]+=output[index-2];
    return output[-1:][0];


def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=input();
        arr=list(input());
        output.append(Count_Possible_Decodings(arr));
        
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();