# def check_balance(root):
#     if(!root):
#         return True;

#     left_hight=hight(root.left);
#     right_hight=hight(root.right);
#     if(abs(left_hight-right_hight)<=1 and check_balance(root.left) and check_balance(root.right)):
#         return True;

#     return False;




# def hight(root):
#     if(!root):
#         return 0;

#     return 1+max(root.left,root.right);

# dict={};
# dict[1]=2;
# dict[2]=3;
# if(3 in dict):
#     dict.pop(3);
# for i in len(dict.keys()):
#     print(i);

import functools


a=[1,2,3,4];
def myfunc(i,j):
    if(i<j):
        return 1;
    return -1;


a.sort(key=functools.cmp_to_key(myfunc));
print(a);