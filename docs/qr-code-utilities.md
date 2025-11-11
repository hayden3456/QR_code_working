## QR Code Utility Functions

### validate_qr_data(data, max_length=2953)

Validates the data intended for QR code encoding.

**Parameters:**
- `data` (str): The data to encode in the QR code.
- `max_length` (int, optional): Maximum allowed length of the data. Defaults to 2953, which is the maximum capacity for a QR code.

**Returns:**
- `bool`: Returns `True` if the data is valid, otherwise raises an exception.

**Raises:**
- `ValueError`: If the data is empty or exceeds the maximum length.

### calculate_qr_version(data_length)

Determines the minimum QR code version required based on the data length.

**Parameters:**
- `data_length` (int): The length of the data to encode.

**Returns:**
- `int`: The minimum QR version number required, ranging from 1 to 40.

This function provides a simplified calculation for determining the QR version, which may not cover all edge cases.
