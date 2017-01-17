
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def print_list(head):
    if head == 'NULL':
        a = Node(data='NULL',next_node='')
        print a.next
    else:
        
if __name__ == '__main__':
    a = raw_input()
    print_list(a)