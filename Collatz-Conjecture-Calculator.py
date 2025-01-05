import time

bold = "\033[1m" 
reset = "\033[0m"

print(bold + "This is the Collatz Conjecture Calculator!" + reset)
print("This is a calculator to help show how the Collatz Conjecture works.")
print(bold + "Why?" + reset + " Beacue I thought the idea of this mathmatics")
print("problem was intriguing and want to share it a little.")

print() # Used to space two text blocks

print(bold + "What is the Collatz Conjecture?" + reset)
print("The Collatz Conjecture is a mathematical conjecture that asks whether")
print("repeating two arithmetic operations will eventually")
print("transform every positive integer into 1.")

print() # Used to space two text blocks

print(bold + "The Collatz Conjecture follows two rules:" + reset)
print("1. If the positive integer is odd, then")
print("   you multiply it by 3 and add 1 ((n*3)+1).")
print("2. If the psoitive integer is even, then")
print("   you divide it by 2 (n/2).")
print(bold + "For example:" + reset)
print("Let's choose 5 as our number.")
print("5 is odd: (5*3)+1 = 16, 16 is even: 16/2 = 8, 8 is even: 8/2 = 4,")
print("4 is even: 4/2 = 2, 2 is even: 2/2 = 1")

print() # Used to space two text blocks

while True:
    print(bold + "Now you try!" + reset)
    origonal_num = input("Choose a positive number to use: ")
    print() # Used to space two text blocks 

    if not origonal_num.isdigit():
        print(bold + "That's not a valid number. Please try gain." + reset)
        print()
        continue

    try:
        start_time = time.time() # Record the start time
        num2 = int(origonal_num) # Number after operation is done
        steps = 0
        odd_steps = 0
        even_steps = 0
        while num2 != 1:
            num1 = int(num2) # Number before operation is done

            if num1 % 2 == 0:
                num2 = num1 // 2
                print(f"{num1} is even: {num1}/2 = {num2}")
                even_steps += 1
            else:
                num2 = (num1 * 3) + 1
                print(f"{num1} is odd: ({num1}*3)+1 = {num2}")
                odd_steps += 1
            steps += 1

        end_time = time.time() # Record the end time
        elapsed_time = end_time - start_time  # Calculate the elapsed time

        print(f"It took {steps} total steps to turn {origonal_num} into 1")
        print(f"Even Steps: {even_steps}, Odd Steps: {odd_steps}")
        print(f"Total Time: {elapsed_time:.4f}")
        break

    except OverflowError:
        print(bold + "The number is too large. Please try again." + reset)
    except Exception as e:
        print(bold + f"An error occurred: {e} Please try again." + reset)
    print()

input() # To keep window open after code finishes
