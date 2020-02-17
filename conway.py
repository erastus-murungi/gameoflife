import numpy as np
from itertools import product
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def conway(rows, cols, num_zeroes, vid):
    on, off = 1, 0
    Writer = animation.writers['ffmpeg']
    writer = Writer(fps=15, metadata=dict(artist='Erastus'), bitrate=1800, extra_args=['-vcodec', 'libx264'])
    iterations = list(product(range(rows), range(cols)))

    def _draw(state):
        fig, ax = plt.subplots()
        img = ax.imshow(state, interpolation='nearest', cmap='Greys')
        anim = animation.FuncAnimation(fig, _update_state, fargs=(img, state,),
                                       frames=1000,
                                       interval=100,
                                       save_count=50)
        if vid:
            anim.save('conway.mp4', writer=writer)
        plt.show()

    def _neighbors(r, c, state):
        _c = (c - 1) % cols
        _r = (r - 1) % rows
        c_ = (c + 1) % cols
        r_ = (r + 1) % rows
        total = sum([state[r][c_], state[r][_c], state[_r][_c], state[_r][c], state[_r][c_],
                     state[r_][_c], state[r_][c], state[r_][c_]])
        return total

    def _update_state(_, img, state):
        for i, j in iterations:
            outdeg = _neighbors(i, j, state)
            if state[i, j] == on:
                if outdeg < 2 or outdeg > 3:
                    state[i][j] = off
            else:
                if outdeg == 3:
                    state[i][j] = on
        img.set_data(state)
        return img,

    initial = np.random.choice([0] * num_zeroes + [1], (rows, cols))
    _draw(initial)


if __name__ == '__main__':
    conway(100, 100, 20, False)
