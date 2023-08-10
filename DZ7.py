
class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None


    def print_list(self):
        if self.head is None:
            print("Список пуст!")
            return
        else:
            cur_node = self.head
            while cur_node is not None:
                print(cur_node.value, end = " ")
                cur_node = cur_node.next
                
    
    def insert_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
 
        
    def insert_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
            cur_node.next = new_node
 
            
    def insert_after(self, ind, value):
        cur_node = self.head
        while cur_node is not None:
            cur_node = cur_node.next
            if cur_node.value == ind:
                break
        if cur_node is None:
            print("Список пуст!")
        else:
            new_node = Node(value)
            new_node.next = cur_node.next
            cur_node.next = new_node

            
    def get(self):
        if self.head is None:
            return 0
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.next
        return count


    def find(self, value):
        if self.head is not None:
            if self.head.value == value:
                return True
            else:
                print()
        else:
            print("Список пуст!")

        cur_node = self.head
        while cur_node is not None:
            if cur_node.value == value:
                return True
            cur_node = cur_node.next
        return False 
 
    
    def delete(self, value):
        cur_node = self.head
        if list.find(value) is True:
            if value is self.head.value:
                self.head = cur_node.next
                return
            else:
                prev = None
                while cur_node is not None:
                    if cur_node.value == value:
                        if prev is not None:
                            prev.next = cur_node.next
                        else:
                            self.head = cur_node.next
                            return
                    prev = cur_node
                    cur_node = cur_node.next
        else:
            print("Данного числа нет в списке")


    def reverse(self):
        prev = None
        cur_node = self.head
        while cur_node is not None:
            next = cur_node.next
            cur_node.next = prev
            prev = cur_node
            cur_node = next
            self.head = prev


    def sort(self):
        end = None
        while end != self.head:
            cur_node = self.head
            while cur_node.next != end:
                node = cur_node.next
                if cur_node.value > node.value:
                    cur_node.value, node.value = node.value, cur_node.value
                cur_node = cur_node.next
            end = cur_node

    
list = LinkedList()
  
list.insert_end(4)

list.print_list()

print()

list.insert_start(1)
list.insert_start(2)
list.insert_start(3)

list.print_list()

print()

list.insert_end(5)

list.print_list()

print()

list.insert_after(1, 6)

list.print_list()

print()

print(list.get())

print()

list.reverse()

list.print_list()

print()

print(list.find(3))

list.delete(3)

list.print_list()

list.sort()

print()

list.print_list()
