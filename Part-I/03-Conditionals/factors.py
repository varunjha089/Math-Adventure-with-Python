def factors(nums):
    """
    param nums: takes a number
    :return: A list of factors
    """
    factorList = []
    for i in range(1, nums + 1):
        if nums % i == 0:
            factorList.append(i)
    return factorList


if __name__ == "__main__":
    print(factors(int(input("Please Enter a Number: "))))
