import streamlit as st

limit = 100
with open('requests_log.txt', 'r') as file:
    n_reqs = int(file.readline())


st.title("Interface")
st.subheader(f"You have {n_reqs} requests so far")
st.subheader(f"You have {limit - n_reqs} requests remaining")


r = st.button("Request:")
if r:
    st.text("You requested")
    with open('requests_log.txt', 'w') as file:
        file.write(str(n_reqs + 1))

