import streamlit as st

pg = st.navigation(
    [
        st.Page("pages/home.py", title="Home"),
        st.Page("pages/form.py", title="Form Test"),
    ]
)
pg.run()
