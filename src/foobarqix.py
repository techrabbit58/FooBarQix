divisors = {
    3: "Foo",
    5: "Bar",
    7: "Qix",
}


def foo_bar_qix(number: int) -> str:
    if type(number) != int or number <= 0:
        raise ValueError(
            f"foo_bar_qix: argument must be a positive integer, but {number} is not")
    result = []
    for divisor, word in divisors.items():
        if number % divisor == 0:
            result.append(word)
    number_as_text = str(number)
    for char in number_as_text:
        replacement = "*" if char == "0" and result else divisors.get(int(char))
        if replacement is not None:
            result.append(replacement)
    if not result:
        for char in number_as_text:
            result.append("*" if char == "0" else char)
    return ''.join(result)