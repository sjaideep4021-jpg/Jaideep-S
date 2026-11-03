from urllib.parse import urlparse
import ipaddress

SUSPICIOUS_WORDS = [
    "login", "verify", "account", "update",
    "secure", "banking", "password", "confirm"
]


def check_url(url):
    score = 0
    reasons = []

    parsed = urlparse(url)
    host = parsed.hostname or ""

    # Check whether HTTPS is used
    if parsed.scheme != "https":
        score += 2
        reasons.append("The URL does not use HTTPS.")

    # Check whether the host is an IP address
    try:
        ipaddress.ip_address(host)
        score += 3
        reasons.append("The website uses an IP address as its host.")
    except ValueError:
        pass

    # Check URL length
    if len(url) > 75:
        score += 1
        reasons.append("The URL is unusually long.")

    # Check suspicious words
    lower_url = url.lower()
    if any(word in lower_url for word in SUSPICIOUS_WORDS):
        score += 2
        reasons.append("The URL contains a suspicious keyword.")

    # Check the @ symbol
    if "@" in url:
        score += 2
        reasons.append("The URL contains an @ symbol.")

    # Check excessive hyphens
    if url.count("-") >= 3:
        score += 1
        reasons.append("The URL contains many hyphens.")

    # Decide the warning level
    if score <= 1:
        level = "LOW"
    elif score <= 4:
        level = "MEDIUM"
    else:
        level = "HIGH"

    return score, level, reasons


def main():
    print("PHISHING URL DETECTION SYSTEM")
    print("--------------------------------")

    url = input("Enter a website URL: ").strip()

    if not url.startswith(("http://", "https://")):
        print("Invalid input. Enter a URL beginning with http:// or https://")
        return

    score, level, reasons = check_url(url)

    print("\nRisk score:", score)
    print("Warning level:", level)

    if reasons:
        print("\nWarning signs:")
        for reason in reasons:
            print("-", reason)
    else:
        print("No selected warning signs were detected.")

    print("\nNote: This tool cannot guarantee that a website is safe.")


if __name__ == "__main__":
    main()
