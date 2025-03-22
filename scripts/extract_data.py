
# Simulated structured data extraction
import json

contacts = [
    {"name": "John Doe", "email": "john@example.com", "company": "Event Co", "phone": "555-1234"}
]

events = [
    {"client": "John Doe", "event": "Corporate Gala", "date": "2025-04-05", "location": "Punta Cana"}
]

with open("data/contacts.json", "w") as f:
    json.dump(contacts, f, indent=2)

with open("data/events.json", "w") as f:
    json.dump(events, f, indent=2)

print("Contacts and events data saved.")
