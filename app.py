import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("反比例函数 y = k/x 作图演示（初中版）")

# 调整 k 值：可以随便输、随便拖
k = st.slider("拖动调整 k", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)
st.subheader(f"当前函数：y = {k}/x")

# 作图用的点（课堂描点法）
x_dot = np.array([-5, -2, -1, 1, 2, 5])
y_dot = k / x_dot

# 平滑曲线
x1 = np.linspace(0.1, 6, 200)
x2 = np.linspace(-6, -0.1, 200)
y1 = k / x1
y2 = k / x2

# 画图
plt.figure(figsize=(6, 4))
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.grid(True, alpha=0.3)

# 先描点
plt.scatter(x_dot, y_dot, color='red', s=60, label='先描点')
# 再连线
plt.plot(x1, y1, color='blue', linewidth=2, label='再连线')
plt.plot(x2, y2, color='blue', linewidth=2)

plt.xlim(-6, 6)
plt.ylim(-6, 6)
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
st.pyplot(plt)

# 初中知识点
st.markdown("""
**初中知识点：**
1. k>0 时，图像在一、三象限
2. k<0 时，图像在二、四象限
3. 图像永远不与x、y轴相交
4. |k| 越大，曲线离坐标轴越远
""")
