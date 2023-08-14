from pattern_matcher import matcher


def read_and_split_txt_file(file_path):
    """
    Read file at given location and iterate through the file word by word
    :param file_path: path to file
    :return: list of words in file or empty list
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            return words
    except FileNotFoundError:
        print("File not found.")
        return []
    except Exception as e:
        print("An error occurred:", e)
        return []


def write_output_to_file(in_path, out_path, pattern):
    """
    Function to check pattern word by word in file at in_path and create a file of boolean values ay out_path
    :param in_path: path to file
    :param out_path: path to output file
    :param pattern: pattern to match words in input file
    :return: True or exception
    """
    word_array = read_and_split_txt_file(in_path)
    try:
        with open(out_path, 'w') as file:
            for word in word_array:
                res = matcher(word, pattern)
                file.write(str(res) + "\n")
        print("Output written to", out_path)
        return True
    except Exception as e:
        print("An error occurred:", e)
        return e
