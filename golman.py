import functools


def myCmp(a,b):
  if int(str(a) + "" + str(b)) < int(str(b) + "" + str(a)):
    return 1
  else:
    return -1

def main():
    arr=list(map(int,input().split()));
    arr.sort(key = functools.cmp_to_key(myCmp))
    print(arr);


if(__name__=='__main__'):
    main();