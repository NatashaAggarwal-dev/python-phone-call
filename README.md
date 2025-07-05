# 📞 Twilio Phone Call Script with Python

This Python script allows you to make automated phone calls using the [Twilio API](https://www.twilio.com/). It prompts for user input and speaks a custom message over the phone.
## 🚀 Features

- ✅ Make real phone calls using Twilio's voice API  
- 🎙️ Speak custom messages during the call  
- 🔒 Secure Auth Token input using `getpass`  
- 🗣️ Uses `Polly.Joanna` voice in `en-US`  
- 💻 Simple command-line interface  

## 🧰 Requirements

- Python 3.x
- [twilio](https://pypi.org/project/twilio/)
- A Twilio account (free trial available)
- Verified phone numbers in Twilio console

## 🛠️ Setup Instructions

1. **Install Twilio Python Library**  
   Open terminal or Git Bash and run:

   ```bash
   pip install twilio

2.Get Twilio Credentials
Go to Twilio Console and note:

✅ Account SID

🔑 Auth Token

📞 Twilio Phone Number (for calling)

3.Run the Script
In the terminal, run:

python phone_call.py
->Follow the prompts to:

Enter SID, Auth Token

Enter sender and receiver phone numbers

Type the message to speak

4.📁 File Structure
📦 phone_call_project
 ┣ 📄 phone_call.py
 ┗ 📄 README.md

📞 Demo (How It Works)
The script authenticates with Twilio using your inputs.
It sends a call from your Twilio number to the recipient.
Your custom message is read out loud using Twilio's voice engine.


⚠️ Disclaimer
This project is for educational purposes only.
Please follow Twilio’s Acceptable Use Policy and never use this for spamming or commercial use without consent.

## 👩‍💻 Author

**Natasha Aggarwal** 
Github Profile: [@NatashaAggarwal-dev](https://github.com/NatashaAggarwal-dev)
GitHub Repo: [python-phone-call](https://github.com/NatashaAggarwal-dev/python-phone-call)
