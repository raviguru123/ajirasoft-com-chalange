# function is use for find successfull attack
def find_successfull_attack(days):
    dict={};#this dictionary is use to track height of wall.
    #ititially all side of wall length is zero.
    dict['N']=0;
    dict['S']=0;
    dict['E']=0;
    dict['W']=0;
    #initially count of attack should be zero.
    attackcount=0; 

    for day in days:#iterate days 
        attacks=((day.split(';')[1]).strip()).split(':');
        dict2={};#this dictionary is use for track single day force and direction.
        for attack in attacks:
            direction=(attack.split('-')[1]).strip();
            force=int((attack.split('-')[2]).strip());
            dict2[direction]=force;
            if(dict[direction]<force):
                attackcount+=1;

        for direction,force in dict2.items():# made wall after single day attack
            if(dict[direction]<force):
                dict[direction]=force;
            
               
       
    return attackcount;

# this function is use for unit test
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = ' WRONG OUTPUT'
    print ('%s   got: %s expected: %s' % (prefix, repr(got), repr(expected)));



#main function in entry point of program;
def main():
    print("<-----------------start from here------------------->");
    days=[];
    for i in range(3):
        day=input();
        days.append(day);
    print();
    Output=int(input('Enter Expected Output='));
    print();
    print('<--------------Unit Test Output---------------->')
    test(find_successfull_attack(days),Output);
    



#Check if this file is main file
if(__name__=='__main__'):
    main();







