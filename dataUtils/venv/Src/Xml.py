'''
'@File   : .py
@description:
    @   This py is for read xml data from input datapack or output datapack
@Version: V1.0.0
'''
import zipfile

from xml.dom.minidom import parse
from xml.dom.minidom import parseString
import xml.dom.minidom
import xml.etree.ElementTree as ElementTree

def readZip(filename):
    #filepath = "";
    print("Read File: ", filename+"\n");
    read = zipfile.ZipFile




def read():
    fileTree = ElementTree.parse('ywxx.xml')
    root = fileTree.getroot()
    print(root.text)

if __name__ == '__main__':
    filename = "301_401_SET000E_SET000_3505be77ca7a67f605745f7fbccfca8a_zxlTestA1000E000.zip";
    readZip(filename);
