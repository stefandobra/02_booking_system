from anthropic import Anthropic
from dotenv import load_dotenv
import os
import json

load_dotenv()
client = Anthropic(
    api_key=os.getenv("BOOKING_SYSTEM_API_KEY")
)

def generate_ai_summary(appointments: list, clients: list):
    appts_json = json.dumps([appt.__dict__ for appt in appointments])
    clients_json = json.dumps([cl.__dict__ for cl in clients])

    message = client.messages.create(
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": f"""You are an AI assistant for a beauty salon booking system.
                Analyse the following salon data and provide a business summary including:
                - Most popular treatments
                - Busiest therapist
                - Busiest and slowest days
                - Peak booking times (morning vs afternoon)
                - Estimated revenue (assume £30 per appointment)
                - Client retention (clients who have booked more than once)
                - Clients who haven't booked in over 60 days (re-engagement opportunities)

                Clients data:
                {clients_json}

                Appointments data:
                {appts_json}

                Provide clear, concise insights a salon owner would find useful. Keep it practical and actionable."""
            }
        ],
        model="claude-sonnet-4-6",
    )

    return message.content[0].text


