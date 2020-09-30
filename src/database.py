from src.node import Node
from src.status import Status


class Database(object):
    """Represents a database storing a dynamic class structure.

    We use a tree structure to store nodes with their current status.
    A status is a property of the node, and is not associated to an image, 
    since all images associated to a given class share the same status.
    The high-level strategy is to make the main computations during the write phase, 
    and provide a light read, at the expense of storing statuses.

    Please see the README file for more details.
    """

    def __init__(self, root_name):
        """Init database with the root class name.

        Args:
            root_name (str): The root class name.
        """
        self.name_to_node = {root_name: Node(None)}
        self.extract = None

    def add_nodes(self, elements):
        """Add nodes to the structure.
        This might trigger status computing if needed.

        Args:
            elements (List[Tuple[str, str]]): The new elements to add, 
            of the form (child name, parent name).
        """
        for child_name, parent_name in elements:
            # Add node to structure
            parent = self._add_node(child_name, parent_name)

            # Update node status if required
            if self._should_compute_status():
                parent.update_status_new_child()

    def add_extract(self, extract):
        """Add extract to the database.

        Args:
            extract (Dict[str, List[str]]): The image extract of the form 
            (image name -> [class name 1, class name 2, ...])
        """
        self.extract = extract

    def get_extract_status(self):
        """Returns the extract status.

        Returns:
            Dict[str, str]: The extract status.
        """
        return {
            img_name: self._get_status(node_names).value
            for img_name, node_names in self.extract.items()
        }

    def _add_node(self, child_name, parent_name):
        """Add a new node to the database.
        """
        # Get parent and create child, suppose parent always exists
        parent = self.name_to_node[parent_name]
        child = Node(parent)

        # Add new node to structure
        parent.children.append(child)
        self.name_to_node[child_name] = child

        return parent

    def _get_status(self, node_names):
        """Compute the status of each node, and aggregate to the final one.
        """
        statuses = {self._get_node_statuses(name) for name in node_names}
        return Status.aggregate(statuses)

    def _get_node_statuses(self, node_name):
        """Compute the status of a single node.
        """
        # Label does not exist in structure
        if not node_name in self.name_to_node:
            return Status.INVALID

        return self.name_to_node[node_name].status

    def _should_compute_status(self):
        """Returns True if an extract has already been added.
        """
        return self.extract is not None
