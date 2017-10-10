#code

def max_sum(arr):
    max=-999999;
    sum=0;
    for elem in arr:
        sum=sum+int(elem);
        if(max<sum):
            max=sum;
        if(sum<0):
            sum=0;
    return max;


def main():
    arr=[];
    for index,val in enumerate(arr):
        print(index,val);




if __name__=='__main__':
    main();