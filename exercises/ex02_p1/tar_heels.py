"""Tar Heels exercise redux as a structured program."""

__author__ = "730368118"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    z: str = (tar_heels(choice))
    print(z)


def tar_heels(UNC: int) -> str:
    if UNC % 7 == 0 and UNC % 2 == 0:
        return("TAR HEELS")
    else:
        if UNC % 7 == 0:
            return("HEELS")
        else:
            if UNC % 2 == 0:
                return("TAR")
            else:
                return("CAROLINA")


if __name__ == "__main__":
    main()
