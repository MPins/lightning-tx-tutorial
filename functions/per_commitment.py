from functions.hashfunctions import *

# Flip the (bit_index % 8) bit of the (bit_index // 8) byte in value.
def flip_bit(value: bytearray, bit_index: int):
    byte_index = bit_index // 8  # Get the byte index
    bit_position = bit_index % 8  # Get the bit position within the byte
    value[byte_index] ^= (1 << bit_position)  # Flip the bit using XOR

# Generate a derived value P from a seed and an integer I
# param seed: 32-byte initial seed.
# param I: Index whose set bits determine which bits in P get flipped.
# return: 32-byte derived value P.
def generate_from_seed(seed: bytes, I: int) -> bytes:
    P = bytearray(seed)  # Convert to mutable bytearray

    for B in range(47, -1, -1):  # Iterate from 47 down to 0
        if (I & (1 << B)) != 0:  # Check if bit B is set in I
            flip_bit(P, B)  # Flip the corresponding bit in P
            P = bytearray(sha256(P))  # Hash P and convert back to bytearray

    return bytes(P)  # Convert back to bytes before returning

