class DirectNode():

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None

    def __str__(self):
        return '(' + str(self.key) + ',' + str(self.value) + ',' + str(self.next_node) + ')'

class DirectList():

    def __init__(self):
        self.first_node = DirectNode(None,None)
        self.end_of_list = DirectNode(None,None)
        self.last_node = self.first_node

    def add(self, node):
        self.last_node.next_node = node
        node.next_node = self.end_of_list
        self.last_node = node

        return node.value

    def delete(self, key):
        self.previous_node = self.first_node
        self.current_node = self.first_node.next_node

        while not self.is_last_node(self.current_node):
            if self.current_node.key == key:
                self.previous_node.next_node = self.current_node.next_node
                return True

            self.current_node = self.current_node.next_node
            self.previous_node = self.previous_node.next_node

        return False

    def find(self, key):
        self.current_node = self.first_node

        while not self.is_last_node(self.current_node):
            if self.current_node.key == key:
                return self.current_node.value

            self.current_node = self.current_node.next_node

        return None

    def is_last_node(self, node):
        return node.next_node == None

    def __str__(self):
        return str(self.first_node)
