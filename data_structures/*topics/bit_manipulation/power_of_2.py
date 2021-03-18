"""Checking if given 32 bit integer number is power of 2"""


def find_power_of_2(num):
    """
    All power of 2 have only single bit set e.g. 16(00010000)
    If we minus 1 from this, all the bits from LSB to set bit get
    toggled., i.e 16-1 = 15 (00001111). Now, if we AND x and x-1
    and result is 0, x is power of 2 else not.
    """
    if num & (num - 1):
        return False
    return True


print(find_power_of_2(15))
