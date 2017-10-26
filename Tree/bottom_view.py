import tree

dict={};
def bottom_view(root,distance):
    if(not root):
        return;
    if(distance==0):
        dict[0]=root.data;
    if(not root.left and not root.right):
        dict[distance]=root.data;
        return;

    bottom_view(root.left,distance-1);
    bottom_view(root.right,distance+1);
    
node=tree.node;
bt=tree.Tree();
bt=bt.root;
bt=node(20);
bt.left=node(8);
bt.left.left=node(5);
bt.left.right=node(3);
bt.left.right.left=node(10);
bt.left.right.right=node(14);
bt.right=node(22);
bt.right.left=node(4);
bt.right.right=node(25);
bottom_view(bt,0);
for key in sorted(dict.keys()):
    print(dict[key],end=' ');

print();