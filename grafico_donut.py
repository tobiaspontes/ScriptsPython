import matplotlib.pyplot as plt

fig, ax = plt.subplots()
circle = plt.Circle((0,0), 0.64, color='white')
lbls = ['Codar', 'Estudar', 'Comer', 'Dormir']

ax.pie([70, 40, 20, 50],
    labels=lbls,
    autopct='%.1f%%',
    pctdistance=.82)
ax.add_artist(circle)
ax.set_title('Etapas', fontsize=16)

plt.show()