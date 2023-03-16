import os

os.system("wget http://sourceforge.net/projects/m64py/files/m64py-0.2.3/m64py_0.2.3-0_all.deb")
os.system("sudo dpkg -i m64py_0.2.3-0_all.deb")
os.system("sudo apt-get install -f")
