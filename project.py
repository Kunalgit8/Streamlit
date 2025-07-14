import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import os

pressed = st.button("1 press = 1 smash")
if pressed:
    st.write("smashed reload to smash again")
st.divider()
st.image(os.path.join(os.getcwd(), "static", "lostless.png"))
