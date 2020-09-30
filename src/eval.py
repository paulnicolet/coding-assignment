
def accuracy(expected_status, computed_status):
    """Compute accuracy of computed status.

    Args:
        expected_status (Dict[str, str]): The expected status.
        computed_status (Dict[str, str]): The computed status.

    Returns:
        float: The accuracy.
    """
    shared_items = {
        k: expected_status[k] for k in expected_status
        if k in computed_status and computed_status[k] == expected_status[k]
    }

    return len(shared_items) / len(expected_status)
