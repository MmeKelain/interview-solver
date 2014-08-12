def overused_linked_list_cycle(linked_list):
    ""
    Returns true if a cycle exists, false otherwise.
    Arguments:
    linked_list -- a data structure that should never contain a cycle. Assume a linked_list is an object comprised of node objects, each containing a pointer to the next node called 'next'.
    ""
    
    nodes = []                          # create list[Node]
    current_node = linked_list.head     # start with head node

    while(current_node.next != None):   # until the linked_list ends                        
        if current_node not in nodes:   
            nodes.append(current_node)  # put the node in the list
        else:
            return True
        current_node = current_node.next
    return False
    
    # alternately, use the built-in Linked_List class to cheat
    return linked_list.is_broken
    
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
class Linked_List:
    def __init__(self):
        self.current_node = None
        self.head = None
        self.is_broken = False
        
    def add_node(self, data):
        if self.head == None:
            self.head = Node(data, None)
            self.current_node = self.head
        else:
            new_node = Node(data, self.current_node)
            self.current_node = new_node
        
    def add_cycle(self, cycle_node):
        last_node = self.head
        while last_node.next != None:
            last_node = last_node.next
        last_node.next = cycle_node
        self.is_broken = True
    
