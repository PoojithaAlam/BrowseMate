# 🌐 BrowseMate - *An AI-powered agent that browses the web like a human.*

Control a browser using natural language, powered by LLMs, Puppeteer, and Python's asyncio.

## 🚀 How It Works

This app turns your plain language requests into browser automation. Just describe what you want, and the agent does it for you.

Examples:

- 🧠 *"Go to Wikipedia and summarize the Artificial Intelligence page."*
- ✈️ *"Open Skyscanner and search flights from Seattle to New York next Monday."*
- 🔐 *"Log in to example.com using demo credentials."*
- 📝 *"Fill out the feedback form with my name, email, and message."*

**Under the hood:**

1. **Streamlit** captures your input in a user-friendly interface.
2. **OpenAI’s GPT-4** converts your command into actionable steps.
3. **MCP Agent** handles the planning and tool orchestration.
4. **Puppeteer (via Node.js)** runs the browser, executing clicks, scrolls, typing, and navigation.
5. The LLM summarizes or extracts data and returns it — all asynchronously using `asyncio`.

---

## 📦 Features

- 🔍 Navigate and interact with websites using natural commands
- 🖱 Click buttons, scroll pages, and fill out forms
- 📝 Extract and summarize page content
- 📸 Capture screenshots of web pages
- 🔄 Perform multi-step tasks in a single command

---

## 🛠 Tech Stack

- **Python + Streamlit** for the interactive UI
- **OpenAI (GPT-4)** for command interpretation and summarization
- **Puppeteer (Node.js)** for browser control
- **MCP Agent** as the orchestration layer
- **asyncio** for concurrency
- **dotenv** for environment management

---

## ▶️ How to Run

streamlit run main.py



## Screenshots

![App Screenshot](https://github.com/PoojithaAlam/BrowseMate/blob/92f4185ec12708be640b376afab984055a971716/BrowseMate.png)


##  🌍 Live Demo

Explore the app live:

🔗 **[Click here to open Browser MCP Agent](https://browsemate.streamlit.app/)**

Or use the button below:

<p align="left">
  <a href="https://your-app-url.streamlit.app" target="_blank">
    <img src="https://img.shields.io/badge/Open%20App-Click%20Here-brightgreen?style=for-the-badge" alt="Open App">
  </a>
</p>

## ⚠️ Prerequisites
Python 3.8+

Node.js + npm

OpenAI API key

Internet connection to access target websites


## 📄 Example Prompts

“Go to https://en.wikipedia.org/wiki/Artificial_intelligence and summarize it.”

“Click on the first link and scroll halfway down the page.”

“Take a screenshot of the login section.”


## 💡 Planned Enhancements

🎙️ Voice input using WebRTC or browser APIs

📄 Document upload + intelligent summarization

🧠 Support for other LLMs (Claude, Gemini)

🔧 Native Puppeteer JS integration for better control
## 🙌 Acknowledgements

Built using Streamlit

Powered by OpenAI

Browser automation via Puppeteer

Orchestrated using MCP Agent

## 📬 Contact

I'd love to hear your feedback or ideas!

- ✉️ poojithaalam@gmail.com
