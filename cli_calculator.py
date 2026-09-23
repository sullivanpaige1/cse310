#!/usr/bin/env python3
"""A simple command-line calculator."""

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Perform a basic arithmetic calculation.")
    parser.add_argument("first", type=float, help="the first number")
    parser.add_argument(
        "operation",
        choices=("+", "-", "*", "/"),
        help="the arithmetic operation",
    )
    parser.add_argument("second", type=float, help="the second number")
    args = parser.parse_args()

    if args.operation == "+":
        result = args.first + args.second
    elif args.operation == "-":
        result = args.first - args.second
    elif args.operation == "*":
        result = args.first * args.second
    else:
        if args.second == 0:
            print("Error: cannot divide by zero.", file=sys.stderr)
            return 1
        result = args.first / args.second

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
