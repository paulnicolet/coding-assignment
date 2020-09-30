class Node(object):
    """ Represents a node in the class graph.
    It keeps track of its parent and children.
    """

    def __init__(self, parent):
        self.parent = parent
        self.children = []
