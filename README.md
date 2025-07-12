
# 🏗️ Autodesk BuildingConnected Pipeline Scraper

This Python automation script logs into Autodesk's [BuildingConnected](https://app.buildingconnected.com/) platform, fetches OTP automatically from Gmail, and scrapes data from the **Bid Board (Pipeline)**. The data is exported to Excel and JSON formats, and a screenshot of the bid board is saved.

---

## 🚀 Features

- 🔐 Automates secure login to Autodesk (BuildingConnected)
- 📩 Automatically fetches OTP (One-Time Passcode) from Gmail using IMAP
- 🧠 Navigates to the Pipeline dashboard and scrapes bid data
- 📊 Saves scraped data to:
  - Excel file (`autodesk_pipeline.xlsx`)
  - JSON file (`autodesk_pipeline.json`)
  - Screenshot (`autodesk_pipeline.png`)

---

## 🧱 Tech Stack

- [Playwright](https://playwright.dev/python/) – Browser automation
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) – HTML parsing
- [pandas](https://pandas.pydata.org/) – Excel & data manipulation
- [imaplib](https://docs.python.org/3/library/imaplib.html) – Email fetching
- [python-dotenv](https://pypi.org/project/python-dotenv/) – Environment variable management

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/autodesk-pipeline-scraper.git
cd autodesk-pipeline-scraper
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

> Note: If you don't have `requirements.txt`, install manually:

```bash
pip install playwright beautifulsoup4 pandas lxml python-dotenv
```

---

## 🔐 Environment Variables (.env)

Create a `.env` file in the project root to securely store sensitive credentials:

```env
GMAIL_EMAIL=your_email@gmail.com
GMAIL_APP_PASSWORD=your_gmail_app_password
AUTODESK_PASSWORD=your_autodesk_password
```

### ✅ How to generate Gmail App Password:
If you have 2FA enabled on Gmail, [generate an App Password](https://support.google.com/accounts/answer/185833) and use it instead of your real password.

---

## ▶️ Usage

Simply run the script:

```bash
python main.py
```

This will:

- Launch Chrome
- Log in to Autodesk
- Fetch OTP from Gmail
- Navigate to the bid pipeline
- Scrape the data
- Save to `.xlsx`, `.json`, and `.png` files

---

## 📁 Output Files

| File                     | Description                          |
|--------------------------|--------------------------------------|
| `autodesk_pipeline.xlsx` | Excel file with scraped table data   |
| `autodesk_pipeline.json` | JSON version of the same data        |
| `autodesk_pipeline.png`  | Screenshot of the Pipeline page      |

---

## 🛑 Warning

- ❌ **DO NOT** commit your `.env` file.
- ✅ Add `.env` to `.gitignore`:

```bash
echo ".env" > .gitignore
```

---

## 🧑‍💻 Author

**Samuel P**  
📧 judosam72@gmail.com

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💡 Disclaimer

This tool is for **educational and internal automation purposes only**.  
Please ensure that usage complies with Autodesk and Gmail's Terms of Service.
