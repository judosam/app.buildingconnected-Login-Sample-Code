import asyncio
from patchright.async_api import async_playwright
from bs4 import BeautifulSoup
import pandas as pd
import imaplib
import email
import re
import json

EMAIL = "judosam72@gmail.com"
PASSWORD = "bxkx kjmv nscj ndyq"  # Use 16-digit App Password if 2FA is on

def get_autodesk_otp():
	# Connect to Gmail IMAP
	mail = imaplib.IMAP4_SSL("imap.gmail.com")
	mail.login(EMAIL, PASSWORD)
	mail.select("inbox")

	# Filter latest unseen emails from Autodesk with subject 'One-time passcode'
	status, messages = mail.search(None, '(UNSEEN FROM "noreply@signin.autodesk.com" SUBJECT "One-time passcode")')
	mail_ids = messages[0].split()

	if not mail_ids:
		print("No new OTP emails found.")
		return None

	# Fetch latest matching email
	latest_email_id = mail_ids[-1]
	status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
	raw_email = msg_data[0][1]
	msg = email.message_from_bytes(raw_email)

	# Extract body
	if msg.is_multipart():
		for part in msg.walk():
			if part.get_content_type() == "text/plain":
				body = part.get_payload(decode=True).decode()
				break
	else:
		body = msg.get_payload(decode=True).decode()

	# Search for the 6-digit code
	otp_match = re.search(r'Code:\s*\n?(\d{6})', body)
	if otp_match:
		return otp_match.group(1)
	else:
		return None

async def main():
	async with async_playwright() as pw:
		browser = await pw.chromium.launch(
			headless=False, channel="chrome",
			args=[
				"--disable-gpu",
				"--disable-blink-features=AutomationControlled"
			]
		)
		ctx = await browser.new_context()
		page = await ctx.new_page()
		# await stealth_async(page)

		print("Navigating to Autodesk login page...")
		await page.goto("https://accounts.autodesk.com/logon?resume=%2Fas%2FmOBeYaklBU%2Fresume%2Fas%2Fauthorization.ping&spentity=null#username", wait_until="domcontentloaded", timeout=60000)
		
		print("Waiting for email input...")
		email_input = await page.wait_for_selector('#userName', timeout=10000)
		await email_input.fill('judosam72@gmail.com')

		print("Waiting for next button...")
		next_button = await page.wait_for_selector('#verify_user_btn', timeout=10000)
		await next_button.click()
		await page.wait_for_timeout(5000)
		
		print("Waiting for password input...")
		password_input = await page.wait_for_selector('#password', timeout=10000)
		await password_input.fill('Samuel@0101')
		await page.wait_for_timeout(5000)
		print("Waiting for sign-in button...")
		signin_button = await page.wait_for_selector('#btnSubmit', timeout=10000)
		await signin_button.click()
		await page.wait_for_timeout(5000)
		
		print("Waiting for OTP...")
		await asyncio.sleep(10)
		# Fetch OTP from email
		print("Fetching OTP from email...")
		otp = get_autodesk_otp()
		print("Autodesk OTP is:", otp)
		
		print("Waiting for OTP input...")
		otp_input = await page.wait_for_selector('#VerificationCode', timeout=10000)
		await otp_input.fill(otp)
		
		print("Waiting for sign-in button after OTP...")
		signin_button = await page.wait_for_selector('#btnSubmit', timeout=10000)
		await signin_button.click()
		await page.wait_for_timeout(5000)
		
		print("Navigating to Autodesk pipeline page...")
		await page.goto("https://app.buildingconnected.com/opportunities/pipeline", wait_until="domcontentloaded", timeout=60000)
		await page.wait_for_timeout(5000)

		print("Waiting for email input on pipeline page...")
		email_input = await page.wait_for_selector('#emailField', timeout=10000)
		await email_input.fill('judosam72@gmail.com')

		signin_button = await page.wait_for_selector('button[aria-label="NEXT"]', timeout=10000)
		await signin_button.click()
		await page.wait_for_timeout(5000)

		button = await page.wait_for_selector('div.filter-0-1-89:nth-child(2) > button:nth-child(1)', timeout=10000)
		await button.click()
		await page.wait_for_timeout(5000)

		html_content = await page.inner_html(".bidBoardBeta-0-1-85")
		soup = BeautifulSoup(html_content, 'lxml')
		spec = []
		table = soup.select_one('.tableAndHeader-0-1-71')
		for row in table.select('.ReactVirtualized__Table__headerRow,.ReactVirtualized__Table__row'):
			# print(row.select('.ReactVirtualized__Table__headerColumn,.ReactVirtualized__Table__rowColumn'))
			row_data = [cell.get_text(strip=True) for cell in row.select('.ReactVirtualized__Table__headerColumn,.ReactVirtualized__Table__rowColumn')]
			# print(row_data)
			spec.append(row_data)

		df = pd.DataFrame(spec[1:], columns=spec[0])
		df = df.loc[:, df.columns[df.apply(lambda col: col.str.strip().astype(bool).any(), axis=0)]]
		print("DataFrame created with columns:", df.columns.tolist())
		print(df)
		df.to_excel("autodesk_pipeline.xlsx", index=False)

		df_dict = df.to_dict(orient='records')
		print(df_dict)
		print("DataFrame converted to dictionary format.")
		
		with open("autodesk_pipeline.json", "w", encoding="utf-8") as f:
			json.dump(df_dict, f, ensure_ascii=False, indent=2)
		
		print("Data saved to autodesk_pipeline.xlsx and autodesk_pipeline.json")
		
		await page.screenshot(path="autodesk_pipeline.png", full_page=True)
		print("Screenshot saved as autodesk_pipeline.png")

		await browser.close()

asyncio.run(main())
