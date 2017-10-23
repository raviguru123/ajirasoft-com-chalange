def spiral(a):
    if(isinstance(a[0],list)):
        row=len(a);
        col=len(a[0]);
    else:
        for i in a:
            print(i, end=' ');
        print();
        return;
        
    
    start_row=0;
    end_row=row-1;
    start_col=0;
    end_col=col-1;
    dr=0;
    while(start_row<=end_row and start_col<=end_col):
        if(dr==0):
            for i in range(start_col,end_col+1):
                print (a[start_row][i], end=" ")
            start_row+=1;
            dr=1;
        elif(dr==1):
            for i in range(start_row,end_row+1):
                print(a[i][end_col],end=" ");
            end_col-=1;
            dr=2;
        elif(dr==2):
            for i in range(end_col,start_col-1,-1):
                print(a[end_row][i],end=" ");
            end_row-=1;
            dr=3;
        else:
            for i in range(end_row,start_row-1,-1):
                print(a[i][start_col],end=" ");
            start_col+=1;
            dr=0;
        print();
    print();
    print();
a = [1,2,3,4]
     
#Calling Function
spiral(a)