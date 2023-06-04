from sys import argv

flags = {
    "decode": "-d"
}

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def caesar(path_to_file: str, shift: int = 0, decode = False):
    shift = (32 - (shift % 32)) if decode else (shift % 32)
    msg = list(read_file(path_to_file))

    for i, letter in enumerate(msg):
        if (letter < 'А' or letter > 'я'):
            continue

        tmp = ord(letter) + shift
        if (tmp > ord('Я') and letter <= 'Я' or tmp > ord('я') and letter <= 'я'):
            msg[i] = chr(tmp - 32)
        else:
            msg[i] = chr(tmp)

    write_file(get_new_file_path(path_to_file, "decoded" if decode else "encoded"), ''.join(msg))

def check_flag(flag_key: str):
    return flags.get(flag_key) in argv[1:]

def write_file(file: str, data: str, force = False):
    try:
        with open(file, 'w+' if force else 'x') as file_d:
            file_d.write(data)
            file_d.close()
    except FileExistsError:
        print(f"{colors.FAIL}Error:{colors.ENDC} File {colors.UNDERLINE}({file}){colors.ENDC} already exists")
        answer = input(f"{colors.OKCYAN}Overwrite?{colors.ENDC} {colors.OKGREEN}[y/N]{colors.ENDC}\n")
        if (answer.lower() == 'y'):
            write_file(file, data, True)
        else:
            return


def read_file(file: str):
    buffer = ""
    try:
        with open(file, 'r') as file_d:
            buffer = file_d.read()
            file_d.close()
    except FileNotFoundError:
        print(f"{colors.FAIL}Error:{colors.ENDC} File ({file}) is not found")

    return buffer

def get_new_file_path(path: str, prefix: str):
    arr = path.split('/')
    arr[len(arr) - 1] = f"{prefix}-{arr[len(arr) - 1]}"
    return '/'.join(arr)
