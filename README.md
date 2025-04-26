# Simple Python Caesar Cipher Tool

A simple command-line tool for encrypting and decrypting text using the Caesar cipher algorithm.

## Description

This tool allows you to encrypt or decrypt text files using the classic Caesar cipher, one of the simplest and most widely known encryption techniques. Named after Julius Caesar, who used it to communicate with his generals, the cipher works by shifting letters in the alphabet by a specified number of positions.

## Features

- Encrypt plaintext files using a specified shift value
- Decrypt previously encrypted files when you know the shift value
- Process text while preserving non-alphabetic characters (spaces, numbers, punctuation)
- Output results to a file or display them in the terminal

## Usage

### Basic Usage

```bash
python caesar_cipher.py filename [options]
```

### Options

- `-e, --encrypt`: Encrypt the input file
- `-d, --decrypt`: Decrypt the input file
- `-s, --shift SHIFT`: Specify the shift value (required)
- `-o, --output FILENAME`: Write output to a file instead of displaying it

### Examples

Encrypt a file with a shift of 3 and display the result:

```bash
python caesar_cipher.py message.txt -e -s 3
```

Decrypt a file with a shift of 3 and save to a new file:

```bash
python caesar_cipher.py encrypted_message.txt -d -s 3 -o decrypted_message.txt
```

## How It Works

The Caesar cipher works by replacing each letter in the plaintext with a letter some fixed number of positions down the alphabet. For example, with a shift of 3:

- A becomes D
- B becomes E
- Z wraps around to C

Non-alphabetic characters remain unchanged.

## Limitations

- The Caesar cipher is a very basic encryption method and not secure for sensitive information
- Both parties need to know the shift value to encrypt/decrypt messages
