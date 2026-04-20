# 🎂 Birthday Wisher

A Python automation that sends personalized birthday emails on the right day.

## How It Works

1. Reads birthdays from `birthdays.csv`
2. Checks if today matches any birthday
3. Picks a random letter template and personalizes it with the recipient's name
4. Sends the email automatically via Gmail SMTP

## Project Structure

```
birthday-wisher/
│
├── main.py
├── birthdays.csv
└── letter_templates/
    ├── letter_1.txt
    ├── letter_2.txt
    └── letter_3.txt
```

## Setup

1. Clone the repo
2. Install dependencies:
```bash
pip install pandas
```
3. Add your credentials in `main.py`:
```python
email = "your_email@gmail.com"
password = "your_app_password"
```
> ⚠️ Use a [Gmail App Password](https://support.google.com/accounts/answer/185833), not your real password.

4. Add birthdays to `birthdays.csv`:
```
name,email,year,month,day
Ana,ana@email.com,1998,4,9
```

## Automate It

To run it daily without manual execution, schedule it with:
- **Windows**: Task Scheduler
- **Mac/Linux**: `cron`

## Built With

- Python 3
- `smtplib` — sending emails
- `pandas` — reading the CSV
- `datetime` — checking today's date
