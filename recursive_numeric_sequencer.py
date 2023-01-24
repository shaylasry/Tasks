
def count_max_elements(stream, max_element, count):
    element = next(stream)

    if element == 0:
        return (max_element, count)

    if max_element is None or element > max_element:
        max_element = element
        count = 1
    elif element == max_element:
        count += 1
    return count_max_elements(stream, max_element, count)


if __name__ == '__main__':
    example_tuple = ( 1 ,5 ,42, -376, 5, 19, 5, 3, 42, 2, 0)
    stream = iter(example_tuple)
    print(count_max_elements(stream, None, 0))