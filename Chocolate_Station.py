
def Chocolate_Station(station_list):
    chocolate=station_list[0];
    for station in station_list:
        if(station>chocolate):
            chocolate=station;
    return chocolate;

def main():
    numtest=int(input());
    output=[];
    for i in range(numtest):
        sizea=input();
        stations=list(map(int,input().split()));
        price=int(input());
        output.append(Chocolate_Station(stations)*price);
        
    for i in output:
        print(i);


if(__name__=='__main__'):
    main();