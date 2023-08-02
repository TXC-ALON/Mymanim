from manimlib import *
import numpy as np
np.set_printoptions(precision=3)

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
    myinterfacep = find_intersection(a1, n1, a2, n2)
    print("as {0}, am {1}, ae {2},len is {3}".format(a1, h, a2, arclen))
def checkarc(arc):
    arclen = len(arc.get_points())
    midlen = int(arclen/2)
    print(arclen)
    print(midlen)
    a_s = arc.get_points()[0]
    a_m = arc.get_points()[midlen]
    a_e = arc.get_points()[-1]
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
    myinterfacep = find_intersection(a1, n1, a2, n2)
    print("as {0}, am {1}, ae {2},len is {3}".format(a_s, a_m, a_e,arclen))
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
    checkarc(arc1)
    checkarc(arc3)
def testitem(a1= np.array([0.0,0.0,0.0]),h= np.array([1,0.0,0.0]),a2= np.array([1.0,1.0,0.0])):
    t1 = h - a1
    t2 = h - a2
    n1 = rotate_vector(t1, TAU / 4)
    n2 = rotate_vector(t2, TAU / 4)
    myinterfacep = find_intersection(a1, n1, a2, n2)
    print("a1 {0}, h {1}, a2 {2}".format(a1, h, a2))
    print("t1 {0}, t2 {1}".format(t1, t2))
    print("n1 {0}, n2 {1}".format(n1, n2))
    print(myinterfacep)

testArc()