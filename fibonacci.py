# fibonacci sequence is the sum of the 2 previous number to create the next number in sequence
# ig [0,1,1] => 1+1=2 , new list=[0,1,1,2] 

def fibonacci(len):
    # List that will contain the Fibonacci sequence
    fibonacci_sequence = []
    
    # starting numbers, you need minimum of 2 number to make a fibonacci sequence
    num1 = 0
    num2 = 1
    
    # adding to the fibonacci list
    fibonacci_sequence.append(num1)
    fibonacci_sequence.append(num2)

    # the length of the fibonacci list made user, to choose length
    total_nums = len - 2 # subtracted 2 becuase we already have the first 2 numbers

    for number in range(total_nums):
        next = num1 + num2
        fibonacci_sequence.append(next)
        num1 = fibonacci_sequence[-2] # updating num1 to be the second last number in list  
        num2 = fibonacci_sequence[-1] # updating num2 to be the last number in list 
    print(fibonacci_sequence)


tot_num_in_sequence = int(input("Input length of Squence: "))
fibonacci(tot_num_in_sequence)
