import argparse
import string

alphabet = string.ascii_letters


def parse_file(filename: str) -> str:
    """Parse text from the input file"""

    with open(filename, "r", encoding="utf-8") as file:
        file_contents = file.read()

    return file_contents


def encrypt(plaintext: str, shift: int) -> str:
    "Encrytps plaintext with using the given shift"

    encrypted_text = ""

    for char in plaintext:
        if char.isalpha():
            # encrypted_char_position = (char_position + shift) mod len(alphabet) - equation for encryption
            encrypted_char_position = (alphabet.index(char) + shift) % len(alphabet)
            encrypted_text += alphabet[encrypted_char_position]
            continue
        encrypted_text += char

    return encrypted_text


def decrypt(encrypted_text: str, shift: int) -> str:
    "Decrypts encrypted text using the given shift"

    decrypted_text = ""

    for char in encrypted_text:
        if char.isalpha():
            # decrypted_char_position = (char_position - shift) mod len(alphabet) - equation for decryption
            decrypted_cahr_position = (alphabet.index(char) - shift) % len(alphabet)
            decrypted_text += alphabet[decrypted_cahr_position]
            continue
        decrypted_text += char

    return decrypted_text


def write_to_file(text: str, filename: str) -> None:
    "Write encrypted/decrypted text to a file"

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)


def main():
    # file, or text
    # left shift or right shift ammount

    # Parse comand-line arguments
    parser = argparse.ArgumentParser(
        description="Simple tool to encrypt plain text that is in a file using a Caesar cipher"
    )

    parser.add_argument("filename", help="Plaintext file to encrypt.")
    parser.add_argument(
        "-s",
        "--shift",
        type=int,
        help="Shift to use for the cipher. Positive number for a left shift and negative number for a right shift",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Name of output file. If omitted, output is dsiplayed on the standard output",
    )
    parser.add_argument(
        "-d",
        "--decrypt",
        action="store_true",
        help="Decrypt mode. Only one mode can be used at a time.",
    )
    parser.add_argument(
        "-e",
        "--encrypt",
        action="store_true",
        help="Encrypt mode. Only one mode can be used at a time.",
    )

    args = parser.parse_args()

    input_file = args.filename
    output_file = args.output
    is_decrypt_mode = args.decrypt
    is_encrypt_mode = args.encrypt
    shift = args.shift

    # Hanlde user specifying both modes
    if is_decrypt_mode and is_encrypt_mode:
        print("Please specify only one mode.")
        return

    input_text = parse_file(input_file)

    if is_encrypt_mode:
        encrypted_text = encrypt(input_text, shift)
        if output_file:
            write_to_file(encrypted_text, output_file)
            return
        print(encrypted_text)

    if is_decrypt_mode:
        decrypted_text = decrypt(input_text, shift)
        if output_file:
            write_to_file(decrypted_text, output_file)
            return
        print(decrypted_text)


if __name__ == "__main__":
    main()
