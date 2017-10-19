def decode_string(string):
    # print(string);
    if(len(string)==0):
        return "";
    if(('[' in string)==False):
        return string;
    if(ord(string[0])>47 and ord(string[0])<57):
        open_index=string.index('[');
        num=int(string[0:open_index]);
        length=len(string);
        new_str=decode_string(string[open_index+1:-1]);
        output=[];
        for i in range(num):
            output.append(new_str);
        return ''.join(output);
	  
    else:
        index=0;
        while( index<len(string) and ((ord(string[index])>=65 and ord(string[index])<=90) or (ord(string[index])>=97 and ord(string[index])<=122))):
            index+=1;
        if(index==len(string)):
            return string;
        else:
            new_str=string[0:index];
            return new_str+decode_string(string[index:]);
            
            



def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        str1=input();
        # print(len(str1));
        output.append(decode_string(str1));
        
        
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();