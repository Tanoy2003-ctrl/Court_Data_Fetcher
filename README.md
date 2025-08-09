# eCourt Case Search – Flask + Selenium

This project provides a **simple web interface** to search Indian court cases from the official **eCourts India Portal**.  
It uses **Flask** for the frontend and **Selenium** to open the eCourts CNR search page with the case details pre-filled, letting you solve the CAPTCHA manually.

------------------------------------------------------------
📌 Features
------------------------------------------------------------
- Clean, minimal web form for entering:
  - Case Type
  - Case Number
  - Filing Year
- Automatic browser launch using Selenium
- No manual ChromeDriver setup (uses webdriver-manager)
- Manual CAPTCHA solving for compliance
- Works on Windows, macOS, and Linux

------------------------------------------------------------
📂 Project Structure
------------------------------------------------------------
project/
├── app.py              # Flask app with UI
├── scraper.py          # Selenium automation logic
├── templates/
│   └── index.html      # HTML form
├── requirements.txt    # All dependencies
└── README.md           # This file

------------------------------------------------------------
🛠 Requirements
------------------------------------------------------------
- Python 3.8+
- Google Chrome browser installed
- Internet connection

------------------------------------------------------------
📥 Installation
------------------------------------------------------------
Install dependencies:
 pip install -r requirements.txt

------------------------------------------------------------
▶️ Usage
------------------------------------------------------------
1. Run the Flask app:
       python app.py

2. Open your browser and go to:
       http://127.0.0.1:5000

3. Enter case details:
   - Case Type
   - Case Number
   - Filing Year

4. Click “Search Case”.
   - Selenium will launch Chrome
   - It will go directly to the eCourts CNR Search page
   - Your case details will be pre-filled

5. Solve the CAPTCHA manually on the eCourts portal and click “Search” there to view official case details.

