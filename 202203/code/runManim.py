import os

f = open ('run_manim.bat', 'w')

py_file_name = 'beziersurface.py'
classname = 'addthesquare'
videoquality = '--hd'
other = '-ow'
str01 = 'manimgl ' + py_file_name + ' ' + classname + ' ' + videoquality
#str01 = 'manimgl ' + py_file_name + ' ' + classname + ' ' + videoquality + ' ' + other

f.write(str01)
f.close

os.system('run_manim.bat')
