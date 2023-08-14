from pattern_matcher import matcher_iter
from readfile import write_output_to_file

if __name__ == "__main__":
    print('Choose use case: ')
    print('1 --> Enter text to terminal')
    print('2 --> read from file')

    option = int(input('Enter no: '))
    print(option)
    text1 = None
    in_path = None

    if option == 1:
        text1 = input('Enter the string: ')
    elif option == 2:
        text1 = input('Enter file path: ')
    else:
        print("Invalid option.")
        exit(1)

    pattern1 = input('Enter pattern to be matched: ')

    if text1 is not None:
        if matcher_iter(text1, pattern1):
            print("The pattern was found in the text '{}'.".format(text1))
        else:
            print("The pattern was not found in the text '{}'.".format(text1))

    if in_path is not None:
        try:
            write_output_to_file(in_path, 'data/text.output', pattern1)
        except FileNotFoundError:
            print('File not found')
            exit(1)
        except Exception as e:
            print("An error occurred:", e)
            exit(1)
