import streamlit as st
import pandas as pd


st.title("Electricity Bill App Using IF_ELSE")

st.subheader("Electricity Units Rates")

df = pd.DataFrame({
    "Unit Range": ["0 - 100", "101 - 200", "201 - 500", "Above 500"],
    "Rate per Unit": ["Free", "5", "10", "20"]
})

st.table(df)

units = st.number_input(label="Enter Units", min_value=0.0, step=1.0,
                        format="%.2f")

if st.button("Calculate Bill"):
    if units <= 100:
        bill = units * 0
    elif units <= 200:
        bill = (100 * 0) + ((units - 100) * 5)
    elif units <= 500:
        bill = (100 * 0) + (100 * 5) + ((units - 200) * 10)
    else:
        bill = (100 * 0) + (100 * 5) + (300 * 10) + ((units - 500) * 20)
    st.write(f"Your Electricity Bill is: Rs {bill}")
