from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
import getpass

print("📞 Make a Phone Call with Your Message\n")

# 🧾 Input credentials & call details
account_sid = input("🆔 Enter your Twilio Account SID: ").strip()
auth_token = getpass.getpass("🔑 Enter your Twilio Auth Token (hidden): ").strip()
twilio_number = input("📲 Enter your Twilio Phone Number (e.g., +1234567890): ").strip()
to_number = input("📥 Enter recipient's phone number (e.g., +91xxxxxxxxxx): ").strip()
your_message = input("🗣️ Enter the message to be spoken during the call: ").strip()

# 📜 Build the TwiML voice response
response = VoiceResponse()
response.say(your_message, voice="Polly.Joanna", language="en-US")

# 📞 Place the call
try:
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        twiml=response,
        from_=twilio_number,
        to=to_number
    )

    print("✅ Call initiated successfully!")
    print("📱 Call SID:", call.sid)

except Exception as e:
    print(f"❌ Failed to make the call: {e}")
