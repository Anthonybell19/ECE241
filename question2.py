class Hw1q2:
    def monomial(a: float, b: float, c: float):
        x = (c + 2 * b) / a
        return x

    def polynomial(a: float, b: float, c: float):
        x = (c**2 - 2 * b) / a
        return x
def main():
    print(Hw1q2.monomial(1, 1, 4))
    print(Hw1q2.polynomial(1, 1, 4))


# __name__
if __name__ == "__main__":
    main()