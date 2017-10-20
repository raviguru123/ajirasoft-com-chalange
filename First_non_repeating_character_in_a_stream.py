def First_non_repeating_character_in_a_stream(arr):
    frequency={};
    queue=[];
    output=[];
    
    for i in arr:
        if(i in frequency):
            frequency[i]=frequency[i]+1;
        else:
            frequency[i]=1;
        
        queue.append(i);
        repeat=-1
        while(len(queue)>0 and frequency[queue[0]]>1):
            queue.pop(0);
        if(len(queue)>0):
            repeat=queue[0];
        output.append(repeat);
            
        
    
    
    
    return output;
    
    


def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=input();
        arr=list(input().split());
        output.append(First_non_repeating_character_in_a_stream(arr));
    
    for i in output:
        for j in i:
            print(j,end=' ');
        print();


if(__name__=='__main__'):
    main();