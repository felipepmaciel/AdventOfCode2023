import os

dirname = os.path.dirname(__file__)
input_filename = os.path.join(dirname, "Q1_input.txt")
test_input_filename = os.path.join(dirname, "Q1_test_input.txt")

input_file = open(input_filename, "r")
test_input = open(test_input_filename, "r")

numeric_digits_in_string_format_list = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

named_numbers_list = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def string_number_to_string_digit(string_number):
    if string_number == "one":
        return "1"
    if string_number == "two":
        return "2"
    if string_number == "three":
        return "3"
    if string_number == "four":
        return "4"
    if string_number == "five":
        return "5"
    if string_number == "six":
        return "6"
    if string_number == "seven":
        return "7"
    if string_number == "eight":
        return "8"
    if string_number == "nine":
        return "9"


def get_line_first_numeric_value_index(line):
    index = -1
    for digit in line:
        index += 1
        if digit in numeric_digits_in_string_format_list:
            return index
    return -1


def get_line_first_or_last_string_value_index(
    line: str, first_or_last: str, named_numbers_list: list
):
    string_numbers = {
        number: line.find(number) if first_or_last == "first" else line.rfind(number)
        for number in named_numbers_list
    }
    string_numbers = {k: v for k, v in string_numbers.items() if v != -1}

    if string_numbers:
        occurrence_key = min if first_or_last == "first" else max
        occurrence_index = string_numbers[
            occurrence_key(string_numbers, key=string_numbers.get)
        ]
        return occurrence_index, occurrence_key(string_numbers, key=string_numbers.get)
    else:
        return -1, named_numbers_list[-1] if named_numbers_list else None


def calculate_file_calibration_value(file):
    file_sum = 0
    for line in file:
        index_of_first_digit_numeric = get_line_first_numeric_value_index(line)
        (
            index_of_first_digit_string,
            string_first_digit,
        ) = get_line_first_or_last_string_value_index(line, "first", named_numbers_list)
        index_of_last_digit_numeric = (
            (len(line) - get_line_first_numeric_value_index(line[::-1]) - 1)
            if get_line_first_numeric_value_index(line[::-1]) != -1
            else -1
        )
        (
            index_of_last_digit_string,
            string_last_digit,
        ) = get_line_first_or_last_string_value_index(line, "last", named_numbers_list)
        # so tem numerico
        if index_of_first_digit_numeric != -1 and index_of_first_digit_string == -1:
            first_digit = line[index_of_first_digit_numeric]
        # so tem string
        if index_of_first_digit_numeric == -1 and index_of_first_digit_string != -1:
            first_digit = string_number_to_string_digit(string_first_digit)
        # tem ambos
        if index_of_first_digit_numeric != -1 and index_of_last_digit_string != -1:
            if index_of_first_digit_numeric < index_of_first_digit_string:
                first_digit = line[index_of_first_digit_numeric]
            else:
                first_digit = string_number_to_string_digit(string_first_digit)
        # so tem numerico
        if index_of_last_digit_numeric != -1 and index_of_last_digit_string == -1:
            last_digit = line[index_of_last_digit_numeric]
        # so tem string
        if index_of_first_digit_numeric == -1 and index_of_last_digit_string != -1:
            last_digit = string_number_to_string_digit(string_last_digit)
        # tem ambos
        if index_of_last_digit_numeric != -1 and index_of_last_digit_string != -1:
            if index_of_last_digit_numeric > index_of_last_digit_string:
                last_digit = line[index_of_last_digit_numeric]
            else:
                last_digit = string_number_to_string_digit(string_last_digit)
        line_numeric_string = f"{first_digit + last_digit}"
        file_sum += int(line_numeric_string)
    return file_sum


print(calculate_file_calibration_value(test_input))
print(calculate_file_calibration_value(input_file))
