# File: 1.6-chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("The program illustrates a chaotic function")
    x = eval(input("Enter the first number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range (n):
        x = 3.9 * x * (1-x)
        print(x)

main()
