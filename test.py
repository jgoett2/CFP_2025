import numpy as np
import streamlit as st

st.title("Jeff")

for scenario in range(0,2**18):
  a = np.uint32(14)
  b = np.uint32(15)
  x = np.uint32(~(a^b))
  total = 0
  for i in range(0,18):
    total += x%2
    x = x//2
print("Finished!")
st.title("Dave")