import sys


def fac(num):
    return 1 if num == 0 else num * fac(num - 1)


def main():
    print(fac(59996))


if __name__ == '__main__':
    sys.setrecursionlimit(60000)
    main()
# for i in range(1000):
#     print(f'{i}:'.rjust(3), fac(i))

