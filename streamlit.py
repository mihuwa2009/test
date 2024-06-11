import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_drawable_canvas import st_canvas

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
    canvas_result = st_canvas(stroke_width=15,
                              stroke_color='rgb(255, 255, 255)',
                              background_color='rgb(0, 0, 0)',
                              height=150,
                              width=150,
                              key="canvas")

    if canvas_result.image_data is not None:
        img = canvas_result.image_data
    st.write("Here are the results.")
    # Add results display widgets and functionality here
