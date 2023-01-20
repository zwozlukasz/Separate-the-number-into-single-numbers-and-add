input_value = input("Put input number").replace(',', '.')
part_1 = 0
part_2 = 0
result_part_1 = 0
result_part_2 = 0


def count_numbers(input_string: str):
    result = 0
    for element in input_string:
        print(f"znak: {element}")
        if element.isprintable() and element.isnumeric():
            result += int(element)
    return result


def is_float_number(input_str: str):
    return '.' in input_str


def generate_results(input_str: str, input_str_part_1: str, input_str_part_2: str):
    global result_part_1
    global result_part_2
    if is_float_number(input_str):
        result_part_1 = count_numbers(input_str_part_1)
        result_part_2 = count_numbers(input_str_part_2)
    else:
        result_part_1 = count_numbers(input_str_part_1)


def print_results(input_str: str):
    if is_float_number(input_str):
        print(f"suma to: {result_part_1}.{result_part_2}")
    else:
        print(f"suma to: {result_part_1}")


def split_input_value(input_str: str):
    global part_1
    global part_2
    if is_float_number(input_str):
        part_1 = input_str.split('.')[0]
        part_2 = input_str.split('.')[1]
    else:
        part_1 = input_str
    return {part_1: part_1,
            part_2: part_2
            }


split_input_value(input_value)

generate_results(input_value, part_1, part_2)

print_results(input_value)
