"""Using bitmask, we can save memory by not using 4 byte variable to save
the flag"""


def bitmask():

    # define flag variable
    flag = 0

    # set first bit
    flag |= 1

    # set second bit
    flag |= 2

    # set third bit
    flag |= 4

    # check bit
    if flag & 4:
        print('bit set')
    else:
        print('bit not set')

    # unset the 3 bit
    flag = flag ^ 4
