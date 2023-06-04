from sys import argv
from core import check_flag, caesar, colors

def exec():
    if (len(argv[1:]) < 2):
        print(f"{colors.FAIL}Error:{colors.ENDC} Not enough arguments")
        return

    path_to_file = argv[1]
    shift: int
    is_decode = check_flag("decode")

    try:
        shift = int(argv[2])
    except ValueError:
        print(f"{colors.FAIL}Error:{colors.ENDC} Incorrect shift value")
        return

    caesar(path_to_file, shift, is_decode)

exec()
