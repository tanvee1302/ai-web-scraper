import streamlit as st
from scrape import scrape_website, split_dom_Content, clean_body_content, extract_body_content
from parse import parse_with_ollama

st.set_page_config(page_title="AI Web Scraper", layout="wide")
st.title("🕸️ AI Web Scraper with LLaMA3")

# Input: URL
url = st.text_input("🌐 Enter a website URL")

# Scrape button
if st.button("🚀 Scrape Site"):
    if url:
        st.write("🔄 Scraping the website...")
        result = scrape_website(url)
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content)
        st.session_state.dom_content = cleaned_content

        with st.expander("🧾 View Raw DOM Content"):
            st.text_area("DOM Content", cleaned_content, height=300)
    else:
        st.warning("⚠️ Please enter a valid URL.")

# If DOM content is available, show parsing options
if "dom_content" in st.session_state:
    st.markdown("---")
    st.subheader("🔍 Extract Specific Info from DOM")

    parse_description = st.text_area("✏️ What information do you want to extract?")
    if st.button("🧠 Parse with LLaMA3"):
        if parse_description.strip() == "":
            st.warning("⚠️ Please describe what to extract.")
        else:
            st.info("Calling LLaMA3 to parse content...")
            dom_chunks = split_dom_Content(st.session_state.dom_content)
            result = parse_with_ollama(dom_chunks, parse_description)
            st.success("✅ Extraction Complete")
            st.text_area("📤 Extracted Result", result, height=200)
