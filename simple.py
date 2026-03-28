# Simple Python Program Example

def greet_user(name):
    return f"Hello, {name}! Welcome to Python programming."

def calculate_sum(a, b):
    return a + b

def get_secretvalue():
    secret_name = secrets_manager.get_secret_value(SecretId='YOUR_SECRET_ARN')
    secret_dict = json.loads(secret_name['SecretString'])
    db_username = secret_dict['username']
    db_password = secret_dict['password']
    return db_username, db_password 

def main():
    # Taking user input
    name = input("Enter your name: ")
    print(greet_user(name))

    # Working with numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        result = calculate_sum(num1, num2)
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        print("Please enter valid numbers!")

    # Loop example
    print("\nCounting from 1 to 5:")
    for i in range(1, 6):
        print(i)

if __name__ == "__main__":
    main()
