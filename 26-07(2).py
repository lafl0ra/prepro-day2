"""Talubmad"""
def main():
    """Find kwam yaw"""
    kyt = int(input())
    number = 0
    if kyt == 0:
        print("No Tape Measure")
    else:
        while True:
            num1 = input()
            if num1 == "No more!":
                break
            elif int(num1) <= kyt:
                number += int(num1)
        if number == 0:
            print("Not Found Number")
        else:
            print("Sum of Found Number = %d" %number)
main()
