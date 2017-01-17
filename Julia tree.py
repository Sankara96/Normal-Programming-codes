class Node(object):

    def __init__(self,Key):
        self.lchild = None
        self.rchild = None
        self.data = Key
    def check(self):
        if self.lchild is not None and self.rchild is not None:
            return 2
        elif self.rchild is None and self.lchild is not None:
            return 1
        elif self.rchild is not None and self.lchild is None:
            return 1
        elif self.rchild is None and self.lchild is None:
            return 0

class Tree(object):

    def __init__(self):
        self.root = None
        self.size = 0



def insert(node,value):
    temp = node
    if value>temp.data:
        if temp.rchild is None:
            temp.rchild = Node(value)
        else:
            insert(temp.rchild,value)
    elif value<temp.data:
        if temp.lchild is None:
            temp.lchild = Node(value)
        else:
            insert(temp.lchild,value)


def maxDepth(node):
    if node is None:
        return 0;

    else:

        # Compute the depth of each subtree
        lDepth = maxDepth(node.lchild)
        rDepth = maxDepth(node.rchild)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1
def kthnode(node,k):
    if node is None:
        return 0
    else:
        if k==0:
            return 1
        else:
            a = kthnode(node.lchild,k-1)
            b = kthnode(node.rchild,k-1)
            return a+b

if __name__ == '__main__':
    t = Tree()
    t.size = input()
    temp = raw_input().split()
    temp = [int(x) for x in temp]
    root = t.root
    for elements in temp:
        if t.root is None:
            t.root = Node(elements)
        else:
            insert(t.root,elements)
    root = t.root
    depth = maxDepth(t.root)
    value = 0
    for i in xrange(depth):
        value+= kthnode(t.root,i)*i
    print value