#Q2
#    to denote asymptotic time complexity use the following notation
#    O(n) O(m) O(a) O(b)
# e.g. traversing through n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] is O(n)

#1
def append():
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = [15, 16, 17, 18]

    for m_i in m:
        n.append(m_i)

    print("n:{}".format(m))

#2
def merge():
    n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    m = [15, 16, 17, 18]
    nm = []

    for n_i in n:
        nm.append(n_i)

    for m_i in m:
        nm.append(m_i)

    print("nm:{}".format(nm))

#3
def normalize():
    n = [8, 3, 5, 6, 7, 2, 4, 9, 1]
    nn = []

    sum = 0
    for i in n:
        sum += i
    avg = sum / len(n)
    for i in n:
        nn.append(i - avg)

    print("n:{}".format(n))
    print("nn:{}".format(nn))

#4
def go_through():

    n = 10
    nm = []

    while n > 0:
        nm.append(n)
        n=int(n/2)

    print("nm:{}".format(nm))

#5
def go_through_two():
    n = 10
    m = 5
    nm = []

    while n > 0:

        nm.append(n)
        n = int(n/2)

        m1=1
        while m1*m1 <= m:
            print("in")
            nm.append(m1)
            m1 +=1

    print("nm:{}".format(nm))

#6
def times():
    a=100
    b=5
    sum=b
    count=0
    while sum<=a:
        sum+=b
        count+=1

    print("count:{}".format(count))


if __name__ == "__main__":
    append()
    merge()
    normalize()
    go_through()
    go_through_two()
    times()