import streamlit as st
from streamlit_option_menu import option_menu

# Sidebar with tabbed navigation
with st.sidebar:
    selected = option_menu(
        "Main Menu", ["Home", "Training Models", "Results"],
        icons=['house', 'gear', 'bar-chart'],
        menu_icon="cast", default_index=0,
    )

# Home Page
if selected == "Home":
    st.title("Home")
    st.write("Welcome to the Home page.")

# Training Models Page
elif selected == "Training Models":
    st.title("Training Models")
    st.write("Here you can train your models.")
    # Add model training widgets and functionality here

# Results Page
elif selected == "Results":
    st.title("Results")
    st.write("Here are the results.")
    # Add results display widgets and functionality here
