#simple interest calculator

principal = 1000
rate = 0.05
time = 3

def calculate_simple_interest(principal, rate, time):
    interest = principal * rate * time
    return print(f"The simple interest is: {interest}")

calculate_simple_interest(principal, rate, time)