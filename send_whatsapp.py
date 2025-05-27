import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class FonnteWhatsApp:
    def __init__(self, api_key=None):
        """
        Initialize the FonnteWhatsApp client with your API key
        
        Args:
            api_key (str, optional): Your Fonnte API key from the dashboard. If None, loads from environment variable.
        """
        self.api_key = api_key or os.getenv("FONNTE_API_KEY")
        self.base_url = os.getenv("FONNTE_BASE_URL", "https://api.fonnte.com/send")
        self.headers = {
            "Authorization": self.api_key
        }

    def send_message(self, target, message):
        """
        Send a WhatsApp message to a specific number
        
        Args:
            target (str): The target phone number with country code (e.g., "628123456789")
            message (str): The message to be sent
            
        Returns:
            dict: API response as a dictionary
        """
        payload = {
            "target": target,
            "message": message
        }

        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                data=payload
            )
            return response.json()
        except Exception as e:
            return {"status": "error", "message": str(e)}

    def send_image(self, target, image_url, caption=""):
        """
        Send an image with optional caption
        
        Args:
            target (str): The target phone number with country code
            image_url (str): URL of the image to send
            caption (str, optional): Caption for the image
            
        Returns:
            dict: API response as a dictionary
        """
        payload = {
            "target": target,
            "url": image_url,
            "message": caption
        }

        try:
            response = requests.post(
                self.base_url,
                headers=self.headers,
                data=payload
            )
            return response.json()
        except Exception as e:
            return {"status": "error", "message": str(e)}


# Example usage
if __name__ == "__main__":
    # API key now loaded from .env file
    fonnte = FonnteWhatsApp()

    # Example: Send a text message
    recipient = os.getenv("TEST_RECIPIENT", "6281234567890")  # Replace with the recipient's number or set in .env
    message = "Hello selamat siang!"

    response = fonnte.send_message(recipient, message)
    print("Message response:", json.dumps(response, indent=2))

    # Example: Send an image with caption
    # image_url = "https://example.com/image.jpg"
    # caption = "Check out this image!"
    # response = fonnte.send_image(recipient, image_url, caption)
    # print("Image response:", json.dumps(response, indent=2))
