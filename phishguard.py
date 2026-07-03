import re
import sys

print("====================================")
print("      PHISHGUARD EMAIL ANALYZER")
print("====================================")
print("Paste email content below.")
print("Press CTRL + D when finished.\n")

email = sys.stdin.read()

score = 0

suspicious_keywords = [
    "urgent",
    "verify",
    "click here",
    "account suspended",
    "password",
    "login",
    "bank",
    "immediately",
    "limited time",
    "confirm"
]

for keyword in suspicious_keywords:
    if keyword.lower() in email.lower():
        score += 1

urls = re.findall(r'https?://\S+', email)

if len(urls) > 0:
    score += 2

if len(urls) > 3:
    score += 2

print("\n========== SECURITY REPORT ==========")
print("Suspicious Links Found:", len(urls))

if score <= 2:
    risk = "LOW"

elif score <= 5:
    risk = "MEDIUM"

else:
    risk = "HIGH"

print("Risk Level:", risk)

if risk == "HIGH":
    print("Recommendation: Do NOT click links or provide credentials.")

elif risk == "MEDIUM":
    print("Recommendation: Verify sender before responding.")

else:
    print("Recommendation: No major phishing indicators detected.")

print("====================================")
