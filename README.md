# 🧾 Invoice Data Extractor

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen) ![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![License](https://img.shields.io/badge/License-MIT-green)

### A powerful PDF invoice data extraction tool that leverages OpenAI's GPT-4 to parse essential information like invoice numbers, dates, amounts, and contact details from invoices, and stores it in a structured format for analysis.

## 🌟 Features

- 🔍 Extracts key fields from invoices: invoice numbers, dates, descriptions, amounts, and contact info.
- 💼 Processes multiple PDF files in one go.
- 📝 Outputs structured data in a user-friendly format (Pandas DataFrame).
- 🔒 Keeps your API keys secure with environment variable management.

## 🛠 Tech Stack

| Technology             | Description                                         |
|------------------------|-----------------------------------------------------|
| ![Python](https://img.shields.io/badge/Python-3.9%2B-blue) | Core programming language |
| [OpenAI GPT-4](https://platform.openai.com/) | Language model for intelligent text extraction |
| [LangChain](https://www.langchain.com/) | Framework for building chains with LLMs |
| [PyPDF](https://pypdf2.readthedocs.io/en/latest/) | Library for reading and extracting text from PDF files |
| [Python-dotenv](https://pypi.org/project/python-dotenv/) | Manages environment variables securely |

## 📂 Project Structure

Invoice Extractor/ ├── main.py # Main script to run the extraction ├── util.py # Utility functions for extraction ├── .env # Environment file for API keys ├── requirements.txt # Python package dependencies └── README.md # Project documentation
