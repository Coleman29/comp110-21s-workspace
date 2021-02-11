"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730368118"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    x = (randint(1, 30))
    if x >= 16:
        return("You will discover new riches")
    else:
        if x == 15:
            return("You will recieve everything you ever wanted")
        else:
            if x != 14:
                return("You get three wishes provided by a genie")
            else:
                return("You will be blessed with good vibes for a week")



# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
