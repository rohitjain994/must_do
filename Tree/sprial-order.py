def spiralOrderTraversal(root):
     
    if root is None:
        return
 
    # create an empty double-ended queue and enqueue the root node
    q = deque()         # or use deque
    q.appendleft(root)
 
    # `flag` is used to differentiate between odd or even level
    flag = False
 
    # loop till deque is empty
    while q:
 
        # calculate the total number of nodes at the current level
        nodeCount = len(q)
 
        # print left to right
        if flag:
            # process each node of the current level and enqueue their
            # non-empty left and right child to deque
            while nodeCount > 0:
                # pop from the front if `flag` is true
                curr = q.popleft()
                print(curr.key, end=' ')
 
                # it is important to push the left child into the back,
                # followed by the right child
 
                if curr.left:
                    q.append(curr.left)
 
                if curr.right:
                    q.append(curr.right)
 
                nodeCount = nodeCount - 1
 
        # print right to left
        else:
            # process each node of the current level and enqueue their
            # non-empty right and left child
            while nodeCount > 0:
                # it is important to pop from the back
                curr = q.pop()
                print(curr.key, end=' ')    # print front node
 
                # it is important to push the right child at the front,
                # followed by the left child
 
                if curr.right:
                    q.appendleft(curr.right)
 
                if curr.left:
                    q.appendleft(curr.left)
 
                nodeCount = nodeCount - 1
 
        # flip the flag for the next level
        flag = not flag
        print()