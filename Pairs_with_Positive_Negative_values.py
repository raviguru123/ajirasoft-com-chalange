def main():
    testcount=int(input());
    outputs=[];
    for i in range(testcount):
        dict={};
        sizecount=input();
        arr=list(map(int, input().split()))
        temp=[];
        for el in arr:
            el=abs(el);
            if(el in dict):
                dict[el]+=1;
            else:
                dict[el]=1;

        for el in sorted(dict.keys()):
            if(dict[el]>1):
                temp.append(el);
        outputs.append(list(temp));
    for output in outputs:
        for el in output:
            print(-1*el,el,end=' ');
        print();
           



if __name__=='__main__':
    main();