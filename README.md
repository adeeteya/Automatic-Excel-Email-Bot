# 📧 Automatic Email Sending Bot

A Python-based email automation tool designed to send **individualized emails** using recipient data from an Excel sheet. Commonly used by professors to privately share grades with students, ensuring confidentiality and efficiency.

## ✅ Features

- Sends customized emails to each recipient listed in an Excel sheet
- Secures credentials using `getpass` and SSL encryption
- Configurable SMTP server and sender details via a `config.txt` file
- Facilitates academic use-cases like sharing marks with privacy
- Easy terminal-based interaction


## 🛠️ Technologies Used

- `smtplib`: To create an SMTP client session to send emails.
- `ssl`: For secure connection using TLS.
- `openpyxl`: To read and parse Excel `.xlsx` files.
- `getpass`: For secure password input without echoing it in the terminal.


## 📁 Project Structure

```
📁 email_bot/
 ├── EmailSender.py          # Main script
 ├── config.txt              # Contains SMTP and sender details
 └── student_marks.xlsx      # Excel sheet with student data
```


## ⚙️ Configuration File (config.txt)

Format:
```
smtp_server: smtp.gmail.com
email_id: your-email@gmail.com
filename: student_marks.xlsx
sheetname: Sheet1
```

## 📋 Excel Sheet Format

| A (Name) | B (Email) | C (Marks) |
|----------|-----------|-----------|
| John     | john@email.com | 92    |
| Alice    | alice@email.com | 88   |

## 🚀 How to Run

1. Place your `.xlsx` file in the **same directory** as the Python script.
2. Edit `config.txt` with your SMTP and file details.
3. Run the script:

```bash
python send_emails.py
```

4. When prompted, enter your email password (input hidden).
5. The script will send emails and notify you on successful completion.

## 📌 Notes

- Gmail users may need to enable "Less secure apps" or generate an app-specific password.
- For macOS, you may need to install the `certifi` module if SSL certificates cause issues.

## 🔐 Security Reminder

Avoid hardcoding sensitive information. Use `getpass` or environment variables and **never upload credentials or actual data files to public repositories**.

## 📄 License
This project is for educational and internal use. [MIT License](LICENSE).
