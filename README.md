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
## 📌 Project Steps

1. **User inputs a website URL** in the Streamlit interface.
2. **Selenium launches a browser** session and loads the page.
3. **BeautifulSoup extracts the `<body>` content** from the raw HTML.
4. HTML content is **cleaned** to remove `<script>` and `<style>` tags.
5. Cleaned DOM is **split into manageable chunks** if too long.
6. User provides a natural language description of what to extract (e.g., "extract all book titles and prices").
7. The chunks are **passed through LLaMA3 via LangChain**, which parses and returns only the required info.
8. Final extracted content is shown in a text area on the UI.

---

## 🛠️ Installation

1. **Create a virtual environment:**

   ```bash
   python -m venv venv

