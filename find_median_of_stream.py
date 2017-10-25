# import heapq;
# import functools;

# class MinHeap:
#     def __init__(self):
#         self.h=[];
#     def push(self,x):
#         heapq.heappush(self.h,x);
#     def pop(self):
#         return heapq.heappop(self.h).val;
#     def __len__(self):
#         return len(self.h);

# def check(elem):
#     elem[0]=2;

# a=[20];
# check(a);
# print(a[0]);


# def myfunc(a,b):
#     if(a>b):
#         return 1;
#     return -1;
# arr=[10,3,5,6];
# arr.sort(key=functools.cmp_to_key(myfunc));
# arr=''.join(list(map(str,arr)));
# print(arr);

for i in range(1,10,1):
    print(i);