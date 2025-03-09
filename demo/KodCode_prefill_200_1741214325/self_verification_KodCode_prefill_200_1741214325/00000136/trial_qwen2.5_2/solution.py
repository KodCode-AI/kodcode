def enqueue(queue, item):
    """
    Adds an item to the end of the queue.
    """
    queue.append(item)

def dequeue(queue):
    """
    Removes and returns the item from the front of the queue.
    If the queue is empty, returns None.
    """
    if len(queue) > 0:
        return queue.pop(0)
    else:
        return None