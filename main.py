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


tab1, tab2 = st.tabs(['테스트용 탭 1', '테스트 탭 2'])


with tab2:
	col1, col2 = st.columns([2,3])
	with col1:
		st.title('My First App')
	with col2:
		st.header("이건 헤더입니다.")

	col2.subheader('이건 col2.subheader입니다.')
	col1.link_button("테스트 링크 버튼", "https://leezmodev.vercel.app")
	
	if st.button("NASA"):
		st.write_stream(stream_data)
		st.image("nasa.jpg", caption="images from NASA")






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
        







st.divider()




def calculator():
    
	st.title("간단한 계산기 만들기")
	num1 = st.number_input("숫자1", value=None, placeholder="계산을 원하시는 숫자 1을 입력해주세요")
	num2 = st.number_input("숫자2", value=None, placeholder="계산을 원하시는 숫자 2을 입력해주세요")

	st.divider()
	st.write("아래 버튼을 눌러 결과를 확인해주세요")
	col1, col2, col3, col4 = st.columns(4)


	with col1:
		if st.button("더하기(+)"):
			st.write(num1+num2)
	with col2:
		if st.button("빼기(-)"):
			st.write(num1-num2)
	with col3:
		if st.button("곱하기(*)"):
			st.write(num1*num2)
	with col4:
		if st.button("나누기(/)"):
			try:
				st.write(round(num1/num2))
			except ZeroDivisionError:
				st.write("0으로 나눌 수 없습니다. 다른 숫자를 넣어주세요")


with tab1:
	calculator()