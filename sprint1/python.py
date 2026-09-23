"""Read input from the command line and write output to the command line."""


def main() -> None:
    name = input("baka: ").strip()

    if name:
        print(f"baka, {name}!")
    else:
        print("baka, World!")


if __name__ == "__main__":
    main()
