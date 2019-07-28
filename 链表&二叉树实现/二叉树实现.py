class Node(object):
    def __init__(self,elem = -1,lchild = None, rchild = None):
        self.elem =elem
        self.lchild = lchild
        self.rchild = rchild

class Tree:
    def __init__(self,root =None):
        self.root = root

    def add(self,elem):
        node = Node(elem)
        if self.root == None:
            self.root = node
        else:
            queue =[]
            queue.append(self.root)
            while queue:
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)
#先序遍历
def preorder(root):
    if root == None:
        return
    print(root.elem)
    preorder(root.lchild)
    preorder(root.rchild)
#深度遍历
"""
新建一个栈
把root存入栈中
如果左子节点不为空，存进去
又子节点不为空，存进去
"""
def bread_travel(root):
    if root == None:
        return
    queue =[]
    queue.append(root)
    while queue:
        node = queue.pop(0)
        print(node.elem)
        if node.lchild !=None:
            queue.append(node.lchild)
        if node.rchild != None:
            queue.append(node.rchild)
s = Tree()
s.add(1)
s.add(2)
s.add(3)
s.add(4)
preorder(s.root)
bread_travel(s.root)