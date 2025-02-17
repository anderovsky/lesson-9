class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return

    def show_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" / ")
            current_node = current_node.next
        print(None)

    def check_list(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                print(f"This node is in the list")
            current_node = current_node.next

    def replace_node(self, old_data, new_data):
        current_node = self.head
        while current_node:
            if current_node.data == old_data:
                current_node.data = new_data
                return True
            current_node = current_node.next


my_list = LinkedList()
my_list.add_node(10)
my_list.add_node(30)
my_list.add_node(4)
my_list.add_node(999)
my_list.show_list()
my_list.delete_node(10)
my_list.show_list()
my_list.check_list(999)
my_list.check_list(15)
my_list.replace_node(999, 33)
my_list.show_list()
