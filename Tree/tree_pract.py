class tree:
    def __init__(self,data):
        self.data=data;
        self.right=None;
        self.left=None;
    def inorder(self):
        
        if(self.left):
            self.left.inorder();
        print(self.data,end=' ');
        if(self.right):
            self.right.inorder();
        

bt=tree(8);
bt.left=tree(18);
bt.left.left=tree(118);
bt.right=tree(12);
bt.right.right=tree(80);

bt.inorder();
print();