"""
Title: Mod 26
Category: cryptography

Description: Cryptography can be easy, do you know what ROT13 is?
Solution author: kodemakerDor
"""

import string


def find_letter(alphabet: str, letter: str):
    char = alphabet.find(letter)
    possition = char - 13
    if possition < 0:
        possition += len(alphabet)
    response = alphabet[possition]
    return response


def decypher_rot_13(cypher_text: str) -> str:
    result = ""
    lower_alphabet = string.ascii_lowercase
    upper_alphabet = string.ascii_uppercase

    for letter in cypher_text:
        if letter not in lower_alphabet and letter not in upper_alphabet:
            result += letter
        elif letter in lower_alphabet:
            result += find_letter(lower_alphabet, letter)
        elif letter in upper_alphabet:
            result += find_letter(upper_alphabet, letter)
    return result


def test_cases() -> bool:
    assert "fabian" == decypher_rot_13("snovna")
    assert "Abraham" == decypher_rot_13("Noenunz")
    assert "picoCTF{next_time_I'll_try_2_rounds_of_rot13_Aphnytiq}" == decypher_rot_13("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_Ncualgvd}")


def main():
    test_cases()

main()