def sorted(s):
    output=[];
    output.append(s.pop());
    while(len(s)>0):
        elem=s.pop();
        while(len(output)>0 and output[-1]>elem):
            s.append(output.pop());
        output.append(elem);
        

    for i in reversed(output):
        s.append(i);


arr=list(map(int,input().split()));
sorted(arr);
print(arr);
    