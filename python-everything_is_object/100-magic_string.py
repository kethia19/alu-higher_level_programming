#!/usr/bin/python3
def magic_string(n=0):
    return "Holberton" * (n + 1) if n == 0 else ", ".join(["Holberton"] * (n + 1))
