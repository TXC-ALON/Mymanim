import matplotlib.pyplot as plt
from Pi_walk import PIWalk

for i in range(10001, 100000):
    piw = PIWalk(i)
    piw.fill_walk()

    num = str(i)
    scale = 20
    mm = int(i/10000+1)
    m = str(mm)
    imgs_dir = './pinew' + m + '0000/'

    if i > 100:
        scale = 10
    if i > 1000:
        scale = 5
    if i > 5000:
        scale = 2
    if i > 10000:
        scale = 1.3
    if i > 50000:
        scale = 0.8

    plt.figure(figsize=(11, 6))
    point_numbers = list(range(piw.num_points))

    title_str = 'the ' + num + ' dot\'s position is ' + 'x:' + str(piw.x_values[i - 1]) + ' y:' + str(piw.y_values[i - 1])
    plt.scatter(piw.x_values, piw.y_values, c=point_numbers,edgecolor='none', s=scale)
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(piw.x_values[-1], piw.y_values[-1], c='red', edgecolors='none',s=50)

    plt.title(title_str)
    plt.savefig(imgs_dir + num + '.png', dpi=180)
    plt.close()
