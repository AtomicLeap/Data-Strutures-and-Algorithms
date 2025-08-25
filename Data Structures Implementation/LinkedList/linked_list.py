# Linked List

# Define a Node class
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

# Define LinkedList class
class LinkedList:
  def __init__(self):
    self.head = None
    self.count = 0

# Add new node at the end
  def append(self, value):
    current = self.head
    new_node = Node(value)

    if not current:
      self.head = new_node
      self.count += 1
      return
    
    while current.next:
      current = current.next
    
    current.next = new_node
    self.count += 1

  def contains(self, value):
    current = self.head

    while current:
      if current.value == value:
        print('Linked list contains: ', value)
        return True
      current = current.next
    print('Linked list does not contain: ', value)
    return False
  
  def delete(self, value):
    current = self.head
    previous = None

    if current.value == value:
      self.head = current.next
      self.count -= 1
      return

    while current:
      if current.value == value:
        previous.next = current.next
        self.count -= 1
        return
      previous = current
      current = current.next
   
    # Print linked list
  def print(self):
    current = self.head

    while current:
      print(current.value, end=" -> ")
      current = current.next
    print("None")

# Reverse linked list
  def reverse(self):
    previous = None
    current = self.head

    while current:
      next_node = current.next
      current.next = previous
      previous = current
      current = next_node
    self.head = previous

  def size(self):
    print(f"Linked list size: {self.count}")
    return self.count

linkedlist = LinkedList()
linkedlist.print()
linkedlist.append("A")
linkedlist.append("B")
linkedlist.append("C")
linkedlist.append("D")
linkedlist.append("E")
linkedlist.print()
linkedlist.size()
linkedlist.delete("A")
linkedlist.print()
linkedlist.size()
linkedlist.contains("C")
linkedlist.reverse()
linkedlist.delete("C")
linkedlist.print()
linkedlist.size()
linkedlist.contains("C")

