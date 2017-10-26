import functools;

def my_function(a,b):
    if((str(a)+" "+str(b))<(str(b)+" "+str(a))):
        return 1;
    return -1;

a=[12,9,10];
a.sort(key=functools.cmp_to_key(my_function));
print(a);
