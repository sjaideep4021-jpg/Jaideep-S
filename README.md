# Phishing URL Detection System

A beginner-friendly cybersecurity mini project written in Python. It checks a website URL for selected warning signs and displays a simple risk score.

> **Important:** This is an educational demonstration, not a professional phishing detector. A LOW score does not prove that a website is safe, and a HIGH score does not prove that it is malicious.

## 1. Project overview

Phishing is a cyberattack in which criminals use deceptive messages or websites to trick people into sharing sensitive information. This project demonstrates how a program can inspect the text of a URL and flag some characteristics that may deserve attention.

The program does **not** open or visit the submitted website. It does not collect passwords or personal information.

## 2. Features

The program checks for these indicators:
- URL does not use HTTPS.
- Website host is an IP address rather than a domain name.
- URL is longer than 75 characters.
- URL contains selected words such as `login`, `verify`, `account`, or `password`.
- URL contains the `@` symbol.
- URL contains three or more hyphens.

Each detected indicator adds points to a risk score.

### Risk levels

| Score | Warning level |
|---:|---|
| 0–1 | LOW |
| 2–4 | MEDIUM |
| 5 or more | HIGH |

These are simple classroom rules, not validated security ratings.

## 3. Requirements

- Python 3.8 or later
- Windows, macOS, or Linux
- IDLE, Visual Studio Code, or another Python editor

**External packages:** None. The program uses Python standard-library modules.

## 4. Project files

- `phishing_detector.py` — main Python program
- `README.md` — project documentation

## 5. How to run

1. Download `phishing_detector.py` to your computer.
2. Open a terminal or command prompt in the folder containing the file.
3. Run:

   ```bash
   python phishing_detector.py
   ```

   On some systems, use:

   ```bash
   python3 phishing_detector.py
   ```

4. Enter a URL beginning with `http://` or `https://`.
5. Read the risk score, warning level, and reasons.

You can also open the file in Python IDLE or VS Code and run it there.

## 6. Example

Example input:

```text
http://192.0.2.10/verify-account-login
```

Example output:

```text
PHISHING URL DETECTION SYSTEM
--------------------------------
Enter a website URL: http://192.0.2.10/verify-account-login

Risk score: 9
Warning level: HIGH

Warning signs:
- The URL does not use HTTPS.
- The website uses an IP address as its host.
- The URL contains a suspicious keyword.
- The URL contains many hyphens.

Note: This tool cannot guarantee that a website is safe.
```

The example IP address is reserved for documentation and is not intended to identify a real website.

## 7. How it works

1. Reads a URL from the user.
2. Checks that it begins with `http://` or `https://`.
3. Extracts the host name using `urllib.parse`.
4. Checks for selected warning indicators.
5. Adds points for each indicator.
6. Displays the score, warning level, and reasons.

## 8. Limitations

- A phishing URL may not contain any of the indicators used here.
- Legitimate websites can trigger warning signs.
- HTTPS encrypts the connection but does not prove that a website is genuine.
- The program does not check website reputation, page contents, redirects, or domain registration information.
- The risk score is only a learning aid.

## 9. Future improvements

- Add a graphical user interface using Tkinter.
- Add a trusted URL reputation service or threat-intelligence API.
- Evaluate a machine-learning model using a labelled dataset.
- Save scan results locally.
- Develop a browser extension that warns users about suspicious links.

## 10. Safety

Use harmless sample URLs for testing. Do not visit suspicious links or enter passwords, banking details, or other personal information into unknown websites. Do not treat the program's result as a guarantee that a website is safe.

## 11. Student details

- **Student name:** __________________________
- **Department / Class:** _____________________
- **College:** _______________________________
- **Academic year:** _________________________
