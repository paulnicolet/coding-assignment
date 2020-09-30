from src.status import Status


class Node(object):
    """ Represents a node in the class graph.
    It keeps track of its parent, children and a status, valid by default.
    """

    def __init__(self, parent):
        self.parent = parent
        self.children = []
        self.status = Status.VALID

    @property
    def is_valid(self):
        return self.status == Status.VALID

    def update_status_new_child(self):
        """Compute and update the status using the parent node.
        """
        # If not valid, GRANULARITY_STAGED does not take priority
        if self.is_valid:
            self.status = Status.GRANULARITY_STAGED

        # Override status of all children
        for neighbor in self.children:
            neighbor.status = Status.COVERAGE_STAGED
