from lxml import etree
#from io import StringIO, BytesIO
import pandas as pd

data = pd.read_csv('CSVData.csv')
FileName = "BuildKmlFile"
PointNameText = '1'
PointNameText1 = '0'
PointNameText2 = '2'
CoordinatesText = '1,1'
CoordinatesText1 = '0,0'
CoordinatesText2 = '2,2'
CoordinatesLineText1 = '1,1,0 \n 5,5,0'
CoordinatesLineText2 = '3,3,3'
#xml = '<kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2"></kml>'
#print(data.head(10))
#root
"""
<kml xmlns="http://www.opengis.net/kml/2.2"
 xmlns:gx="http://www.google.com/kml/ext/2.2">
 text = "xmlns:gx"
"""

page = etree.Element('kml', xmlns = "http://www.opengis.net/kml/2.2" )
doc = etree.ElementTree(page)
document = etree.SubElement(page, 'Document')
name = etree.SubElement(document, 'name')
name.text = FileName

#===============================
#Create Point Class
class Point:
    def __init__(self, PointNameText, CoordinatesText):
        self.PlacemarkPoint = etree.SubElement(document, 'Placemark')
        self.PointName = etree.SubElement(self.PlacemarkPoint, 'name')
        self.PointName.text = PointNameText
        self.Point = etree.SubElement(self.PlacemarkPoint, 'Point')
        self.CoordinatesPoint = etree.SubElement(self.Point, 'coordinates')
        self.CoordinatesPoint.text = CoordinatesText
    #def printData():
        #print(CoordinatesPoint.text)
#End of Creating Point Syntax
#===============================

#===============================
#Create Point Syntax
"""
PlacemarkPoint = etree.SubElement(document, 'Placemark')
PointName = etree.SubElement(PlacemarkPoint, 'name')
PointName.text = PointNameText
Point = etree.SubElement(PlacemarkPoint, 'Point')
CoordinatesPoint = etree.SubElement(Point, 'coordinates')
CoordinatesPoint.text = CoordinatesText
"""
#End of Creating Point Syntax
#===============================

#===============================
#Create Line Syntax
"""
PlacemarkLine = etree.SubElement(document, 'Placemark')
LineString = etree.SubElement(PlacemarkLine, 'LineString')
CoordinatesLine = etree.SubElement(LineString, 'coordinates')
CoordinatesLine.text = CoordinatesLineText1
#CoordinatesLine.text = CoordinatesLineText2
"""
#Ending of Creating Line Syntax
#===============================

"""
headElt = etree.SubElement(page, 'head')
bodyElt = etree.SubElement(page, 'body')

title = etree.SubElement(headElt, 'title')
title.text = 'Your page Title'

linkElt = etree.SubElement(bodyElt, 'link', rel='stylesheet', href = 'mystyke.css')
"""
point1 = Point(PointNameText1, CoordinatesText1)
#point1.PointNameText = PointNameText1
#point1.CoordinatesText = CoordinatesText1
print (point1.CoordinatesPoint)
#point2 = Point()

outFile = open('home.kml', 'w')
outFile.write('<?xml version="1.0" encoding="UTF-8"?> \n')
outFile = open('home.kml', 'ab')
doc.write(outFile,  pretty_print=True)
outFile.close()
