import streamlit as st

def interface():
    limit = 100
    st.title("Interface")
    r = st.button("Request:")
    if r:
        with open('requests_log.txt', 'r') as file:
            n_reqs = int(file.readline())
        with open('requests_log.txt', 'w') as file:
            file.write(str(n_reqs + 1))
        with open('requests_log.txt', 'r') as file:
            n_reqs = int(file.readline())
        st.subheader(f"You have {n_reqs} requests so far")
        st.subheader(f"You have {limit - n_reqs} requests remaining")

        st.text("You requested")

interface()