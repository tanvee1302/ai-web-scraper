# 🕸️ AI Web Scraper with LLaMA3

This project is an intelligent web scraping application built with **Streamlit**, **Selenium**, **BeautifulSoup**, and **LangChain's LLaMA3 model**. It allows users to input any website URL, scrape its DOM content, and extract specific information using natural language instructions powered by AI.

---

## 🚀 Features

- 🌐 Scrape live websites using Selenium
- 🧹 Clean and parse HTML with BeautifulSoup
- 🧠 Use LLaMA3 (via LangChain & Ollama) to extract info from scraped DOM
- 💬 Describe what you want to extract in plain English
- 📤 Streamlit UI for easy interaction and result display

---

## 🛠️ Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/ai-web-scraper.git
   cd ai-web-scraper
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Download Chromedriver:

Download the version compatible with your Chrome browser from chromedriver.chromium.org

Update the chrome_driver_path in scrape.py accordingly

🚦 Usage
Start the Streamlit app:

bash
Copy
Edit
streamlit run app.py
Enter a website URL and click "Scrape Site"

Review the cleaned DOM content and describe the information you want

Click "Parse with LLaMA3" to extract relevant content
