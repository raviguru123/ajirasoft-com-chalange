def max(a,b):
	if(a>b):
		return a;
	return b;
			
    			
def check(arr,n):
	if(n<0):
		return 0;
	if(n==0):
		return arr[0];
	if(n==1):
		max(arr[0],arr[1]);
    
	value=max(arr[n]+check(arr,n-2),arr[n-1]+check(arr,n-3));
	return value;


def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        n=int(input());
        arr=list(map(int,input().split()));
        output.append(check(arr,n-1));
        
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();