import streamlit as st
from pages.bitcoin import bitcoin


pg = st.navigation([
	st.Page(bitcoin, title="비트코인 데이터 분석", icon="📈")
])

pg.run()