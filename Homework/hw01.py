import doctest

_author_ = "Sidath Marapane"
_credits_ = ["Your list of helpers"]
_email_ = "marapash@mail.uc.edu"


# Returns given fraction (n/d) as sum of unit fractions without repetition
def egypt(n, d):
    """
    >>> egypt(7,10)
    1/2 + 1/5 = 7/10
    >>> egypt(3,4)
    1/2 + 1/4 = 3/4
    >>> egypt(11,12)
    1/2 + 1/3 + 1/12 = 11/12
    """

    list_of_fractions = []
    sumfraction = round(n / d, 7)
    unit = 1

    # loop until sum of unit fractions = n/d
    # if n/d - 1/unit is positive or 0, add unit to list_of_fractions
    while True:
        unit = unit + 1
        if(round(sumfraction - 1/unit, 7) > 0 or round(sumfraction - 1/unit, 7) == 0):
            sumfraction = round(sumfraction - 1/unit, 10)
            list_of_fractions.append(unit)

            # if n/d - 1/unit is small enough, break the loop
            # this is due to floating point arithmetic inconsistencies
            if(abs(sumfraction) < 1.0e-7):
                break

    final_list = ""

    # append the 1/unit to the string in the designated format
    for num in list_of_fractions:
        final_list = final_list + f"1/{num} + "

    # remove extra + sign, append n/d, and print string
    final_list = final_list[:-2]
    print(final_list + f"= {n}/{d}")


if __name__ == "__main__":
    doctest.testmod(verbose=True)
