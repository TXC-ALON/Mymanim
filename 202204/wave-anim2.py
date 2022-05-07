from manimlib import *

import wave
import numpy as np
import queue


def my_coord(x, y):
    return RIGHT * x + UP * y


def new_my_point(scale=1):
    point = Dot()
    point.scale(scale)
    point.set_fill(WHITE, opacity=0.5)
    point.set_stroke(WHITE, width=0)
    return point


def my_curve(t, k1, k2, k3, k4, k5, k6, omega):
    rou = (abs(t/k1 + k2))**k5 / k3 + k4
    theta = t / k6

    return my_coord(rou * np.cos(theta + omega), rou * np.sin(theta + omega))


class MWave():
    def __init__(self):
        self.nframes = 0
        self.framerate = 0
        self.frames = []
        self.npmin = 0
        self.npmax = 0

        self.points = []
        self.k_values = []

        self.num_points = 0

        self.vsum = 0
        self.vsum_qq = None
        self.omega = 0
        self.k1 = 400
        self.k2 = 0
        self.k3 = 2
        self.k4 = -1
        self.k5 = 0.4

    def open(self, path: str):
        with wave.open(path) as f:
            nframes = f.getnframes()
            self.framerate = f.getframerate()
            m_frames = f.readframes(nframes)
            frames = np.frombuffer(m_frames, dtype='short')

            self.nframes = len(frames)
            # part = nframes//4
            self.frames = frames
            self.npmin = np.min(frames)
            self.npmax = np.max(frames)
        return self

    def create(self, scene, scale):
        distance = 200

        # 创建点集
        for i in range(distance):
            rate = int(i**0.8)
            for j in range(0, rate):
                k = i + j / rate
                point = new_my_point(scale)
                scene.add(point)
                self.points.append(point)
                self.k_values.append(k)

        self.num_points = len(self.points)
        self.vsum_qq = queue.Queue(self.num_points)

    def init(self, color_func, opacity_func, k1, k2, k3, k4, k5, k6, k7):
        self.k1 = k1
        self.k2 = k2
        self.k3 = k3
        self.k4 = k4
        self.k5 = k5
        self.k6 = k6
        self.k7 = k7
        self.color_func = color_func
        self.opacity_func = opacity_func

    def update(self, i):
        index = i % self.num_points

        value = 1000*(int(self.frames[i]) - int(self.npmin) /
                      1000) / (int(self.npmax) - int(self.npmin))
        value = min(max(value, 0), 1)

        v2 = index / self.num_points

        pos = my_curve(self.k_values[index], self.k1,
                       self.k2, self.k3, self.k4, self.k5, self.k6, self.omega)
        self.points[index].move_to(pos)
        self.points[index].set_fill(rgb_to_color(
            self.color_func(value, v2)), opacity=self.opacity_func(value, v2))

        self.vsum_qq.put(self.frames[i])
        self.vsum += self.frames[i]
        if self.vsum_qq.qsize() >= self.num_points:
            self.vsum -= self.vsum_qq.get()

        rou = self.vsum / self.num_points
        time = i / self.framerate
        self.k2 = abs(rou)

        self.omega = time / self.k7


wave1 = MWave().open('assets/wav/Bach1.wav')
wave2 = MWave().open('assets/wav/Bach2.wav')

print(wave1.nframes, wave2.nframes)


class MusicVisualizeMain2(Scene):
    def wait1frame(self):
        self.wait(1/self.camera.frame_rate)

    def construct(self):
        wave1.create(self, 2)
        wave2.create(self, 1)
        nframes = wave2.nframes

        wave1.init(color_func=lambda value, v2: [value, v2, 1 - value / 2],
                   opacity_func=lambda value, v2: value/4,
                   k1=400, k2=0, k3=4, k4=2, k5=0.3, k6=2, k7=10)

        wave2.init(color_func=lambda value, v2: [1 - value / 2, v2, 0.2+0.8*value],
                   opacity_func=lambda value, v2: 0.2+value/2,
                   k1=400, k2=0, k3=3, k4=0, k5=0.5, k6=4, k7=10)

        for i in range(nframes):
            wave1.update(i)
            #print("wave1-i", i," " ,nframes)
            wave2.update(i)
            #print("wave2-i", i," " ,nframes)

            if i % wave2.num_points == 0:
                self.wait1frame()

# manimgl wave-anim.py --uhd --frame_rate 30 -w
