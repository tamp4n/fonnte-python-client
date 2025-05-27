# Python WhatsApp Sender using Fonnte API

This project provides a simple Python interface for sending WhatsApp messages using the [Fonnte API](https://fonnte.com).

## Features

- Send text messages to WhatsApp numbers
- Send images with optional captions
- Easy-to-use Python class with error handling

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Configuration

Before using the API, you need to get your API key from the [Fonnte dashboard](https://fonnte.com).

```python
from send_whatsapp import FonnteWhatsApp

# Initialize with your API key
API_KEY = "YOUR_FONNTE_API_KEY"
fonnte = FonnteWhatsApp(API_KEY)
```

### Sending a Text Message

```python
# Replace with the recipient's number (with country code)
recipient = "628123456789"
message = "Hello from Python Fonnte API!"

response = fonnte.send_message(recipient, message)
print(response)
```

### Sending an Image with Caption

```python
recipient = "628123456789"
image_url = "https://example.com/image.jpg"
caption = "Check out this image!"

response = fonnte.send_image(recipient, image_url, caption)
print(response)
```

## API Response

The API responses are returned as Python dictionaries. A successful response typically includes:

```json
{
  "status": true,
  "details": "Some message from the API"
}
```

## License

This project is open source and available under the MIT License.

## Credits

This project uses the [Fonnte API](https://fonnte.com/tutorial/mengirim-pesan-whatsapp-php-api/) for sending WhatsApp messages.
