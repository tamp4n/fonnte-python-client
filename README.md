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

## Environment Variables

This project uses environment variables to securely store API credentials. Follow these steps to set up your environment:

1. Create a `.env` file in the root directory of the project by copying the provided example:

```bash
cp .env_example .env
```

2. Open the `.env` file and replace the placeholder values with your actual credentials:

```
# Fonnte WhatsApp API Configuration
FONNTE_API_KEY=your_actual_api_key_here
FONNTE_BASE_URL=https://api.fonnte.com/send

# Test configuration (optional)
TEST_RECIPIENT=6281234567890
```

### Available Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `FONNTE_API_KEY` | Yes | Your API key from the Fonnte dashboard |
| `FONNTE_BASE_URL` | Yes | The Fonnte API endpoint URL |
| `TEST_RECIPIENT` | No | A test phone number for development purposes |

## Usage

### Basic Configuration

Before using the API, you need to get your API key from the [Fonnte dashboard](https://fonnte.com) and set it in your `.env` file.

```python
from send_whatsapp import FonnteWhatsApp
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize with your API key from environment variables
API_KEY = os.getenv("FONNTE_API_KEY")
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
