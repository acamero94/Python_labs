# Лабораторная работа №3

import random


class GammaEncryptor(object):
    BYTE_MAX = 255

    def __init__(self):
        self.rng = random.SystemRandom()

    @staticmethod
    def xor(ba1, ba2):
        return [b1 ^ b2 for b1, b2 in zip(ba1, ba2)]

    def encrypt(self, message, key):
        res = self._execute_round(message, key)
        return res

    def decrypt(self, message, key):
        res = self.encrypt(message, key)
        return res

    def _execute_round(self, message, key):
        if isinstance(message, str):
            message = message.encode()
        if isinstance(key, str):
            key = key.encode()

        if len(key) < len(message):
            raise ValueError(
                    "The key should be at least as long as the message."
                )
        return self.xor(message, key)

    def get_key_for_message(self, message):
        return [self.rng.randint(0, self.BYTE_MAX) for _ in message.encode()]


def print_process(msg_in, key, msg_out, process):
    print(
        "Process: {}\n"
        "Input:   {}\n"
        "Key:     {}\n"
        "Output:  {}\n"
        .format(
            process, msg_in, key, msg_out
        )
    )


def main():
    # Task 01: substitution cipher
    plaintext = "Gaby is working now in this computer."
    key = {
        "a": "w",
        "b": "x",
        "c": "y",
        "d": "z",
        "e": "a",
        "f": "b",
        "g": "c",
        "h": "d",
        "i": "e",
        "j": "f",
        "k": "g",
        "l": "h",
        "m": "i",
        "n": "j",
        "o": "k",
        "p": "l",
        "q": "m",
        "r": "n",
        "s": "o",
        "t": "p",
        "u": "q",
        "v": "r",
        "w": "s",
        "x": "t",
        "y": "u",
        "z": "v",
        " ": "0",
        ".": ",",
    }


    ge = GammaEncryptor()
    key = ge.get_key_for_message(plaintext)
    ciphertext = ge.encrypt(plaintext, key)
    print_process(plaintext, key, ciphertext, process="Encryption")

    decrypted = ge.decrypt(ciphertext, key)
    print_process(ciphertext, key, "".join(map(chr, decrypted)), process="Decryption")

if __name__ == "__main__":
    main()