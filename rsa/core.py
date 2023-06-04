from secrets import randbelow
from sympy import prevprime
from hashlib import md5
import threading
from numpy import full
import time


def gcd(a: int, b: int):
    while b:
        a, b = b, a % b
    return a


def calc_euler(p: int, q: int):
    return (p - 1) * (q - 1)


def current_milli_time():
    return round(time.time() * 1000)


def get_p():
    return prevprime(randbelow(2**8))


def get_q():
    _ = md5(bytes(str(get_p()), "UTF-8")).hexdigest()
    byte_list = list(bytes(_, "UTF-8"))
    tmp = byte_list[: round(len(byte_list) / 32)]
    return prevprime(int("".join(str(i) for i in tmp)) * 3)


def get_public_key(euler: int):
    e = 1 + randbelow(euler)  # equivalent to 1 < x ≤ 𝜑(n)

    while gcd(e, euler) != 1:
        e = 1 + randbelow(euler)

    return e


def worker(public_key: int, euler: int, inc: int, init: list):
    d = round(get_public_key(euler) / 32)

    while int(init[0]) == 0:
        while (public_key * d) % euler != 1 and int(init[0]) == 0:
            d += inc
        if (public_key * d) % euler == 1:
            init[0] = str(d)


def get_private_key(public_key: int, euler: int):
    d = ["0"]

    thread1 = threading.Thread(target=worker, args=(public_key, euler, +1, d))
    thread2 = threading.Thread(target=worker, args=(public_key, euler, -1, d))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    return abs(int(d[0]))


def chunks(lst: list, n: int):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def parse_message(message: str):
    parsed_message = ""

    for c in message:
        _ = str(oct(ord(c))[2:])

        zeros = full(8 - len(_), "0")
        parsed_message += "".join(zeros) + _

    return parsed_message


def encode(message: str, public_key: int, n: int):
    parsed_message = parse_message(message)
    enc_message = []

    for c in parsed_message:
        enc_message.append((int(c) ** public_key) % n)

    hexed = bytes("-".join(str(i) for i in enc_message), "UTF-8").hex()

    return hexed


def decode(message: str, private_key: int, n: int):
    enc_message = bytes.fromhex(message).decode("UTF-8").split("-")
    init_message = []
    buff = []

    for i in enc_message:
        buff.append((int(i) ** private_key) % n)

    msg_chunks = list(chunks(buff, 8))
    for chunk in msg_chunks:
        _ = "".join(str(x) for x in chunk)
        init_message.append(chr(int(_, 8)))

    return "".join(init_message)
