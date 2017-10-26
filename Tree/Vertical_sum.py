import tree

dict={};

def vertical_sum(root,distance):
    if(not root):
        return;

    if(distance in dict):
        dict[distance]+=root.data;
    else:
        dict[distance]=root.data;
    vertical_sum(root.left,distance-1);
    vertical_sum(root.right,distance+1);

bst=tree.Tree();
bst.root=tree.node(5);
bst.root.left=tree.node(2);
bst.root.right=tree.node(3);
bst.root.left.left=tree.node(1);
bst.root.left.right=tree.node(7);
bst.root.right.left=tree.node(6);

vertical_sum(bst.root,0);
for k in sorted(dict.keys()):
    print(dict[k],end=' ');

print();

