def Column_name(num):
    letters=[];
    output=[];
    for i in range(26):
        letters.append(chr(65+i));
    while(num!=0):
        rem=num%26;
        output.append(letters[rem-1]);
        num-=1;
        num=int(num/26);
        
    output.reverse();
    return ''.join(output);



num=int(input());
for i in range(1,num+1,1):
    print(i,Column_name(i));    
