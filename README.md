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
