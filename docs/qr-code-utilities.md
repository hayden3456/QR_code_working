## QR Code Utility Functions

### validate_qr_data(data, max_length=2953)

Validates QR code data before encoding.

**Parameters:**
- `data` (str): The data to encode in the QR code.
- `max_length` (int, optional): Maximum allowed length. Defaults to 2953, which is the maximum capacity for a QR code.

**Returns:** `bool` - True if the data is valid, False otherwise.

**Raises:** `ValueError` - If the data is empty or exceeds the maximum length.

### calculate_qr_version(data_length)

Calculates the minimum QR code version needed for a given data length.

**Parameters:**
- `data_length` (int): Length of the data to encode.

**Returns:** `int` - Minimum QR version number (1-40).

**Note:** This function uses a simplified calculation method. Actual QR version determination may involve more complex logic.
