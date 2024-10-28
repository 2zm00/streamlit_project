import time
import numpy as np
import pandas as pd
import streamlit as st
from menu import menu


# Initialize st.session_state.role to None
if "role" not in st.session_state:
    st.session_state.role = None

# Retrieve the role from Session State to initialize the widget
st.session_state._role = st.session_state.role

def set_role():
    # Callback function to save the role selection to Session State
    st.session_state.role = st.session_state._role


# Selectbox to choose role
st.selectbox(
    "Select your role:",
    [None, "user", "admin", "super-admin"],
    key="_role",
    on_change=set_role,
)
menu() # Render the dynamic menu!



col1, col2 = st.columns([2,3])

with col1:
    st.title('My First App')
    
with col2:
    st.header("this is header")

col2.subheader('this is col2.subheader')
col1.link_button("link button add to zmo site", "https://leezmodev.vercel.app")






_Behemoth = """
This computer-simulated image shows a supermassive black hole at the core of a galaxy. The black region in the center represents the black hole’s event horizon, where no light can escape the massive object’s gravitational grip. The black hole’s powerful gravity distorts space around it like a funhouse mirror. Light from background stars is stretched and smeared as the stars skim by the black hole.
"""


def stream_data():
    for word in _Behemoth.split(" "):
        yield word + " "
        time.sleep(0.02)

    yield pd.DataFrame(
        np.random.randn(5, 10),
        columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"],
    )

    for word in _Behemoth.split(" "):
        yield word + " "
        time.sleep(0.02)
        




if st.button("NASA"):
    st.write_stream(stream_data)
    st.image("nasa.jpg", caption="images from NASA")