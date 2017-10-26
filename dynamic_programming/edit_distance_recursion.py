def edit_distance(str1,str2,n1,n2):
    if(n1<0):
        return n2;
    if(n2<0):
        return n1;
    if(str1[n1]==str2[n2]):
        return edit_distance(str1,str2,n1-1,n2-1);
    else:
        return 1+min(min(edit_distance(str1,str2,n1,n2-1),edit_distance(str1,str2,n1-1,n2)),edit_distance(str1,str2,n1-1,n2));


str1="satur";
str2="sun";

print(edit_distance(str1,str2,len(str1)-1,len(str2)-1));

