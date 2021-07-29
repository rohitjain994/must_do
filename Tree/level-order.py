def levelOrderTraversal(root):
     
    # create an empty queue and enqueue the root node
    queue = deque()
    queue.append(root)
 
    # loop till queue is empty
    while queue:
 
        # process each node in the queue and enqueue their
        # non-empty left and right child
        curr = queue.popleft()
 
        print(curr.key, end=' ')
 
        if curr.left:
            queue.append(curr.left)
 
        if curr.right:
            queue.append(curr.right)