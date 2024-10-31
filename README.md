Started as a hobby project where i stumbled upon the use of Langchains to extract data for a Hackathon.



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

Invoice Extractor/ ├── main.py # Main script to run the extraction 
├── util.py # Utility functions for extraction
├── .env # Environment file for API keys
├── requirements.txt # Python package dependencies 
└── README.md # Project documentation




## ⚙️ Setup and Installation

### Prerequisites

Ensure you have Python 3.9+ installed on your system. Install dependencies with:

```bash
pip install -r requirements.txt
```
API Key Setup
1.Generate an OpenAI API Key: Get your API Key here.
2.Create a .env File: In the project root, create a .env file and add your API key:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

Running the Project
```
streamlit run main.py
```
📝 Usage
1.Place the PDF invoices you want to extract data from in the same directory or specify their path.
2.Run the main.py script, which will process the PDF files, extract structured information, and store it in a Pandas DataFrame.

Example output:
Processing invoice.pdf
{
  'Invoice no': '12345',
  'Description': 'Consulting Services',
  'Quantity': '1',
  'Date': '01/01/2024',
  'Unit Price': '500.00',
  'Amount': '500.00',
  'Total': '500.00',
  'Email': 'client@example.com',
  'Phone Number': '1234567890',
  'Address': '123 Main St, Anytown, USA'
}


📊 Data Extraction Workflow
Load and Split Text: PDFs are loaded, and text is extracted from each page.
Prompt Preparation: Text data is fed to OpenAI's GPT-4 with a specific prompt designed to pull the necessary fields.
Structured Output: The extracted data is processed into a structured format, ideal for further analysis.
🎨 Visual Examples

🔐 Security
API keys are stored securely using environment variables in the .env file. Ensure you do not share or expose this file in public repositories.

🐛 Troubleshooting
Environment Variable Issues: Make sure the .env file is in the root directory.
OpenAI API Errors: Check your API key validity and OpenAI usage limits.














