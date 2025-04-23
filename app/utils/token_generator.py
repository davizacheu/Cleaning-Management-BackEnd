# app/utils/token_generator.py
import secrets


def generate_token_str(length=32):
    return secrets.token_hex(length)