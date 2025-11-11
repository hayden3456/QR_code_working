## QR Code Utility Functions

### validate_qr_data(data, max_length=2953)

Validates QR code data before encoding.

**Parameters:**
- `data` (str): The data to encode in the QR code.
- `max_length` (int, optional): Maximum allowed length. Defaults to 2953, which is the maximum capacity for QR codes.

**Returns:** `True` if the data is valid, `False` otherwise.

**Raises:** `ValueError` if the data is empty or exceeds the maximum length.

### calculate_qr_version(data_length)

Calculates the minimum QR code version needed for a given data length.

**Parameters:**
- `data_length` (int): Length of the data to encode.

**Returns:** Minimum QR version number (1-40).

**Note:** This function uses a simplified calculation for determining the QR version.
