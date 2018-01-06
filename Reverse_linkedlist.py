##Iteration

def reverse(head):
  prev = None
  while head:
    curr = head
    head = head.next
    curr.next = prev
    prev = curr
  return prev
  
  
##Recursion
  
def reverse(head):
  helper(head)

def helper(Node,prev = None):
  if Node is None:
    return prev
  #curr = Node
  new_Node = Node.next
  Node.next = prev
  prev = Node
  return helper(new_Node,prev)
    
