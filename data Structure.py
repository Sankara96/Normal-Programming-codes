"""
 Print elements of a linked list on console
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""


def print_list(head):
    if head == 'NULL':
        a = Node(data='NULL', next_node='')
        print a.next
    else:
        while (True):
            a = Node(data=head.data, next_node=head.next)
            print a.data
            head = head.next
            B = frozenset([])
            B.
            if head is None:
                break