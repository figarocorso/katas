class BidirectionalNode():

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next_node = None
        self.previous_node = None

    def __str__(self):
        return '(' + str(self.key) + ',' + str(self.value) + ')'

class BidirectionalList():

    def __init__(self):
        self.first_node = BidirectionalNode(None,None)
        self.end_of_list = BidirectionalNode(None,None)

        self.first_node.next_node = self.end_of_list
        self.end_of_list.previous_node = self.first_node
        self.last_node = self.first_node

    def add(self, node):
        node.previous_node = self.last_node
        node.next_node = self.end_of_list

        self.end_of_list.previous_node = node
        self.last_node.next_node = node

        self.last_node = node

        return node.value

    def delete(self, key):
        node = self.find(key)

        if node:
            node.previous_node.next_node = node.next_node
            node.next_node.previous_node = node.previous_node

            return True

        return False

    def find(self, key):
        self.current_node = self.first_node

        while not self.is_last_node(self.current_node):
            if self.equal_key(self.current_node,key):
                return self.current_node

            self.current_node = self.current_node.next_node

        return False

    def equal_key(self, node, key):
        return node.key == key

    def is_last_node(self, node):
        return node.next_node == None

    def __str__(self):
        return str(self.first_node)
