def plusOne(digits: list[int]) -> list[int]:
    # turn it into integer
    total = 0
    multiplier = 1
    for val in digits[::-1]:
        total += (val * multiplier)
        multiplier *= 10

    # print(total)
    # increment by one
    total += 1

    # turn it back into list
    total_as_string = str(total)
    total_as_string_as_list: list[str] = list(total_as_string)

    local_array: list[int] = []
    for val in total_as_string_as_list:
        local_array.append(int(val))

    return local_array


def main() -> None:
    assert (plusOne([1, 2, 3]) == [1, 2, 4])
    assert (plusOne([4, 3, 2, 1]) == [4, 3, 2, 2])
    assert (plusOne([9]) == [1, 0])
    print("all tests passed!")


if __name__ == '__main__':
    main()
