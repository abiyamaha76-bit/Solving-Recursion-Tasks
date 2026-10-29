# 1. Factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# 2. Sum of Numbers from 1 to n
def sum_numbers(n):
    if n <= 0:
        return 0
    return n + sum_numbers(n - 1)


# 3. Power of a Number
def power(a, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / power(a, -n)
    return a * power(a, n - 1)


# 4. Count Digits
def count_digits(n):
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)


# 5. Sum of Digits
def sum_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_digits(n // 10)


# 6. Reverse a Number
def reverse_number(n):
    def reverse_helper(n, result):
        if n == 0:
            return result
        return reverse_helper(n // 10, result * 10 + n % 10)

    result = reverse_helper(abs(n), 0)
    return -result if n < 0 else result


# 7. Fibonacci Number
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Time complexity: O(2^n)
# Space complexity: O(n)


# 8. Greatest Common Divisor (GCD)
def gcd(a, b):
    if b == 0:
        return abs(a)
    return gcd(b, a % b)


# 9. Recursive Array Sum (no loops)
def array_sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0] + array_sum(arr[1:])


# 10. Find the Maximum Element
def find_max(arr):
    if len(arr) == 0:
        raise ValueError("Array must not be empty")
    if len(arr) == 1:
        return arr[0]
    maximum = find_max(arr[1:])
    return arr[0] if arr[0] > maximum else maximum


# 11. Count Occurrences
def count_occurrences(arr, x):
    if len(arr) == 0:
        return 0
    return (1 if arr[0] == x else 0) + count_occurrences(arr[1:], x)


# 12. Check for Palindrome
def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


# 13. Reverse a String
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]


# 14. Recursive Binary Search
def binary_search(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    if target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    return binary_search(arr, target, mid + 1, right)

# Time complexity: O(log n)
# Space complexity: O(log n)


# 15. Tower of Hanoi
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

# Number of moves: 2^n - 1


# 16. Generate All Subsets
def generate_subsets(arr, index=0, current=None):
    if current is None:
        current = []

    if index == len(arr):
        print(current.copy())
        return

    # Exclude the current element
    generate_subsets(arr, index + 1, current)

    # Include the current element
    current.append(arr[index])
    generate_subsets(arr, index + 1, current)
    current.pop()


# 17. Generate All Permutations
def generate_permutations(s, current=""):
    if len(s) == 0:
        print(current)
        return

    for i in range(len(s)):
        generate_permutations(
            s[:i] + s[i + 1:],
            current + s[i]
        )


# 18. Maze Solver
# 0 = open cell, 1 = wall
def solve_maze(maze):
    rows = len(maze)
    cols = len(maze[0])

    if maze[0][0] == 1 or maze[rows - 1][cols - 1] == 1:
        print("No path found")
        return

    visited = set()
    path = []

    def search(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False

        if maze[r][c] == 1 or (r, c) in visited:
            return False

        visited.add((r, c))
        path.append((r, c))

        if r == rows - 1 and c == cols - 1:
            return True

        if (search(r + 1, c) or
            search(r, c + 1) or
            search(r - 1, c) or
            search(r, c - 1)):
            return True

        path.pop()
        return False

    if search(0, 0):
        print("Path found:", path)
    else:
        print("No path found")


# 19. N-Queens Problem
def solve_n_queens(n):
    board = [-1] * n
    solutions = []

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            safe = True

            for prev_row in range(row):
                if (board[prev_row] == col or
                    abs(board[prev_row] - col) == row - prev_row):
                    safe = False
                    break

            if safe:
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)

    for number, solution in enumerate(solutions, 1):
        print(f"Solution {number}:")
        for col in solution:
            print(" ".join(
                "Q" if i == col else "." for i in range(n)
            ))
        print()

    print("Total solutions:", len(solutions))


# 20. Recursive Binary Tree Traversal
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root):
    if root is None:
        return
    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.value, end=" ")


# ==========================================
# RUN ALL 20 TASKS
# ==========================================
if __name__ == "__main__":

    print("\n1. Factorial:", factorial(5))
    print("2. Sum of numbers:", sum_numbers(5))
    print("3. Power:", power(2, 5))
    print("4. Count digits:", count_digits(58321))
    print("5. Sum of digits:", sum_digits(58321))
    print("6. Reverse number:", reverse_number(12345))
    print("7. Fibonacci:", fibonacci(7))
    print("8. GCD:", gcd(48, 18))
    print("9. Array sum:", array_sum([2, 4, 6, 8]))
    print("10. Maximum:", find_max([4, 8, 2, 15, 7]))
    print("11. Occurrences:", count_occurrences([2, 5, 2, 8, 2, 9], 2))
    print("12. Palindrome:", is_palindrome("level"))
    print("13. Reverse string:", reverse_string("algorithm"))

    print("14. Binary search index:",
          binary_search([2, 4, 7, 10, 15, 21], 15))

    print("\n15. Tower of Hanoi:")
    tower_of_hanoi(3, "A", "B", "C")

    print("\n16. All subsets:")
    generate_subsets([1, 2, 3])

    print("\n17. All permutations:")
    generate_permutations("ABC")

    print("\n18. Maze solver:")
    maze = [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    solve_maze(maze)

    print("\n19. N-Queens (N=4):")
    solve_n_queens(4)

    print("20. Binary tree traversals:")
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(2)
    root.left.right = Node(7)
    root.right.right = Node(20)

    print("Preorder:", end=" ")
    preorder(root)
    print()

    print("Inorder:", end=" ")
    inorder(root)
    print()

    print("Postorder:", end=" ")
    postorder(root)
    print()