from manimlib.imports import *
from from_3b1b.active.diffyq.part2.fourier_series import *

# pycharm有自动调整代码格式的快捷键，默认为Alt + Ctrl + L

class FOS (FourierCirclesScene):
  CONFIG = {
    "n_circles": 60,
    "center_point": ORIGIN,
    "slow_factor": 0.1,
    "run_time": 30,
    "tex": "\\Sigma",
    "start_drawn": False
  }

  def construct(self):
    path = self.get_path()
    coefs = self.get_coefficients_of_path(path)
    circles = self.get_circles(coefficients=coefs)
    for k, circle in zip(it.count(1), circles):
      circle.set_stroke(width=max(
        1 / np.sqrt(k),
        1))

    drawn_path = self.get_drawn_path(circles)
    if self.start_drawn:
      drawn_path.curr_time = 1 / self.slow_factor

    self.add(path)
    self.add(circles)
    self.add(drawn_path)
    self.wait(self.run_time)

  def get_path(self):
    tex_mob = TexMobject(self.tex)
    tex_mob.set_height(6)
    path = tex_mob.family_members_with_points()[0]
    path.set_fill(opacity=0)
    path.set_stroke(WHITE, 1)
    return path

  def get_coefficients(self):
    return [complex(0) for x in range(self.n_vectors)]

  def get_coefficients_of_path(self, path, n_samples=10000, freqs=None):
    if freqs is None:
      freqs = self.get_freqs()
    dt = 1 / n_samples
    ts = np.arange(0, 1, dt)
    samples = np.array([
      path.point_from_proportion(t)
      for t in ts
    ])
    samples -= self.center_point
    complex_samples = samples[:, 0] + 1j * samples[:, 1]

    result = []
    for freq in freqs:
      riemann_sum = np.array([
        np.exp(-TAU * 1j * freq * t) * cs
        for t, cs in zip(ts, complex_samples)
      ]).sum() * dt
      result.append(riemann_sum)

    return result

  def get_circles(self, vectors):
    return VGroup(*[
      self.get_circle(
        vector,
        color=color
      )
      for vector, color in zip(
        vectors,
        self.get_color_iterator()
      )
    ])
