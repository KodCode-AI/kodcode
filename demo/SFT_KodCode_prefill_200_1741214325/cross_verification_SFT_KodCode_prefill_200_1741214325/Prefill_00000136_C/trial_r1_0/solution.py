from typing import Optional

def enqueue(queue, item) -> None:
    """
    Adds an item to the end of the queue.
    """
    queue.append(item)

def dequeue(queue) -> Optional[int]:
    """
    Removes and returns the item from the front of the queue.
    If the queue is empty, returns None.
    """
    if not queue:
        return None
    return queue.pop(0)