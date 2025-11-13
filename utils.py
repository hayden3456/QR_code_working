"""Utility functions for QR code operations"""


def validate_qr_data(data: str, max_length: int = 2953) -> bool:
    """
    Validate QR code data before encoding.

    Args:
        data: The data to encode in the QR code
        max_length: Maximum allowed length (default is QR max capacity)

    Returns:
        True if valid, False otherwise

    Raises:
        ValueError: If data is empty or exceeds max_length
    """
    if not data:
        raise ValueError("QR code data cannot be empty")

    if len(data) > max_length:
        raise ValueError(f"Data exceeds maximum length of {max_length} characters")

    return True


def calculate_qr_version(data_length: int) -> int:
    """
    Calculate the minimum QR code version needed for data length.

    QR codes range from version 1 (21x21) to version 40 (177x177).
    Each version can store different amounts of data.

    Args:
        data_length: Length of data to encode

    Returns:
        Minimum QR version number (1-40)
    """
    # Simplified calculation (actual calculation is more complex)
    if data_length <= 25:
        return 1
    elif data_length <= 47:
        return 2
    elif data_length <= 77:
        return 3
    elif data_length <= 114:
        return 4
    elif data_length <= 154:
        return 5
    else:
        # For larger data, use approximation
        return min(40, (data_length // 150) + 5)
