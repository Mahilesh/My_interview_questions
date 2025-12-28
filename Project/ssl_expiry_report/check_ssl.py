import ssl
import socks
import socket
import datetime
import requests
import json
import os
import sys

# HTTP Proxy
PROXY_HOST = "repos.gspt.net"
PROXY_PORT = 3128

# List of domains to check
DOMAINS = [
    "www.google.com",
    "www.github.com",
    "www.microsoft.com",
    "www.cloudflare.com",
    "www.wikipedia.org"
]

PORT = 443

# Teams webhook URL stored as environment variable for security
TEAMS_WEBHOOK_URL = os.getenv("TEAMS_WEBHOOK_URL")
if not TEAMS_WEBHOOK_URL:
    raise ValueError("TEAMS_WEBHOOK_URL environment variable not set")

def get_ssl_expiry(domain):
    """Return SSL certificate expiry date via proxy."""
    context = ssl.create_default_context()

    s = socks.socksocket()
    s.set_proxy(socks.HTTP, PROXY_HOST, PROXY_PORT)
    s.settimeout(10)
    s.connect((domain, PORT))

    with context.wrap_socket(s, server_hostname=domain) as ssock:
        cert = ssock.getpeercert()
        expiry_date = datetime.datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
        return expiry_date

def generate_report():
    """Generate SSL expiry table for all domains."""
    report_lines = []

    # Table header (Markdown)
    report_lines.append("| Domain | Expiry Date | Remaining Days | Status |")
    report_lines.append("|--------|------------|----------------|--------|")

    now = datetime.datetime.utcnow()
    for domain in DOMAINS:
        try:
            expiry_date = get_ssl_expiry(domain)
            remaining_days = (expiry_date - now).days
            report_lines.append(f"| {domain} | {expiry_date.date()} | {remaining_days} | ✅ OK |")
        except Exception as e:
            report_lines.append(f"| {domain} | - | - | ❌ Error: {e} |")

    return report_lines

def send_teams_report(report):
    """Send SSL report to Microsoft Teams."""
    payload = {
        "text": "**🔐 SSL Expiry Report**\n\n" + "\n".join(report)
    }

    try:
        response = requests.post(
            TEAMS_WEBHOOK_URL,
            json=payload,
            timeout=10
        )
        if response.status_code != 200:
            raise RuntimeError(f"Teams webhook failed: {response.status_code} {response.text}")
    except Exception as e:
        print(f"Error sending Teams report: {e}", file=sys.stderr)

if __name__ == "__main__":
    report = generate_report()

    # Print to console
    print("\n".join(report))

    # Always send report
    send_teams_report(report)
