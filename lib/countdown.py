# your code goes here!
import time  # Import the time module for the sleep function

def countdown(seconds):
    while seconds > 0:
        print(f'{seconds} SECOND(S)!')
        seconds -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(seconds):
    while seconds > 0:
        print(f'{seconds} SECOND(S)!')
        time.sleep(1)  # Sleep for one second
        seconds -= 1
    print('HAPPY NEW YEAR!')

# Example usage
countdown(10)
print("===")
countdown_with_sleep(10)

