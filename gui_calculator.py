#!/usr/bin/env python3
"""A simple graphical calculator built with Tkinter."""

import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, window: tk.Tk) -> None:
        self.window = window
        self.window.title("Calculator")
        self.window.resizable(False, False)

        self.expression = tk.StringVar()
        display = tk.Entry(
            window,
            textvariable=self.expression,
            justify="right",
            font=("Arial", 22),
            state="readonly",
            readonlybackground="white",
            width=15,
        )
        display.grid(row=0, column=0, columnspan=4, padx=8, pady=8)

        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
        ]

        for label, row, column in buttons:
            tk.Button(
                window,
                text=label,
                width=5,
                height=2,
                font=("Arial", 14),
                command=lambda value=label: self.press(value),
            ).grid(row=row, column=column, padx=3, pady=3)

        tk.Button(
            window,
            text="=",
            width=23,
            height=2,
            font=("Arial", 14),
            command=self.calculate,
        ).grid(row=5, column=0, columnspan=4, padx=3, pady=5)

    def press(self, value: str) -> None:
        if value == "C":
            self.expression.set("")
        else:
            self.expression.set(self.expression.get() + value)

    def calculate(self) -> None:
        try:
            # Input is restricted to calculator buttons, but eval is still
            # limited to arithmetic characters for an extra safety check.
            expression = self.expression.get()
            if not expression or any(char not in "0123456789.+-*/() " for char in expression):
                raise ValueError
            result = eval(expression, {"__builtins__": {}}, {})
            self.expression.set(str(result))
        except (ArithmeticError, SyntaxError, ValueError):
            messagebox.showerror("Invalid calculation", "Please enter a valid expression.")
            self.expression.set("")


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
