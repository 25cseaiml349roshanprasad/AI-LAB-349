# DT : 1/10/26
# EXP 8 : WATER JUG PROBLEM

from collections import deque

# Function to solve water jug problem using BFS
def water_jug(capacity1, capacity2, target):

    visited = set()
    queue = deque()

    # Initial state: both jugs are empty
    queue.append((0, 0, []))

    while queue:

        jug1, jug2, path = queue.popleft()

        # Skip if the state has already been visited
        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # Add current state to path
        path = path + [(jug1, jug2)]

        # Check if target is reached
        if jug1 == target or jug2 == target:
            return path

        # Calculate amount transferred from jug1 to jug2
        transfer = min(jug1, capacity2 - jug2)

        # Calculate amount transferred from jug2 to jug1
        transfer2 = min(jug2, capacity1 - jug1)

        # Generate all possible next states
        next_states = [

            # Fill jug1
            (capacity1, jug2),

            # Fill jug2
            (jug1, capacity2),

            # Empty jug1
            (0, jug2),

            # Empty jug2
            (jug1, 0),

            # Pour jug1 -> jug2
            (jug1 - transfer, jug2 + transfer),

            # Pour jug2 -> jug1
            (jug1 + transfer2, jug2 - transfer2)
        ]

        # Add unvisited states to queue
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))

    # No solution found
    return None


# Main program
jug1 = int(input("Enter capacity of jug1: "))
jug2 = int(input("Enter capacity of jug2: "))
target = int(input("Enter target amount: "))

solution = water_jug(jug1, jug2, target)

if solution:
    print("\nSteps to reach the target:")

    for step in solution:
        print(step)
else:
    print("No solution exists.")
