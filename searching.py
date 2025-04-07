import os

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, field):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """

    if field not in {"unordered_numbers","ordered_numbers","dna_sequence"}:
        return None

    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as json_file:
        seq = json_file.read()
        return seq

def linear_search(sequence, number):

    x=0
    counts = 0
    indices = []
    while x < len(sequence):
        if sequence[x] == number:
            indices.append(x)
            counts += 1
        print(sequence[x])
        x += 1
    return {"position": indices,"counts": counts}

def pattern_search(searched_seq, pattern):
    indices = set()
    pattern_size = len(pattern)

    left_idx = 0
    right_idx = pattern_size
    while right_idx < len(searched_seq):
        for idx in range(pattern_size):
            if pattern[idx] != searched_seq[left_idx + idx]:
                break
            else:
                indices.add()

def binary_search(sequence,number):

    while len(sequence) > 2:
        if number > sequence[len(sequence)/2]:
            low_sequence = sequence.append(sequence[0:len(sequence)/2])
def main():


    pass



if __name__ == '__main__':
    main()