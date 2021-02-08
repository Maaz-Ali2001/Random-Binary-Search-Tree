import random

class Node:
    def __init__(self,value): # nodes of a graph
        self.value=value
        self.left=None
        self.right=None

class RBST:
    def __init__(self):
        self.root=None   # root of the graph
        self.S=None   # For insertion, it's the left subtree of the node which random chose.
        self.G=None   # For insertion , it's the right subtree of the node which random chose.
        self.Aux=None # used for deletion, final tree in it.

    def Size(self):
        return self.__Size(self.root)  # size of the graph

    def __Size(self,node):
        if node is None:
            return 0
        else:
            a= (self.__Size(node.left) +1+ self.__Size(node.right))
            return a

    def Insert(self,item):
        self.S=None   # initialize to it to none if not none
        self.G=None   # initialize to it to none if not none
        self.root= self.__Insert(item,self.root)


    def __Insert(self,x,T):
        if (random.randint(0,self.__Size(T)))== 0: # randomly chose on which level to insert
            return self.__Insert_at_root(x,T)
        if x < T.value:
            T.left= self.__Insert(x,T.left)
        else:
            T.right= self.__Insert(x,T.right)

        return T

    def __Insert_at_root(self,x,T): # inserting at the level which is picked randomly
        self.__split(x,T,self.S,self.G)   # spliting the left and right subtree of the node
        T=Node(x)                        # creating new node to insert
        T.left=self.S                   # add left subtree to the newnode
        T.right=self.G                  # add right subtree to the newnode
        return T

    def __split(self,x,t,s,g):
        if t==None:
            return #S,G
        if x<t.value:
            g=t
            l=t.left
            if l and x>l.value:
                self.__split(x, t.left, s, g.left)
                self.G=g
                self.G.left=None
            else:
                g.left=self.__split(x,t.left,s,g.left)
                self.G = g
            return g

        else:
            s=t
            f=t.right
            if f and x<f.value:
                self.__split(x,t.right,s.right,g)
                self.S=s
                self.S.right=None
            else:
                s.right=self.__split(x,t.right,s.right,g)
                self.S = s

            return s
        return

    def Delete(self,value):
        self.Aux=None
        self.root= self.__Delete(value,self.root)

    def __Delete(self,x,T):
        if T==None:
            return
        if x<T.value:
            T.left=self.__Delete(x,T.left)
        elif x>T.value:
            T.right= self.__Delete(x,T.right)
        else:
            self.Aux= self.__join(T.left,T.right)
            T=self.Aux

        return T

    def __join(self,l,r):
        m,n= self.__Size(l),self.__Size(r)
        t=m+n
        if t==0:
            return None
        ran= random.randint(0,t-1)
        if ran<m:
            l.right= self.__join(l.right,r)
            return l
        else:
            r.left=self.__join(l,r.left)
            return r




    def InOrder(self):
        return self.__InOrder(self.root)

    def __InOrder(self,root):
        if root:
            self.__InOrder(root.left)
            print(root.value)
            self.__InOrder(root.right)

    def PreOrder(self):
        return self.__Preorder(self.root)

    def __Preorder(self,root):
        if root:
            print(root.value)
            self.__Preorder(root.left)
            self.__Preorder(root.right)

    def PostOrder(self):
        return self.__PostOrder(self.root)

    def __PostOrder(self, x):
        if x:
            self.__PostOrder(x.left)
            self.__PostOrder(x.right)
            print(x.value)

    def Print(self):
        if self.root != None:
            self.__Print(self.root)

    def __Print(self, current_node):
        if current_node != None:
            self.__Print(current_node.left)
            print(str(current_node.value))
            self.__Print(current_node.right)

    def Height(self):
        if self.root != None:
            return self.__Height(self.root, 0)
        else:
            return 0

    def __Height(self, current_node, current_height):
        if current_node == None:
            return current_height
        l = self.__Height(current_node.left, current_height + 1)
        r = self.__Height(current_node.right, current_height + 1)
        return max(l, r)

    def FindMin(self):
        if self.root is not None:
            return 'Minimum Value:', self.__FindMin(self.root)

    def __FindMin(self, root):
        while root.left is not None:

            if root.left == None:
                break
            root = root.left
        return root.value

    def FindMax(self):
        return 'Maximum Value:', self.__FindMax(self.root)

    def __FindMax(self, root):
        while root.right is not None:
            if root.right == None:
                break
            root = root.right
        return root.value

    def Successor(self):
        return self.__Succesor(self.root)

    def __Succesor(self, root):
        return self.__FindMin(root.right)

    def Predecessor(self):
        return 'Predecessor:', self.__Predecessor(self.root)

    def __Predecessor(self, root):
        return self.__FindMax(root.left)

obj=RBST()
obj.Insert(4)
obj.Insert(5)
obj.Insert(1)
obj.Insert(2)
obj.Insert(9)
obj.Insert(10)
obj.Delete(5)
obj.InOrder()
#print(obj.Successor())
#print(obj.Predecessor())
#obj.PostOrder()
#obj.Height()




