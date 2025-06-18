from datetime import datetime

class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")
        self.status = False

    def mark_complete(self):
        self.status = True

    def __repr__(self):
        status_text = "Completed" if self.status else "Incomplete"
        return f"{self.title} | {self.description} | Due: {self.due_date.date()} | Status: {status_text}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_all_tasks(self):
        for task in self.tasks:
            print(task)

    def list_incomplete_tasks(self):
        for task in self.tasks:
            if not task.status:
                print(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title.lower() == title.lower():
                task.mark_complete()
                print(f" Task '{title}' marked complete.")
                return
        print(" Task not found.")

def todo_main():
    todo = ToDoList()
    todo.add_task(Task("Math", "Do exercises", "2025-06-20"))
    todo.add_task(Task("Read book", "Finish Chapter 3", "2025-06-22"))

    while True:
        print("\n📋 ToDo List Menu")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. Show All Tasks")
        print("4. Show Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose (1-5): ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due Date (YYYY-MM-DD): ")
            todo.add_task(Task(title, desc, due))
        elif choice == "2":
            title = input("Enter title to complete: ")
            todo.mark_task_complete(title)
        elif choice == "3":
            todo.list_all_tasks()
        elif choice == "4":
            todo.list_incomplete_tasks()
        elif choice == "5":
            break
        else:
            print("Invalid input.")

todo_main()


from datetime import datetime

class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.created_at = datetime.now()

    def __repr__(self):
        return f"\n {self.title} by {self.author} on {self.created_at.strftime('%Y-%m-%d %H:%M')}\n{self.content}"

class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        for post in self.posts:
            print(post)

    def posts_by_author(self, author):
        found = False
        for post in self.posts:
            if post.author.lower() == author.lower():
                print(post)
                found = True
        if not found:
            print(" No posts by that author.")

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f" Deleted post '{title}'")
                return
        print("Post not found.")

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title.lower() == title.lower():
                post.content = new_content
                print(f"✏️ Edited post '{title}'")
                return
        print(" Post not found.")

    def latest_posts(self, count=3):
        for post in sorted(self.posts, key=lambda x: x.created_at, reverse=True)[:count]:
            print(post)

def blog_main():
    blog = Blog()
    blog.add_post(Post("Welcome", "This is our blog!", "Admin"))
    blog.add_post(Post("Python", "Learn Python basics", "Alice"))

    while True:
        print("\n Blog Menu")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Posts by Author")
        print("4. Edit Post")
        print("5. Delete Post")
        print("6. Latest Posts")
        print("7. Exit")

        choice = input("Choose (1-7): ")

        if choice == "1":
            title = input("Title: ")
            content = input("Content: ")
            author = input("Author: ")
            blog.add_post(Post(title, content, author))
        elif choice == "2":
            blog.list_all_posts()
        elif choice == "3":
            name = input("Author name: ")
            blog.posts_by_author(name)
        elif choice == "4":
            title = input("Title to edit: ")
            content = input("New content: ")
            blog.edit_post(title, content)
        elif choice == "5":
            title = input("Title to delete: ")
            blog.delete_post(title)
        elif choice == "6":
            blog.latest_posts()
        elif choice == "7":
            break
        else:
            print("Invalid input.")

blog_main()



class Account:
    def __init__(self, number, holder, balance=0):
        self.number = number
        self.holder = holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f" Deposited {amount}")
        else:
            print(" Invalid amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f" Withdrawn {amount}")
        else:
            print(" Insufficient funds.")

    def __repr__(self):
        return f"Account {self.number} | Holder: {self.holder} | Balance: {self.balance}"

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, acc):
        self.accounts.append(acc)

    def find_account(self, number):
        for acc in self.accounts:
            if acc.number == number:
                return acc
        return None

    def transfer(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)
        if sender and receiver:
            if sender.balance >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print(" Transfer complete.")
            else:
                print(" Not enough funds.")
        else:
            print(" Account(s) not found.")

def bank_main():
    bank = Bank()
    bank.add_account(Account("001", "Alice", 1000))
    bank.add_account(Account("002", "Bob", 500))

    while True:
        print("\n Banking System")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Show All Accounts")
        print("7. Exit")

        choice = input("Choose (1-7): ")

        if choice == "1":
            number = input("Account number: ")
            name = input("Holder name: ")
            bank.add_account(Account(number, name))
        elif choice == "2":
            number = input("Account number: ")
            acc = bank.find_account(number)
            print(acc if acc else " Account not found.")
        elif choice == "3":
            number = input("Account number: ")
            amount = float(input("Amount: "))
            acc = bank.find_account(number)
            if acc:
                acc.deposit(amount)
            else:
                print(" Account not found.")
        elif choice == "4":
            number = input("Account number: ")
            amount = float(input("Amount: "))
            acc = bank.find_account(number)
            if acc:
                acc.withdraw(amount)
            else:
                print(" Account not found.")
        elif choice == "5":
            from_acc = input("From account: ")
            to_acc = input("To account: ")
            amount = float(input("Amount: "))
            bank.transfer(from_acc, to_acc, amount)
        elif choice == "6":
            for acc in bank.accounts:
                print(acc)
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

bank_main()

