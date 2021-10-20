# Note: This program asks the user for a positive integer and determines if the integer is in the Fibonacci Sequence
# Very simple program


def main():
    """Runs the Fibonacci Determinant Program"""
    print("Welcome to the Fibonacci Determinant Program")
    print("This program determines if the positive integer chosen by you, the user, is in Fibonacci Sequence")
    num = input("Please input your a positive integer:  ")
    if check_if_in_fib(int(num)):
        return print("{} is in the Fibonacci Sequence".format(int(num)))
    else:
        return print("{} is not in the Fibonacci Sequence".format(int(num)))


def check_if_in_fib(n):
    """Returns True if an integer is in Fibonacci Sequence, otherwise returns False"""
    prev, next_ = 0, 1
    if n == prev:
        return True
    while next_ <= n:
        if next_ == n:
            return True
        next_next = prev + next_
        prev, next_ = next_, next_next
    return False

main()
