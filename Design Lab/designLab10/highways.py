import zlib
from math import acos,cos,sin,pi,atan2

class Location:
    def __init__(self, id_number, longitude, latitude, name):
        self.id_number = id_number
        self.longitude = longitude
        self.latitude = latitude
        self.name = name

class Link:
    def __init__(self, node_a, node_b, name):
        self.begin = node_a
        self.end = node_b
        self.name = name

locationFromName = eval(zlib.decompress(open('locationFromName.z','rb').read()))
locationFromID = eval(zlib.decompress(open('locationFromID.z','rb').read()))
neighbors = eval(zlib.decompress(open('neighbors.z','rb').read()))
links = eval(zlib.decompress(open('links.z','rb').read()))

def to_kml(path):
    kml = open('path.kml', mode='w')
    kml.write("""<?xml version="1.0" encoding="utf-8"?>
<kml xmlns="http://earth.google.com/kml/2.1">
  <Document>
    <Placemark>
      <LineString>
        <extrude>1</extrude>
        <tessellate>1</tessellate>
        <coordinates>
""")
    kml.writelines("%f,%f\n" % (loc.longitude,loc.latitude) 
                   for loc in [locationFromID[i] for i in path])
    kml.write("""</coordinates>
      </LineString>
    </Placemark>
  </Document>
</kml>
""")
    kml.close()



def locationsMatchingName(state, name):
    name = name or ''
    return [(i,locationFromName[i].id_number) for i in locationFromName if i[:2]==state and name in i[2:]]

def distance(id1, id2):
    """Returns the approximate distance between loc1 and loc2 in miles, 
    taking into account the Earth's curvature."""
    loc1 = locationFromID[id1]
    loc2 = locationFromID[id2]
    phi1 = loc1.latitude*pi/180.
    theta1 = loc1.longitude*pi/180.
    phi2 = loc2.latitude*pi/180.
    theta2 = loc2.longitude*pi/180.
    cospsi = sin(phi1)*sin(phi2) + cos(phi1)*cos(phi2)*cos(theta2-theta1)
    sinpsi = ((sin(theta1)*cos(phi1)*sin(phi2) - sin(theta2)*cos(phi2)*sin(phi1))**2 +\
              (cos(theta2)*cos(phi2)*sin(phi1) - cos(theta1)*cos(phi1)*sin(phi2))**2 +\
              (cos(phi1)*cos(phi2)*sin(theta2-theta1))**2)**0.5
    return atan2(sinpsi,cospsi) * 3958 # miles
