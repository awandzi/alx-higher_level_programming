#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
   from sys  import argv

    sumint = 0
    for i in range(1, len(argv)):
        sumint += int(argv[i])
    print("{}".format(sumint))

