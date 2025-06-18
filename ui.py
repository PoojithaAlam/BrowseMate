import streamlit as st
import re

def render_ui(query, run_callback):
    st.set_page_config(page_title="🌐BrowseMate", layout="wide")

    st.markdown("""
        <style>
        .main-header {
            font-size: 2.8rem;
            font-weight: 800;
            background: linear-gradient(270deg, #ff6f61, #ffca28, #42a5f5, #7e57c2);
            background-size: 800% 800%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: gradientMove 8s ease infinite;
            display: inline-block;
            margin-bottom: 1rem;
        }

        @keyframes gradientMove {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .subtext {
            font-size: 1.05rem;
            margin-bottom: 2rem;
            color: #444;
        }

        .response-box {
            background-color: #f5f7fa;
            padding: 1rem;
            border-radius: 10px;
            border: 1px solid #ddd;
            font-size: 1.05rem;
            line-height: 1.6;
        }

        @media (prefers-color-scheme: dark) {
            .response-box {
                background-color: #1e1e1e;
                border: 1px solid #333;
                color: #ddd;
            }
        }

        div.stButton > button:first-child {
            background-color: #4CAF50;
            color: white;
            height: 3em;
            font-weight: bold;
            border-radius: 8px;
        }

        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

    with st.sidebar:
        st.markdown("### 📝 Example Commands")
        st.markdown("#### 📍 Navigation")
        st.markdown("- Go to [en.wikipedia.org/wiki/Artificial_intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence)")
        st.markdown("#### 🎯 Interaction")
        st.markdown("- Click on the link to object detection and take a screenshot")
        st.markdown("- Scroll down and summarize the page")
        st.markdown("#### 🛠️ Multi-step Tasks")
        st.markdown("- Navigate to [https://en.wikipedia.org/wiki/Artificial_intelligence](https://en.wikipedia.org/wiki/Artificial_intelligence), scroll down and report details")
        st.markdown("- Scroll and summarize the Wikipedia page")
        st.caption("🔧 The agent uses Puppeteer to control the browser.")

    st.markdown("<h1 class='main-header'>🌐BrowseMate</h1>", unsafe_allow_html=True)
    st.markdown("<div class='subtext'>Interact with a powerful web browsing agent that can navigate and interact with websites using Puppeteer and LLMs.</div>", unsafe_allow_html=True)

    query = st.text_area(
        "Your command",
        value=query,
        placeholder="e.g., Go to https://en.wikipedia.org/wiki/Artificial_intelligence and summarize the page.",
        height=100
    )

    if st.button("Run Command"):
        with st.spinner("🤖 Processing..."):
            result = run_callback(query)

        st.markdown("### ✅ Agent Response")
        if result:
            result_with_links = re.sub(r'(https?://[^\s]+)', r'[\1](\1)', result)
            st.markdown(f"<div class='response-box'>{result_with_links}</div>", unsafe_allow_html=True)
        else:
            st.warning("No response received.")

    return query
