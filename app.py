from services.pbiembedservice import PbiEmbedService
from utils import Utils
import streamlit as st
import json

# Load configuration
# Assuming 'config.BaseConfig' contains your configuration settings

# Display the homepage
def display_homepage():
    st.title("Power BI Embedding App")

# Display the report embed configuration
def display_embed_info():
    config_result = Utils.check_config()
    if config_result is not None:
        st.error(f"Error: {config_result}")
    else:
        try:
            embed_info = PbiEmbedService().get_embed_params_for_single_report(
                app.config['WORKSPACE_ID'], app.config['REPORT_ID']
            )
            st.json(embed_info)
        except Exception as ex:
            st.error(f"Error: {str(ex)}")

def main():
    st.set_page_config(page_title="Power BI Embedding App", page_icon=":bar_chart:")

    # Load configuration
    app.config.from_object('config.BaseConfig')

    # Display the selected page based on the URL
    page = st.sidebar.selectbox("Select Page", ["Home", "Embed Info"])

    if page == "Home":
        display_homepage()
    elif page == "Embed Info":
        display_embed_info()

if __name__ == "__main__":
    main()
