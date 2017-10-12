#code

def MyFn(a):
    return a[1];

def Maximum_Tip_Calculator(tip1,tip2,waiter1,waiter2):
    abs_tips=[];
    for index,value in enumerate(tip1):
        val=abs(tip1[index]-tip2[index]);
        abs_tips.append((index,val));
    abs_tips=sorted(abs_tips,key=MyFn,reverse=True);
    
    profit=0;
    # print(abs_tips);
    for profit_tup in abs_tips:
        if(tip1[profit_tup[0]]>tip2[profit_tup[0]] and waiter1>0):
            profit+=tip1[profit_tup[0]];
            waiter1-=1;
        elif(tip2[profit_tup[0]]>tip1[profit_tup[0]] and waiter2>0):
            profit+=tip2[profit_tup[0]];
            waiter2-=1;
        elif(waiter1>0):
            profit+=tip1[profit_tup[0]];
            waiter1-=1;
        else:
            profit+=tip2[profit_tup[0]];
            waiter2-=1;
        
        
    return profit;


def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=list(map(int,input().split()));
        waiter1=sizea[1];
        waiter2=sizea[2];
        tip1=list(map(int,input().split()));
        tip2=list(map(int,input().split()));
        output.append(Maximum_Tip_Calculator(tip1,tip2,waiter1,waiter2));
           
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();