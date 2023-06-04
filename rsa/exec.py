from core import *


def main():
    p = get_p()
    q = get_q()
    n = p * q
    euler = calc_euler(p, q)
    public_key = get_public_key(euler)
    private_key = get_private_key(public_key, euler)
    message = "Привет"
    encoded_msg = encode(message, public_key, n)
    decoded_msg = decode(encoded_msg, private_key, n)

    print(
        f'\np:\t\t{p}\nq:\t\t{q}\nn:\t\t{n}\neuler:\t\t{euler}\npbkey:\t\t{public_key}\nprkey:\t\t{private_key}\n\nmessage:\t"{message}"\nencoded:\t{encoded_msg}\ndecoded:\t"{decoded_msg}"'
    )


main()
