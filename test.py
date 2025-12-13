import numpy as np
import streamlit as st

st.title("Jeff")


x = np.array([[1,np.uint32(4)], 
              [2,np.uint32(15)],
              [3,np.uint32(15)],
              [4,np.uint32(15)],
              [5,np.uint32(15)],
              [6,np.uint32(15)],
              [7,np.uint32(15)],
              [8,np.uint32(15)],
              [9,np.uint32(15)],
              [10,np.uint32(15)],
              [11,np.uint32(15)],
              [12,np.uint32(15)],
              ])

for scenario in range(0,2**18):
  a = ~(x[:,1]^4)
  total = 0
  for i in range(0,18):
    total += a%2
    a = a//2
  


print("Finished!")
st.title("Dave! - 18")