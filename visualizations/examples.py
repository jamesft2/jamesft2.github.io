from pyscript import display
import matplotlib.pyplot as plt

fig1, ax = plt.subplots()
#visualize the julia set 
ax.plot([0, 1], [0, 1],ls ='-')

ax.set_title("Plot of a solid line as a test")
display(fig1, target="mpl")