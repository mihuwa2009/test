import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Sidebar with navigation options
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Training Models", "Results"])

# Home Page
if page == "Home":
    st.title("Home")
    st.write("Welcome to the Home page.")

# Training Models Page
elif page == "Training Models":
    st.title("Training Models")
    st.write("Here you can train your models.")
    # Add model training widgets and functionality here
    
# Results Page
elif page == "Results":
    st.title("Results")
    st.write("Here are the results.")
    # Add results display widgets and functionality here
    canvas_result = st_canvas(stroke_width=15,
						  stroke_color='rgb(255, 255, 255)',
						  background_color='rgb(0, 0, 0)',
						  height=150,
						  width=150,
						  key="canvas")

    if canvas_result.image_data is not None:
      img = canvas_result.image_data
      st.write(img.shape)
