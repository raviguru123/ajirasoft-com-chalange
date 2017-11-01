import math

dict={};
def nCr(n,r):
    f = math.factorial
    first=1;
    second=1;
    third=1;
    
    if(n in dict):
       first=dict[n];
    else:
        dict[n]=(f(n))%1000000007;
        first=dict[n];
        
    if((n-r) in dict):
       second=dict[n-r];
    else:
        dict[n-r]=(f(n-r))%1000000007;
        second=dict[n-r];
    
    if(r in dict):
       third=dict[n-r];
    else:
        dict[r]=(f(r))%1000000007;
        third=dict[r];
        
    return (first/second)/third; 
    
    

def Count_possible_ways_to_construct_buildings(num):
    possible_count=0;
    for i in range(1,num-1):
        possible_count=(possible_count+nCr(num,i))%1000000007;
    if(num%2==0):
        possible_count+=3;
    else:
        possible_count+=2;
    return (int(possible_count*possible_count))%1000000007;
    




def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        num=int(input());
        output.append(Count_possible_ways_to_construct_buildings(num));
    
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();