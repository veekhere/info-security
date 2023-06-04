from hashlib import md5, sha256
import bcrypt

data = [
    b"08122988399",
    b"nampoly2537",
    b"lasabre97",
    b"as534031",
    b"Victor_",
    b"16MSTF68AYSL",
    b"hhrules",
    b"cpt704242",
    b"gracemac",
    b"rayas123123",
]

salt = b"$2b$15$NSVH/I.9u1l/WoYUd/sSI."


def main():
    hashes = []
    for item in data:
        sha = sha256(item).hexdigest()
        md = md5(item).hexdigest()
        bc = bcrypt.hashpw(item, salt)

        hashes.append(sha)
        hashes.append(md)
        hashes.append(bc)

        print(
            f"\n{item}:\n\tsha256:\n\t\t{sha}\n\tmd5:\n\t\t{md}\n\tbcrypt:\n\t\t{bc}\n"
        )


main()
