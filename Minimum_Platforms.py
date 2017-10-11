import bisect;
import re;

def Minimum_Platforms(ar_dp_time):
    plateforms=[];
    max_train_count=0;
    for train in ar_dp_time:
        bisect.insort(plateforms,train[1]);
        stay_count=0;
        index=0;
        for dep_time in plateforms:
            if(train[0]<dep_time):
                stay_count=len(plateforms)-index;
            else:
                index+=1;
        if(max_train_count<stay_count):
            max_train_count=stay_count;
    return max_train_count;



def MyFn(a):
    return a[0]

def main():
    test_case_count=int(input());
    output=[];
    for i in range(test_case_count):
        size=int(input());
        arrivel_time=list(map(int,input().split()));
        departure_time=list(map(int,input().split()));
        arr='A'*len(arrivel_time);
        dep='D'*len(departure_time);

        arrivel_time=list(zip(arrivel_time,arr));
        departure_time=list(zip(departure_time,dep));
        times=arrivel_time+departure_time;
        times=sorted(times,key=MyFn);
        max=0;
        count=0;
        # print(times);
        for time in times:
            if(time[1]=='A'):
                count+=1;
            else:
                count-=1;
            if(max<count):
                max=count;

        print(max);
        # output.append(Minimum_Platforms(ar_dp_time));

   

if __name__=='__main__':
    main();