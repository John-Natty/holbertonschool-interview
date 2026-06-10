#!/usr/bin/python3
"""UTF-8 Validation Module."""


def validUTF8(data):
    """Determine if a data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers representing bytes.

    Returns:
        bool: True if data is valid UTF-8, False otherwise.
    """
    num_bytes = 0

    for byte in data:
        # Keep only the 8 least significant bits of the integer.
        byte &= 0xFF

        # If we are not waiting for continuation bytes,
        # this byte must start a new UTF-8 character.
        if num_bytes == 0:
            # A 2-byte character starts with 110xxxxx.
            if (byte >> 5) == 0b110:
                num_bytes = 1

            # A 3-byte character starts with 1110xxxx.
            elif (byte >> 4) == 0b1110:
                num_bytes = 2

            # A 4-byte character starts with 11110xxx.
            elif (byte >> 3) == 0b11110:
                num_bytes = 3

            # A 1-byte character starts with 0xxxxxxx.
            elif (byte >> 7) == 0:
                continue

            # Any other pattern is invalid.
            else:
                return False

        else:
            # A continuation byte must start with 10xxxxxx.
            if (byte >> 6) != 0b10:
                return False

            # One expected continuation byte has been found.
            num_bytes -= 1

    # The data is valid only if no continuation byte is missing.
    return num_bytes == 0
