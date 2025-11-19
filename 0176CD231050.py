student_db = {}
logged_user = None

def register():
    print("--- Register ---")
    username = input("Enter username: ")
    if username in student_db:
        print("Username already exists.")
        return
    password = input("Enter password: ")
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    course = input("Enter your course: ")
    student_db[username] = {'password': password,'name': name,'age': age,'course': course}
    print("Registration successful")

def login():
    global logged_user
    print("--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in student_db and student_db[username]['password'] == password:
        logged_user = username
        print("Login successful")
    else:
        print("Invalid username or password")

def view_profile():
    if logged_user is None:
        print("Login required to view profile.")
        return
    user_data = student_db[logged_user]
    print("--- Profile ---")
    print(f"Name: {user_data['name']}")
    print(f"Age: {user_data['age']}")
    print(f"Course: {user_data['course']}")

def update_profile():
    if logged_user is None:
        print("Login required to update profile")
        return
    print("--- Update Profile ---")
    user_data = student_db[logged_user]
    name = input(f"Enter new name (current: {user_data['name']}): ")
    age = input(f"Enter new age (current: {user_data['age']}): ")
    course = input(f"Enter new course (current: {user_data['course']}): ")
    if name:
        student_db[logged_user]['name'] = name
    if age:
        student_db[logged_user]['age'] = age
    if course:
        student_db[logged_user]['course'] = course
    print("Profile updated successfully")

def logout():
    global logged_user
    if logged_user:
        print(f"User {logged_user} logged out")
        logged_user = None
    else:
        print("No user is logged in")

def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. Register")
        print("2. Login")
        print("3. View Profile")
        print("4. Update Profile")
        print("5. Logout")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            view_profile()
        elif choice == '4':
            update_profile()
        elif choice == '5':
            logout()
        elif choice == '6':
            print("Exiting the system")
            break
        else:
            print("Invalid choice. Try again")

main()