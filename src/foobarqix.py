divisors = {
    3: "Foo",
    5: "Bar",
    7: "Qix",
}


def foo_bar_qix(number: int) -> str:

    # work only on positive integer numbers, reject everything else
    # and raise a value error on reject
    if type(number) != int or number <= 0:
        raise ValueError(
            f"foo_bar_qix: argument must be a positive integer, but {number} is not")

    # at this point, the given number can be processed by definition
    ordered_results = []

    # first, try to substitute the whole number if it is divisible by one of the divisors
    for divisor, word in divisors.items():
        if number % divisor == 0:
            ordered_results.append(word)

    # substitute all filterable digits by their replacement, obey digit order
    # and drop digits that cannot be replaced
    digits = str(number)
    for char in digits:
        replacement = "*" if char == "0" and ordered_results else divisors.get(int(char))
        if replacement is not None:
            ordered_results.append(replacement)

    # if no replacement so far, return the given number as string (step 2: replace zeros)
    if not ordered_results:
        for char in digits:
            ordered_results.append("*" if char == "0" else char)

    return ''.join(ordered_results)
