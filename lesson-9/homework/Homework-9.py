# 1. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

# 2. Person Class
class Person:
    def __init__(self, name, country, birth_year):
        self.name = name
        self.country = country
        self.birth_year = birth_year
    def age(self, current_year):
        return current_year - self.birth_year

# 3. Calculator Class
class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b): return a / b

# 4. Shape and Subclasses
class Shape:
    def area(self): raise NotImplementedError
    def perimeter(self): raise NotImplementedError

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side * self.side
    def perimeter(self): return 4 * self.side

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def perimeter(self):
        return self.a + self.b + self.c
    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

class CircleShape(Shape):
    def __init__(self, radius): self.radius = radius
    def area(self): return 3.14 * self.radius * self.radius
    def perimeter(self): return 2 * 3.14 * self.radius

# 5. Binary Search Tree Class
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)
    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
            else:
                self._insert(node.right, value)
    def search(self, value):
        return self._search(self.root, value)
    def _search(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

# 6. Stack Data Structure
class Stack:
    def __init__(self):
        self._data = []
    def push(self, item):
        self._data.append(item)
    def pop(self):
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

# 7. Linked List Data Structure
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, value):
        node = ListNode(value)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node
    def delete(self, value):
        curr = self.head
        prev = None
        while curr:
            if curr.value == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False
    def display(self):
        values = []
        curr = self.head
        while curr:
            values.append(curr.value)
            curr = curr.next
        print(values)

# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = []  # list of (name, price)
    def add_item(self, name, price):
        self.items.append((name, price))
    def remove_item(self, name):
        self.items = [item for item in self.items if item[0] != name]
    def total_price(self):
        total = 0
        for _, price in self.items:
            total += price
        return total

# 9. Stack with Display
class DisplayStack(Stack):
    def display(self):
        print(self._data)

# 10. Queue Data Structure
class Queue:
    def __init__(self):
        self._data = []
    def enqueue(self, item):
        self._data.append(item)
    def dequeue(self):
        if not self._data:
            raise IndexError("dequeue from empty queue")
        return self._data.pop(0)

# 11. Bank Class
class Account:
    def __init__(self, acct_no, owner, balance=0):
        self.acct_no = acct_no
        self.owner = owner
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, acct_no, owner, balance=0):
        if acct_no in self.accounts:
            raise ValueError("Account already exists")
        self.accounts[acct_no] = Account(acct_no, owner, balance)
    def deposit(self, acct_no, amount):
        acct = self.accounts[acct_no]
        acct.balance += amount
    def withdraw(self, acct_no, amount):
        acct = self.accounts[acct_no]
        if amount > acct.balance:
            raise ValueError("Insufficient funds")
        acct.balance -= amount
    def get_balance(self, acct_no):
        return self.accounts[acct_no].balance
    def transfer(self, from_acct, to_acct, amount):
        self.withdraw(from_acct, amount)
        self.deposit(to_acct, amount)
