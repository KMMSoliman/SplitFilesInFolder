import os
#==================================================================
# Create empty Kml File
def CreatNewKML(Path , FileName):
    if os.path.exists(Path + "/"+ FileName + ".kml"):
        UserInput = raw_input('File is exist insert: \n N: to delete existing file and create new file \n E: to exit the program \n')
        while UserInput not in ("N" , "n", "E", "e"):
            UserInput = raw_input('File is exist insert: \n N: to delete existing file and create new file \n E: to exit the program \n')

        if UserInput in ("N" , "n"):
            os.remove(Path + "/"+ FileName + ".kml")
            file = open(Path + "/"+ FileName + ".kml", 'w+')
            print ('Old file is deleted and the new file '+ FileName + ' is created')
            file.close()
        #elif UserInput == "E" or "e":
        else:
            print ('File not created')
            #pass
    else:
        file = open(Path + "/"+ FileName + ".kml", 'w+')
        print (FileName + ' is created')
        file.close()
#==================================================================

#==================================================================
# Create the main structure of Kml File
def CreatMainStruc(Path , FileName):
    if os.path.exists(Path + "/"+ FileName + ".kml"):
        if os.stat(Path+ "/" + FileName+".kml").st_size == 0:
            file = open(Path + '/' + FileName + '.kml', 'a+')
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n')

            file.write('<kml xmlns= "http://www.opengis.net/kml/2.2" xmlns:gx= "http://www.google.com/kml/ext/2.2" >\n')
            file.write('<Document id="1">\n')
            file.write('  <name>'+ FileName +'.kml</name>\n')
            """
            file.write('    <Placemark id="2">\n')
            file.write('      <name>'+point[i][2]+'</name>\n')
            file.write('      <Point id="3">\n')
            file.write('        <coordinates>'+point[i][0]+','+ point[i][1]+'</coordinates>\n')
            file.write('      </Point>\n')
            file.write('    </Placemark>\n')
            """
            file.write('\n')
            file.write('\n')
            file.write('</Document>\n')
            file.write('</kml>\n')
            print (FileName + 'is modefied')

        else:
            print('The file is not empty')
            UserInput = ''
            while UserInput not in ("D" , "d", "E", "e"):
                UserInput = raw_input('File is exist insert: \n D: to delete existing file and create new file \n E: to exit the program \n')

            if UserInput in ("D" , "d"):
                file = open(Path + '/' + FileName + '.kml', 'r')
                lines = file.readlines()
                file.close()
                file = open(Path + '/' + FileName + '.kml', 'w')
                for line in lines:
                  if line =="":
                    f.write(line)
                file.close()
                print ('New content is created')

            else:
                print ('The Existing content is not removed')
    else:
        print (FileName + 'kml is not existed')
#==================================================================

#==================================================================
# Check The Image Path
def description(ImagePath, ImageName):
    #return '      <description>&lt;img style=&quot;max-width:500px;&quot; src=&quot;file:///'+ point +'&quot;&gt;</description>\n'
    #return '      <description>&lt;img style=&quot;max-width:500px;&quot; src=&quot;file:///'+ ImagePath+ '/'+ ImageName+'&quot;&gt;</description>\n'

    if os.path.exists(ImagePath+'/'+ ImageName):
        return '      <description>&lt;img style=&quot;max-width:1200px;&quot; src=&quot;file:///'+ ImagePath+ '/'+ ImageName+'&quot;&gt;</description>\n'
        #file.write('      <description>&lt;img style=&quot;max-width:500px;&quot; src=&quot;file:///'+ point[i][3] +'&quot;&gt; &lt;img style=&quot;max-width:500px;&quot; src=&quot;file:///'+ point[i][3] +'&quot;&gt;</description>\n')
    else:
        return '      <description>Image not found</description>\n'
#==================================================================

#==================================================================
def DrawLine (lat1, long1, lat2, long2):
    file.write('    <Placemark>\n')
    file.write('      <LineString>\n')
    file.write('        <coordinates>\n')
    file.write('          '+ lat1 + ','+  long1+', 0'+' ')
    file.write('          '+ lat2+ ','+ long2+', 0\n')
    file.write('        </coordinates>\n')
    file.write('      </LineString>\n')
    file.write('    </Placemark>\n')

#==================================================================
# Point Creation Structure
def PointCreation(SavePath, KmlFileName, date, Long, lat, ImagePath, ImageName, Id, elev):
    #file = open(SavePath + '/' + KmlFileName + '.kml', 'a+')
    file.write('    <Placemark id="'+str(Id)+'">\n')
    file.write(description(ImagePath, ImageName))
    file.write('      <name>'+ date+ '</name>\n')
    file.write('      <styleUrl>#m_ylw-pushpin</styleUrl>\n')
    file.write('      <Point id="2">\n')
    file.write('        <coordinates>'+str(Long)+','+ str(lat)+ ','+ str(elev)+'</coordinates>\n')
    file.write('      </Point>\n')
    file.write('    </Placemark>\n')
    #print("")
#==================================================================

#==================================================================
# Create Style of points
def LabelStyle(styleName, IconScale, labelScale, labelShape):
    labelShape = "http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png"
    file.write('  <StyleMap id="m_ylw-pushpin">\n')
    file.write('    <Pair>\n')
    file.write('      <key>normal</key>\n')
    file.write('      <styleUrl>#'+styleName+'</styleUrl>\n')
    file.write('    </Pair>\n')
    file.write('    <Pair>\n')
    file.write('      <key>highlight</key>\n')
    file.write('      <styleUrl>#'+styleName+'</styleUrl>\n')
    file.write('    </Pair>\n')
    file.write('  </StyleMap>\n')
    file.write('  <Style id="'+styleName+'">\n')
    file.write('    <IconStyle>\n')
    file.write('      <scale>'+IconScale+'</scale>\n')
    file.write('      <Icon>\n')
    file.write('      <href>'+labelShape+'</href>\n')
    file.write('      </Icon>\n')
    file.write('    </IconStyle>\n')
    file.write('    <LabelStyle>\n')
    file.write('      <scale>'+labelScale+'</scale>\n')
    file.write('    </LabelStyle>\n')
    file.write('  </Style>\n')
#==================================================================

#==================================================================
# Create Complete Kml File with points and images paths
def CreatCompleateKML(SavePath , KmlFileName, PointDataArray, styleName, IconScale, labelScale, labelShape):
    CreatNewKML(SavePath , KmlFileName)
    if os.path.exists(SavePath + "/"+ KmlFileName + ".kml"):
        if os.stat(SavePath+ "/" + KmlFileName+".kml").st_size == 0:
            global file
            file = open(SavePath + '/' + KmlFileName + '.kml', 'w')
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n')

            file.write('<kml xmlns= "http://www.opengis.net/kml/2.2" xmlns:gx= "http://www.google.com/kml/ext/2.2" >\n')
            file.write('<Document id="1">\n')
            file.write('  <name>'+ KmlFileName +'.kml</name>\n')
            LabelStyle(styleName, IconScale, labelScale, labelShape)
            i = 0
            while i < len(PointDataArray):
                PointCreation(SavePath , KmlFileName, PointDataArray[i]["DateTime"], PointDataArray[i]["ImageEast"], PointDataArray[i]["ImageNorth"], PointDataArray[i]["path"], PointDataArray[i]["iamgeName"], PointDataArray.index(PointDataArray[i]), PointDataArray[i]["ImageElevation"])

                i += 1
            j = 0

            file.write('    <Placemark>\n')
            file.write('      <LineString>\n')
            file.write('        <coordinates>\n')


            while j < len(PointDataArray):
                if j+1 < len(PointDataArray):
                    file.write('          '+ str(PointDataArray[j]["ImageNorth"]) + ','+  str(PointDataArray[j]["ImageEast"])+',0'+' ')
                    file.write(str(PointDataArray[j+1]["ImageNorth"])+ ','+ str(PointDataArray[j+1]["ImageEast"])+',0\n')

                else:
                    break
                j += 1
            file.write('        </coordinates>\n')
            file.write('      </LineString>\n')
            file.write('    </Placemark>\n')

            file.write('\n')
            file.write('\n')
            file.write('</Document>\n')
            file.write('</kml>\n')
            print (KmlFileName + 'is modefied')

        else:
            print('The file is not empty')
            UserInput = ''
            while UserInput not in ("D" , "d", "E", "e"):
                UserInput = raw_input('File is exist insert: \n D: to delete existing file and create new file \n E: to exit the program \n')

            if UserInput in ("D" , "d"):
                file = open(SavePath + '/' + KmlFileName + '.kml', 'r')
                lines = file.readlines()
                file.close()
                file = open(SavePath + '/' + KmlFileName + '.kml', 'w')
                for line in lines:
                  if line =="":
                    f.write(line)
                file.close()
                print ('New content is created')

            else:
                print ('The Existing content is not removed')
    else:
        print (KmlFileName + 'kml is not existed')
#==================================================================
