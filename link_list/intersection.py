/*
Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function would be added by GfG's Online Judge.*/


/* The structure of the Linked list Node is as follows:
struct Node {
    int val;
    struct Node* next;
}; */
void intersection(Node **head1, Node **head2,Node **head3)
{
    // Your Code Here
    if(!(*head1) and !(*head2)){
        *head3=null;
        return;
    }
    
    while(*head1 && *head2){
        if((*head1)->data==(*head2)->data){
            temp=new Node();
            temp->data=(*head1)->data;
            temp->next=*head3;
            *head3=temp;
            
            *head1=(*head1)->next;
            *head2=(*head2)->next;
        }
        
        else if(*head1->data>*head2->data){
            *head2=(*head2)->next;
        }
        else{
            *head1=(*head1)->next;
        }
    }
}