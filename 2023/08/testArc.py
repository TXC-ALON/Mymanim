from manimlib import *
import numpy as np
np.set_printoptions(precision=3)
from scipy.optimize import least_squares
scale_factor = 10000

def threePtoCenter(arc):
    p1,p2,p3 = arc.get_points()[:3]*scale_factor
    print("p1 {0}, p2 {1}, p3 {2}".format(p1, p2, p3))
     # 计算两个中点
    m1 = (p1 + p2) / 2.0
    m2 = (p2 + p3) / 2.0

        # 计算两条直线的斜率
    slope1 = (p2[1] - p1[1]) / (p2[0] - p1[0])
    slope2 = (p3[1] - p2[1]) / (p3[0] - p2[0])
    print("slope1 = {0} slope2 = {1}".format(slope1,slope2))
        # 检查斜率是否接近于无穷大（垂直线）
    if np.isinf(slope1):
        center_x = m1[0]
        center_y = slope2 * (center_x - m2[0]) + m2[1]
    elif np.isinf(slope2):
        center_x = m2[0]
        center_y = slope1 * (center_x - m1[0]) + m1[1]
    else:
            # 计算两条直线的中垂线的斜率
        perpendicular_slope1 = -1 / slope1
        perpendicular_slope2 = -1 / slope2

        # 计算圆心坐标
        center_x = (m2[1] - m1[1] - perpendicular_slope2 * m2[0] + perpendicular_slope1 * m1[0]) / (perpendicular_slope1 - perpendicular_slope2)
        center_y = slope1 * (center_x - m1[0]) + m1[1]

    return np.array([center_x, center_y,0.0])/scale_factor


def find_intersection1(
    p0: npt.ArrayLike,
    v0: npt.ArrayLike,
    p1: npt.ArrayLike,
    v1: npt.ArrayLike,
    threshold: float = 1e-5
) -> np.ndarray:
    """
    Return the intersection of a line passing through p0 in direction v0
    with one passing through p1 in direction v1.  (Or array of intersections
    from arrays of such points/directions).
    For 3d values, it returns the point on the ray p0 + v0 * t closest to the
    ray p1 + v1 * t
    """
    p0 = np.array(p0, ndmin=2)
    v0 = np.array(v0, ndmin=2)
    p1 = np.array(p1, ndmin=2)
    v1 = np.array(v1, ndmin=2)
    m, n = np.shape(p0)
    assert(n in [2, 3])

    numer = np.cross(v1, p1 - p0)
    denom = np.cross(v1, v0)
    if n == 3:
        d = len(np.shape(numer))
        new_numer = np.multiply(numer, numer).sum(d - 1)
        new_denom = np.multiply(denom, numer).sum(d - 1)
        numer, denom = new_numer, new_denom

    denom[abs(denom) < threshold] = np.inf  # So that ratio goes to 0 there
    ratio = numer / denom
    ratio = np.repeat(ratio, n).reshape((m, n))
    return p0 + ratio * v0


def arcmidPoint_ne(arc,n):
    # 假设有多个点的坐标，存储在 points 列表中，每个点是一个二维数组 [x, y]
    points = arc.get_points()[:n]
    # 对坐标进行放大缩小操作，以确保数值适合进行计算
    scaled_points = points * scale_factor
    # 定义拟合函数，用于计算拟合误差
    def circle_residuals(params, x):
        center_x, center_y, radius = params
        return (x[:, 0] - center_x) ** 2 + (x[:, 1] - center_y) ** 2 - radius ** 2
    # 初始化拟合参数
    initial_params = [0, 0, 1]  # 初始圆心坐标和半径
    # 使用最小二乘拟合算法拟合点到圆形模型
    result = least_squares(circle_residuals, initial_params, args=(scaled_points,))
    center_x, center_y, radius = result.x[:3] / scale_factor  # 进行反操作，得到实际坐标值
    # 得到拟合圆的圆心坐标即为圆弧的中心点
    center = np.array([center_x, center_y,0.0])
    return center

def arcmidPoint_ne2(arc,n):
    # 假设有多个点的坐标，存储在 points 列表中，每个点是一个二维数组 [x, y]
    points = arc.get_points()[:n]
    # 对坐标进行放大缩小操作，以确保数值适合进行计算
    scaled_points = points
    # 定义拟合函数，用于计算拟合误差
    def circle_residuals(params, x):
        center_x, center_y, radius = params
        return (x[:, 0] - center_x) ** 2 + (x[:, 1] - center_y) ** 2 - radius ** 2
    # 初始化拟合参数
    initial_params = [0, 0, 1]  # 初始圆心坐标和半径
    # 使用最小二乘拟合算法拟合点到圆形模型
    result = least_squares(circle_residuals, initial_params, args=(scaled_points,))
    center_x, center_y, radius = result.x[:3]  # 进行反操作，得到实际坐标值
    # 得到拟合圆的圆心坐标即为圆弧的中心点
    center = np.array([center_x, center_y,0.0])
    return center
def arcmidPoint(arc):
    # 假设有三个点 A、B、C
    A,B,C = arc.get_points()[:3]
    # 计算线段 AB 的中点 M
    M = (A + B) / 2

    # 计算向量 V，并进行归一化
    V = (C + B) / 2 - M
    V = V / np.linalg.norm(V)

    # 计算中垂线向量 N（即旋转 90°）
    N = np.array([-V[1], V[0],0.0])

    # 计算圆弧的中心点坐标
    center = M + N
    return center
def checkarcSpecial(arc):
    arclen = len(arc.get_points())
    midlen = int(arclen / 2)
    print(arclen)
    print(midlen)
    a1 = arc.get_points()[0]
    h = arc.get_points()[midlen]
    a2 = arc.get_points()[-1]
    t1 = h - a1
    t2 = h - a2
    # Normals
    n1 = rotate_vector(t1, TAU / 4)
    n2 = rotate_vector(t2, TAU / 4)
    myinterfacep = find_intersection1(a1, n1, a2, n2)
    print("as {0}, am {1}, ae {2},len is {3}".format(a1, h, a2, arclen))
    print("t1 {0}, t2 {1}".format(t1, t2))
    print("n1 {0}, n2 {1}".format(n1, n2))
    print(myinterfacep)

def checkarc(arc):
    a1, h, a2 = arc.get_points()[:3]
    # a1= arc1.get_points()[4]
    # h = arc1.get_points()[5]
    # a2 = arc1.get_points()[6]
    arc1Pointlist = arc.get_points()
    print("----------------------")
    # print(arc1Pointlist)
    # Tangent vectors
    t1 = h - a1
    t2 = h - a2
    # Normals
    n1 = rotate_vector(t1, TAU / 4)
    n2 = rotate_vector(t2, TAU / 4)
    myinterfacep = find_intersection1(a1, n1, a2, n2)
    print("a1 {0}, h {1}, a2 {2}".format(a1, h, a2))
    print("t1 {0}, t2 {1}".format(t1, t2))
    print("n1 {0}, n2 {1}".format(n1, n2))
    print(myinterfacep)
    print("----------------------")
def checkarc3(arc):
    a1, h, a2 = arc.get_points()[:3]
    # a1= arc1.get_points()[4]
    # h = arc1.get_points()[5]
    # a2 = arc1.get_points()[6]
    arc1Pointlist = arc.get_points()
    print("----------------------")
    # print(arc1Pointlist)
    # Tangent vectors
    t1 = h - a1
    t2 = h - a2
    # Normals
    n1 = rotate_vector(t1, TAU / 4)
    n2 = rotate_vector(t2, TAU / 4)
    myinterfacep = find_intersection1(a1, n1, a2, n2)
    print("a1 {0}, h {1}, a2 {2}".format(a1, h, a2))
    print("t1 {0}, t2 {1}".format(t1, t2))
    print("n1 {0}, n2 {1}".format(n1, n2))
    print(myinterfacep)
    print("----------------------")

def testArc():
    arc1 = Arc(((3) / 4) * TAU, TAU / 4, radius=0.5).set_color(RED)
    arc1.move_arc_center_to(np.array([0,1,0]))
    arc3 = Arc(((3) / 4) * TAU, TAU / 4, radius=1).set_color(GREEN)
    arc3.move_arc_center_to(np.array([0,1,0]))
    print(threePtoCenter(arc1))
    print(arcmidPoint_ne(arc1,20))
    print(arcmidPoint_ne2(arc1, 20))
    print(arcmidPoint(arc1))
    print("\nCheckArc1")
    checkarc(arc1)
    print("\ncheckarcSpecial1")
    checkarcSpecial(arc1)
    print("\nCheckArc3")
    checkarc(arc3)

def testitem(a1= np.array([0.0,0.0,0.0]),h= np.array([1,0.0,0.0]),a2= np.array([1.0,1.0,0.0])):
    t1 = h - a1
    t2 = h - a2
    n1 = rotate_vector(t1, TAU / 4)
    n2 = rotate_vector(t2, TAU / 4)
    myinterfacep = find_intersection1(a1, n1, a2, n2)
    print("a1 {0}, h {1}, a2 {2}".format(a1, h, a2))
    print("t1 {0}, t2 {1}".format(t1, t2))
    print("n1 {0}, n2 {1}".format(n1, n2))
    print(myinterfacep)

testArc()
