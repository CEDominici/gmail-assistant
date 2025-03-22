
# Simulated script to fetch emails and save training data
import json

sample_data = [
    {
        "messages": [
            {"role": "user", "content": "Can I get a quote for 100 chairs for April 5?"},
            {"role": "assistant", "content": "Sure! 100 chairs for April 5 will be $500 total. Would you like to confirm the booking?"}
        ]
    }
]

with open("data/email_training.jsonl", "w") as f:
    for entry in sample_data:
        f.write(json.dumps(entry) + "\n")
print("Email training data saved.")
