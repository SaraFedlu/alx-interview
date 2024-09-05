#!/usr/bin/python3


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.
    :param data: List of integers representing bytes.
    :return: True if data is a valid UTF-8 encoding, False otherwise.
    """
    # Number of bytes remaining in the current UTF-8 character
    bytes_to_process = 0

    # Masks to identify the pattern of bytes in UTF-8 encoding
    MASK_1_BYTE = 0b10000000  # Mask for 1 byte (0xxxxxxx)
    MASK_2_BYTE = 0b11100000  # Mask for 2 bytes (110xxxxx)
    MASK_3_BYTE = 0b11110000  # Mask for 3 bytes (1110xxxx)
    MASK_4_BYTE = 0b11111000  # Mask for 4 bytes (11110xxx)
    CONTINUATION_MASK = 0b11000000  # Mask for continuation byte (10xxxxxx)
    CONTINUATION_VALUE = 0b10000000  # Value to compare for continuation byte

    for byte in data:
        # Ensure we only deal with the least significant 8 bits
        byte &= 0xFF

        if bytes_to_process == 0:
            # Determine how many bytes this UTF-8 character spans
            if (byte & MASK_1_BYTE) == 0:
                # 1-byte character (ASCII, 0xxxxxxx)
                continue
            elif (byte & MASK_2_BYTE) == 0b11000000:
                # 2-byte character (110xxxxx)
                bytes_to_process = 1
            elif (byte & MASK_3_BYTE) == 0b11100000:
                # 3-byte character (1110xxxx)
                bytes_to_process = 2
            elif (byte & MASK_4_BYTE) == 0b11110000:
                # 4-byte character (11110xxx)
                bytes_to_process = 3
            else:
                # Invalid first byte
                return False
        else:
            # Check if it's a valid continuation byte (10xxxxxx)
            if (byte & CONTINUATION_MASK) != CONTINUATION_VALUE:
                return False
            bytes_to_process -= 1

    # If we have processed all bytes correctly, bytes_to_process should be 0
    return bytes_to_process == 0
