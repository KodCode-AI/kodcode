def enqueue(queue, item) -> None:
    queue.append(item)

def dequeue(queue) -> int:
    if not queue:
        return None
    return queue.pop(0)