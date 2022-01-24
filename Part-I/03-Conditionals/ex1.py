import time


def factors(nums1, nums2):
    """
    :param nums1: takes a number
    :param nums2: takes another number
    :return: GCF of two numbers
    """
    factorList = nums1 % nums2
    # print(f"The value of nums1 is {nums1} and the value of nums2 is {nums2} and factorList is {factorList}")
    # print()
    if factorList == 0:
        print(nums2)
    else:
        factors(nums2, factorList)


if __name__ == "__main__":
    num1 = int(input("Enter the number: "))
    num2 = int(input("Enter another number: "))

    factors(num1, num2)
