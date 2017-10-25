'''Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.'''


"""  Pairwise swap the elements in a linked list.
  The input list will have at least one element
  Return reference to head of rotated linked list
  Node is defined as
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""
def pairWiseSwap(head):
    if(not head.next):
        return head;
    head1=head;
    head2=head.next;
    while(head2):
        data=head2.data;
        head2.data=head1.data;
        head1.data=data;
        head1=head1.next;
        if(head2.next):
            head2=head2.next;
            head1=head1.next;
        head2=head2.next;
    # code here
