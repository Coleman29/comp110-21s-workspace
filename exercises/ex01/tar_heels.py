"""An exercise in remainders and boolean logic."""

__author__ = "730368118"


favorite = int(input("Whats your favorite interger: "))
if favorite % 7 == 0 and favorite % 2 == 0:
    print("TAR HEELS")
else:
    if favorite % 7 == 0:
        print("HELLS")
    else:
        if favorite % 2 == 0:
            print("TAR")
        else:
            print("CAROLINA")
