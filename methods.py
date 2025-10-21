def fibo(count: int):
    """Fibonachi.

    Return list of a few Fibonachi numbers"""
    fib_list = [0, 1]
    if count == 1:
        return [0]
    elif count == 2:
        return [0, 1]
    for i in range(2, count):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])
    return fib_list


def calc(*nums):
    """Calculate.

    Make somthing with numbers"""
    nums.count(2)


def main():
    llist = [1, 2, 2, 4]
    llist.append(5)
    print(*llist)
    calc(*llist)
    fib_list = fibo(10)
    print(*fib_list)
    fib_copy = fib_list.copy()
    i = id(fib_copy)
    d = id(fib_list)

    print(f"fib_copy.id {i}")
    print(f"fib_list.id {d}")


if __name__ == "__main__":
    main()
