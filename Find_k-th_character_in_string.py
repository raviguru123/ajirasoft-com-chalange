get_bin=lambda x: format(x,'b');

def Findcharacte(m,k,n):
    binary_list=list(get_bin(m));
    # print(binary_list);
    while(n!=0):
        binary_list1=[];
        for i in binary_list:
            if(i=='0'):
                binary_list1.append('0');
                binary_list1.append('1');
            else:
                binary_list1.append('1');
                binary_list1.append('0');
        binary_list=binary_list1[:];
        # print(binary_list);
        n-=1;
    
    return binary_list[k];
        


def main():
    a = [1, 2, 4];
    a.insert(2, 3);
    output=[];
    test_count=int(input());
    for i in range(test_count):
        list1=list(map(int,input().split()));
        m=list1[0];
        k=list1[1];
        n=list1[2];
        output.append(Findcharacte(m,k,n));

    for i in output:
        print(i);


if(__name__=='__main__'):
    main();