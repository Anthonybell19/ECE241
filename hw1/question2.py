class Hw1q2:
    def monomial(a: float, b: float, c: float):
        x = (c + 2 * b) / a
        return x

    def polynomial(a: float, b: float, c: float):
        x = (c**2 - 2 * b) / a
        return x
def main():
    a = float(input('input A '))
    b = float(input('input B '))
    c = float(input('input C '))
    # print(Hw1q2.monomial(a, b, c))
    print(Hw1q2.polynomial(a, b, c))


# __name__
if __name__ == "__main__":
    main()
