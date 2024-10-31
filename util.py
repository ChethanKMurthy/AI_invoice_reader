import openai
import os
from dotenv import load_dotenv
from pypdf import PdfReader
import pandas as pd
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def create_docs(pdf_files):
    # Initialize DataFrame for extracted data
    df = pd.DataFrame({
        'Invoice no': pd.Series(dtype='str'),
        'Description': pd.Series(dtype='str'), 
        'Quantity': pd.Series(dtype='str'), 
        'Date': pd.Series(dtype='str'), 
        'Unit Price': pd.Series(dtype='str'), 
        'Amount': pd.Series(dtype='int'), 
        'Total': pd.Series(dtype='str'), 
        'Email': pd.Series(dtype='str'), 
        'Phone Number': pd.Series(dtype='str'), 
        'Address': pd.Series(dtype='str') 
    })

    # Process each PDF file
    for filename in pdf_files:
        text = ""
        print("Processing ", filename)
        pdf_reader = PdfReader(filename)
        
        # Concatenate all text from PDF pages
        for page in pdf_reader.pages:
            text += page.extract_text()
        
        # Define prompt template for extraction
        template = """
        Extract all the following values: invoice no, description, quantity, date, unit price, amount, total, email, phone number, and address from the following Invoice Content:
        {text}
        
        The fields and values in the above content may be jumbled up as they are extracted from a PDF. Please use your own judgement to fill the fields and values based on the question above.
        
        Expected output format: {{ 'Invoice no': 'xxxx', 'Description': 'xxxx', 'Quantity': 'x', 'Date': 'dd/mm/yyyy', 'Unit Price': xxx.xx, 'Amount': xxx.xx, 'Total': xxx.xx, 'Email': 'xxx@xxx.xxx', 'Phone Number': 'xxxxxxxxxx', 'Address': 'xxxxxxxxxx' }}
        
        Remove all currency symbols from the values. Only provide extracted values, no additional text required.
        """
        
        # Create prompt with text included
        prompt = template.format(text=text)

        # Call OpenAI's API to extract the structured information
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an assistant skilled in structured data extraction."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and parse the JSON output from the response
        extracted_data = eval(response['choices'][0]['message']['content'])
        
        # Append extracted data to DataFrame
        try:
            df = df.append(extracted_data, ignore_index=True)
        except Exception as e:
            print(f"Error appending data for {filename}: {e}")

    return df
