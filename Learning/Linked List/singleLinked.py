class Node:
    def __init__(self,val):
        self.val = val
        self.next: Node | None = None

node1 = Node(5)
node2 = Node(10)
node3 = Node(7)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

# print(node1.next.val,node2.val)

class SLL:
    def __init__(self):
        self.head: Node | None = None
          
    def append(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node 
    
    def traveral(self):
        if self.head is None:
            print("SLL is empty")
            
        else:
            curr = self.head 
            while (curr is not None):
                print(curr.val,end=" ")
                curr = curr.next
            print()
            
    def insert(self,index,value):
        new_node = Node(value)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        i = 0
        curr = self.head
        while (i<index-1):
            curr = curr.next #type:ignore
            i += 1
        print(i,curr.val)  # type: ignore
        temp = curr.next  #type:ignore
        curr.next = new_node
        new_node.next = temp
        
            
        
        
        
sll = SLL()
sll.append(5)
sll.append(8)
sll.append(7)
sll.append(10)
sll.traveral()
sll.insert(2,9)
sll.insert(0,9)
sll.traveral()
