def Ugly_Numbers(count):
    ugly_numbers=[];
    index_2=0;
    index_3=0;
    index_5=0;

    ugly_numbers.append(1);
    next_ugly_number_2=ugly_numbers[index_2]*2;
    next_ugly_number_3=ugly_numbers[index_3]*3;
    next_ugly_number_5=ugly_numbers[index_5]*5;

    for i in range(1,count):
        next_ugly_number=min(next_ugly_number_2,next_ugly_number_3,next_ugly_number_5);
        ugly_numbers.append(next_ugly_number);

        if(next_ugly_number==next_ugly_number_2):
            index_2+=1;
            next_ugly_number_2=ugly_numbers[index_2]*2;

        if(next_ugly_number==next_ugly_number_3):
            index_3+=1;
            next_ugly_number_3=ugly_numbers[index_3]*3;

        if(next_ugly_number==next_ugly_number_5):
            index_5+=1;
            next_ugly_number_5=ugly_numbers[index_5]*5;
    print(ugly_numbers);
    return ugly_numbers[-1];
    
    
def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        num=int(input());
        output.append(Ugly_Numbers(num));
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();