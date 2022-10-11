def factorial01(n):
    if n == 0:
        return 1

    return n * factorial01(n - 1)
