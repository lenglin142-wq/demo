import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("反比例函数交互式演示")

k = st.slider("调整 k 值", -10.0, 10.0, 1.0, 0.5)
st.latex(r"y = \frac{" + str(k) + "}{x}")

x1 = np.linspace(0.1, 10, 200)
x2 = np.linspace(-10, -0.1, 200)
y1 = k / x1
y2 = k / x2

plt.figure(figsize=(6, 4))
plt.plot(x1, y1, 'b-', linewidth=2)
plt.plot(x2, y2, 'b-', linewidth=2)
plt.axhline(0, color='k', lw=1)
plt.axvline(0, color='k', lw=1)
plt.grid(True, alpha=0.3)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("y")

st.pyplot(plt)
