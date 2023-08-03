
#!/usr/bin/python3
"""Determines if all the boxes can be opened."""


def canUnlockAll(boxes):
    """Returns True if all boxes be visited, otherwise False."""
    n = len(boxes)
    visited = [False] * n
    stack = [0]

    while stack:
        box = stack.pop()
        visited[box] = True

        for key in boxes[box]:
            if not visited[key]:
                stack.append(key)

    return all(visited)
