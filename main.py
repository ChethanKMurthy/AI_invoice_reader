import streamlit as st 
from dotenv import load_dotenv
import util as iu



def main():
    load_dotenv()

    st.set_page_config(page_title="Invioce Extraction bot")
    st.title("Invoice extraction Bot ")
    st.subheader("Extract your invoice data with just a click")

    #Upload the Invoices 
    pdf = st.file_uploader("uplaod your PDF invoice(S) here ",type='pdf',accept_multiple_files=True)
    submit=st.button("Extract Data")

    if submit:
        with st.spinner('Wait for it....'):
            df=iu.create_docs(pdf)
            st.write(df.head())

            data_as_csv=df.to_csv(index=False).encode("utf-8")
            st.download_button(
                'Download data as CSV ',data_as_csv,
                'InvoiceData.csv','text/csv',key="download-tools-csv"
            )
            st.button(
                "save to Invoice_Data.csv file",
                df.to_csv('Invoice_data.csv',mode='a',index=False,header=False)
            )
        st.success("extraction Succeeded")


#invoking Main Function
if __name__=='__main__':
    main()


