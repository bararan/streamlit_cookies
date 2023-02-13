import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

cookies = EncryptedCookieManager(
    prefix='testapp/cookies_mgr',
    password='1235'
)
if not cookies.ready():
    st.stop()

try:
    v1 = int(cookies["one"])
    v2 = int(cookies["two"])
    v3 = int(cookies["three"])
except KeyError:
    v1, v2, v3 = 10, 20, 30

# st.write(cookies)

with st.form("Inputs"):
    c1, c2, c3 = st.columns(3)

    with c1:
        val1 = st.number_input("One", value=v1)
    with c2:
        val2 =st.number_input("Two", value=v2)
    with c3:
        val3 =st.number_input("Three", value=v3)
    btn = st.form_submit_button()
    if btn:
        cookies["one"] = str(val1)
        cookies["two"] = str(val2)
        cookies["three"] = str(val3)
        cookies.save()