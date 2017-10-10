# function is use for find successfull attack
def find_successfull_attack(days):
    dict={};#this dictionary is use to track height of wall.
    dict['N']=0;
    dict['S']=0;
    dict['E']=0;
    dict['W']=0;
    #initially count of attack should be .
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

        for direction,force in dict2.items():
            if(dict[direction]<force):
                dict[direction]=force;
            
               
       
    return attackcount;



#main function in entry point of program;
def main():
    print("<-----------------start from here------------------->");
    days=[];
    for i in range(3):
        day=input();
        days.append(day);
  
    print('<--------------Output---------------->')
    print(find_successfull_attack(days));
    



#Check if this file is main file
if(__name__=='__main__'):
    main();







