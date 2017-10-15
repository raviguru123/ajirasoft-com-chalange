import queue

def Jumping_numbers(num,x):
    q=queue.Queue();
    q.put(num);
    while(not q.empty()):
        num=q.get();
        if(num<x):
            print(num,end=' ');
            if(num%10==0):
                num=num*10+(num%10)+1;
                q.put(num);
            elif(num%10==9):
                num=num*10-(num%10)+1;
                q.put(num);
            else:
                num1=num*10+(num%10)-1;
                num2=num*10+(num%10)+1;
                q.put(num1);
                q.put(num2);

def main():
    num=int(input());
    print('num',num);
    print(0,end=' ');
    for i in range(1,10):
        Jumping_numbers(i,num);

if(__name__=='__main__'):
    main();