import pytest

from foobarqix import foo_bar_qix


@pytest.mark.parametrize("number", [-1, 0])
def test_foobarqix_with_nonpositive_number(number):
    with pytest.raises(ValueError, match=str(number)):
        foo_bar_qix(number)


def test_foobarqix_with_non_integer():
    with pytest.raises(ValueError, match=str(3.0)):
        # noinspection PyTypeChecker
        foo_bar_qix(3.)


@pytest.mark.parametrize("actual_number, expected_result", [
    (1, "1"),
    (2, "2"),
    (3, "FooFoo"),  # divisible by 3, contains 3
    (4, "4"),
    (5, "BarBar"),  # divisible by 5, contains 5
    (6, "Foo"),  # divisible by 3
    (7, "QixQix"),  # divisible by 7, contains 7
    (8, "8"),
    (9, "Foo"),  # divisible by 3
    (10, "Bar*"),  # divisible by 5
    (11, "11"),
    (12, "Foo"),  # divisible by 3
    (13, "Foo"),  # contains 3
    (14, "Qix"),  # divisible by 7
    (15, "FooBarBar"),  # divisible by 3 and 5, contains 5
    (16, "16"),
    (17, "Qix"),  # contains 7
    (18, "Foo"),  # divisible by 3
    (19, "19"),
    (20, "Bar*"),  # divisible by 5
    (21, "FooQix"),  # divisible by 3 and 7
    (33, "FooFooFoo"),  # divisible by 3, contains two 3
    (51, "FooBar"),  # divisible by 3, contains 5
    (53, "BarFoo"),  # contains 5 followed by 3
    (101, "1*1"),  # step 2: show all zeros as "*", obey digit position
    (105, "FooBarQix*Bar"),  # step 2: divisible by 3, 5 and 7, contains zero and 5
    (303, "FooFoo*Foo"),  # step 2: divisible by 3, two 3 with zero in between
    (357, "FooQixFooBarQix"),  # divisible by 3 and 7, contains 3, 5, 7
    (375, "FooBarFooQixBar"),  # divisible by 3 and 5, contains 3, 5 and 7
    (537, "FooBarFooQix"),  # divisible by 3, contains 3, 5, 7
    (573, "FooBarQixFoo"),  # divisible by 3, contains 3, 5, 7
    (735, "FooBarQixQixFooBar"),  # divisible by all three, contains all three
    (753, "FooQixBarFoo"),  # divisible by 3, contains all three
    (10005, "FooBar***Bar"),  # divisible by 3 and 5, contains three zeros and one 5
    (10019, "1**19"),  # contains two zeros
    (10101, "FooQix**"),  # step 2: divisible by 3 and 7, conteins two zeros
    (15703, "BarQix*Foo"),  # step 2: contains all three and zero
    (30705, "FooBarFoo*Qix*Bar"),  # step 2: divisible by 3 and 5, contains all
])
def test_foobarquix_with_valid_numbers(actual_number, expected_result):
    assert foo_bar_qix(actual_number) == expected_result
