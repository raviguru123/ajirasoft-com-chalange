class node:
    def __init__(self,data):
        self.data=data;
        self.left=None;
        self.right=None;


    def insert(self,data):
        if(self.data>data):
            if(self.left):
                self.left.insert(data);
            else:
                self.left=node(data);
        else:
            if(self.right):
                self.right.insert(data);
            else:
                self.right=node(data);

    def inoder(self):
        if(self.left):
            self.left.inoder();
        print(self.data,end=' ');
        if(self.right):
            self.right.inoder();       
            
    def preorder(self):
        print(self.data,end=' ');
        if(self.left):
            self.left.preorder();
        if(self.right):
            self.right.preorder();
    def postorder(self):
        if(self.left):
            self.left.postorder();
        if(self.right):
            self.right.postorder();
        print(self.data,end=' ');
    def isSumTree(root):
        if(not root):
            return 0;
        if(not root.left and not root.right):
            return root.data;
        
        return root.data==isSumTree(root.left)+isSumTree(root.right);

class Tree:
    def __init__(self):
        self.root=None;
    def insert(self,data):
        if(self.root):
            self.root.insert(data);
        else:
            self.root=node(data);

    def inorder(self):
        print("<----------inorder traversal start------------>");
        self.root.inoder();
        print();
        print('-----------------------------------------------');
    def preorder(self):
        print('<----------preorder traversal start------------>');
        self.root.preorder();
        print();
        print('-----------------------------------------------');
    def postorder(self):
        print('<----------postorder traversal start------------>');
        self.root.postorder();
        print();
        print('-----------------------------------------------');
