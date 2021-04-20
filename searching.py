import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    file_path = os.path.join(cwd_path, file_name)

    if field not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    with open(file_path, "r") as json_file:
        dict = json.load(json_file)

    return dict[field]


def linear_search(seq, num):
    pos = []
    count = 0

    for idx in range(len(seq)):
        if seq[idx] == num:
            pos.append(idx)
            count += 1

    return {
        "positions": pos,
        "count": count
    }


def pattern_search(sequence, pattern):
    positions = set()
    pattern_size = len(pattern)
    left = 0
    right = pattern_size

    while right < len(sequence):
        for idx_pattern in range(pattern_size):
            if pattern[idx_pattern] != sequence[left+idx_pattern]:
                break
        else:
            positions.add(left+pattern_size // 2)

        left += 1
        right += 1
            # if sequence[idx:idx+pattern_size] == pattern:
            #     positions.add((idx + pattern_size) // 2)


    return positions


def binary_search(seq, number):
    left = 0
    right = len(seq) - 1

    while left <= right:
        middle = (left + right) // 2

        if seq[middle] == number:
            return seq[middle]

        if seq[middle] < number:
            left = middle + 1

        elif seq[middle] > number:
            right = middle - 1


    return None



def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    print(sequential_data)
    uno = linear_search(sequential_data, 9)
    print(uno)

    sequential_data = read_data("sequential.json", "dna_sequence")
    print(sequential_data)
    dos = pattern_search(sequential_data, "ATA")
    print(dos)

    sequential_data  =read_data("sequential.json", "ordered_numbers")
    print(sequential_data)
    tres = binary_search(sequential_data, 8)
    print(tres)

if __name__ == '__main__':
    main()