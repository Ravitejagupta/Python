class Node:
  def __init__(self, val):
    self.value = val
    self.leftchild = None
    self.rightchild = None
    
  def insert(self,data):
    if self.value == data:
      return False
    elif self.value > data:
      if self.leftchild:
        return self.leftchild.insert(data)
      else:
        self.leftchild = Node(data)
        return True
    else:
      if self.rightchild:
        return self.rightchild.insert(data)
      else:
        self.rightchild = Node(data)
        return True
        
  def find(self, data):
    if(self.value ==data):
      return True
    elif data < self.value:
      if (self.leftchild):
        return self.leftchild.find(data)
      else:
        return False
    else:
      if (self.rightchild):
        return self.rightchild.find(data)
      else:
        return False
  
  def preorder(self):
    if self:
      print (str(self.value))
      if self.leftchild:
        self.leftchild.preorder()
      if self.rightchild:
        self.rightchild.preorder()
        
  def postorder(self):
    if self:
      if self.leftchild:
        self.leftchild.postorder()
      if self.rightchild:
        self.rightchild.postorder()
      print (str(self.value))
  
  def inorder(self):
    if self:
      if self.leftchild:
        self.leftchild.inorder()
      print (str(self.value))
      if self.rightchild:
        self.rightchild.inorder()
      
class Tree:
  def __init__(self):
    self.root = None
    
  def insert(self, data):
    if self.root:
      return self.root.insert(data)
    else:
      self.root = Node(data)
      return True
      
  def find(self, data):
    if self.root:
      return self.root.find(data)
    else:
      return False
      
  def preorder(self):
    print("Pre-Order")
    self.root.preorder()
      
  def postorder(self):
    print("Post-Order")
    self.root.postorder()
      
  def inorder(self):
    print("In-Order")
    self.root.inorder()
     
  def remove(self,data):
    if self.root is None:
      return False
    elif self.root.value == data:
      if self.root.leftchild is None and self.root.rightchild is None:
        self.root = None
      elif self.root.rightchild is None and self.root.leftchild:
        self.root = self.root.leftchild
      elif self.root.rightchild and self.root.leftchild is None:
        self.root = self.root.rightchild
      elif self.root.rightchild and self.root.leftchild:
        delNodeParent = self.root
        delNode = self.root.rightchild
        while delNode.leftchild:
          delNodeParent = delNode
          delNode = delNode.leftchild
        
        self.root.value = delNode.value
        if delNode.rightchild:
          if delNodeParent.value > delNode.value:
            delNodeParent.leftchild = delNode.rightchild
          elif delNodeParent.value < delNode.value:
            delNodeParent.rightchild = delNode.rightchild
        else:
          if delNode.value < delNodeParent.value:
            delNodeParent.leftchild = None
          else:
            delNodeParent.rightchild = None
            
      return True
    parent = None
    node = self.root
    
    #finding node
    while node and node.value !=data:
      parent = node
      if data < node.value:
        node = node.leftchild
      else:
        node = node.rightchild
        
    #case 1: if data not found
    if node is None and node.value != data:
      return False
      
    #case 2 : No children
    elif node.leftchild is None and node.rightchild is None:
      if data <parent.value:
        parent.leftchild = None
      else:
        parent.rightchild = None
      return True
      
    #case 3: Only left children
    elif node.leftchild and node.rightchild is None:
      if data < parent.value:
        parent.leftchild = node.leftchild
      else:
        parent.rightchild = node.leftchild
        
    #case 4: Only rightchild
    elif node.rightchild and node.leftchild is None:
      if data > parent.value:
        parent.rightchild = node.rightchild
      else:
        parent.leftchild = node.rightchild
        
    #case 5: Both left and right
    else:
      delNodeParent = node
      delNode = node.rightchild
      while delNode.leftchild:
        delNodeParent = delNode
        delNode = delNode.leftchild
      
      node.value = delNode.value
      if delNode.rightchild:
        if delNodeParent.value > delNode.value:
          delNodeParent.leftchild = delNode.rightchild
        elif delNodeParent.value < delNode.value:
          delNodeParent.rightchild = delNode.rightchild
          
      else:
        if delNode.value <delNodeParent.value:
          delNodeParent.leftchild = None
        else:
          delNodeParent.rightchild = None
            
    
    
bst = Tree()
print(bst.insert(10))
bst.insert(14)
print(bst.insert(5))
print(bst.insert(6))
bst.remove(10)
bst.preorder()
bst.postorder()
