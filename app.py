from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Exposure Log", layout="wide")

html_path = Path(__file__).parent / "exposure-log.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=1600, scrolling=True)
