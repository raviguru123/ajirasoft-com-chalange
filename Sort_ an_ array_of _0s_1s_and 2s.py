#code

def sort_zeros_ones_twos(list):
    zero_count=0;
    one_count=0;
    two_count=0;
    output=[];
    for i in list:
        if(i==0):
            zero_count+=1;
        if(i==1):
            one_count+=1;
        if(i==2):
            two_count+=1;
    for i in range(zero_count+one_count+two_count):
        if(zero_count>0):
            zero_count-=1;
            output.append(0);
        elif(one_count>0):
            one_count-=1;
            output.append(1);
        else:
            two_count-=1;
            output.append(2);
    return output;
    
def main():
    dict={};
    test=int(input());
    for i in range(test):
        list1=[];
        length=input();
        list1=list(map(int,input().split()));
        dict[i]=sort_zeros_ones_twos(list1);
    
    for i in dict.keys():
        for j in dict[i]:
            print(j,end=' ');
        print();

if(__name__=='__main__'):
    main();
            


sudo add-apt-repository "deb http://archive.canonical.com/ $(lsb_release -sc) partner"
sudo dpkg --add-architecture i386
sudo apt-get update
sudo apt-get install skype