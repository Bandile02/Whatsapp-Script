# WhatsApp Business Autoresponder

## Overview

The WhatsApp Business Autoresponder is a Python script that automates the process of responding to incoming messages on WhatsApp for a business. It uses the WhatsApp website to receive messages and sends predefined responses based on user queries. This script is designed to streamline communication with customers, enhance customer service, and provide timely responses to frequently asked questions.

## Prerequisites

Before running the script, make sure you have the following set up:

1. **WhatsApp Business Account**: You need to have a WhatsApp Business account to use the WhatsApp Business API. You can register for a WhatsApp Business account on the WhatsApp Business website.

2. **Python Dependencies**: Ensure you have the necessary Python packages installed. You can install them using the following command:

```bash
pip install selenium
```

## Configuration

1. **WhatsApp Credentials**: In the `config.py` file, replace the placeholders with your WhatsApp account credentials:

```python
WHATSAPP_PHONE_NUMBER = 'YOUR_WHATSAPP_PHONE_NUMBER'
WHATSAPP_PASSWORD = 'YOUR_WHATSAPP_PASSWORD'
```

2. **Autoresponder Rules**: Edit the `autoresponder_rules` dictionary in the `config.py` file to define the rules for autoresponding to specific queries. For example:

```python
autoresponder_rules = {
    'hi': 'Hello! Thank you for reaching out to us.',
    'business hours': 'Our business hours are from 9 AM to 6 PM, Monday to Friday.',
    # Add more rules as needed
}
```

## Usage

1. Make sure you have completed the configuration steps mentioned above.

2. Run the Python script `w_script.py`:

```bash
python w_script.py
```

3. The script will start listening for incoming messages on your WhatsApp Business account and respond based on the predefined rules.

4. To stop the script, press `Ctrl + C`.

## Notes

- The autoresponder will only respond to messages that exactly match the keys in the `autoresponder_rules` dictionary.

- If you need to modify or add new autoresponder rules, you can edit the `autoresponder_rules` dictionary in the `config.py` file without stopping the script.

- Be cautious while defining the autoresponder rules to ensure you provide accurate and helpful responses to your customers.

- This script is intended to handle general queries and provide basic information. For complex interactions or sensitive customer inquiries, it's recommended to have a human operator handle the conversation.

## Disclaimer

This script comes with no warranties or guarantees. The authors are not responsible for any damages or issues caused by the use or misuse of this script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note**: The above Readme file provides a basic outline for the Python script that answers WhatsApp messages for a business. You may need to tailor the instructions, configuration, and usage details based on the specifics of your implementation and the functionality of the script. The script now uses the selenium, an open-source library for WhatsApp, instead of Twilio.
