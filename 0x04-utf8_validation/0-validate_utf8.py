#!/usr/bin/python3
def validUTF8(data):
    """Determines if a given data set represents a valid UTF-8 encoding."""
    n_bytes = 0

    # Masks to check leading bits in a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Only use the 8 least significant bits of the integer
        byte &= 0xFF

        if n_bytes == 0:
            # Determine the number of bytes for the current UTF-8 character
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            # If it's a 1-byte character (ASCII), continue
            if n_bytes == 0:
                continue

            # UTF-8 characters can be 2-4 bytes long, otherwise it's invalid
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # The following bytes must start with '10'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes remaining for the current UTF-8 char
        n_bytes -= 1

    # If we finished processing all bytes, n_bytes should be 0
    return n_bytes == 0
