import untangle
import re
import csv
from pygeodesy import LatLon_, latlonDMS
import sys


inputFilename = sys.argv[1]

try:
    outputFilename = sys.argv[2]
except IndexError:
    outputFilename = inputFilename+'.csv'

print('DEBUG: Reading', inputFilename)
print('DEBUG: Saving to', outputFilename)

latlonre = re.compile(r"""(-*\d+\.\d+)""")  # Extract the two pairs of coords from the rest of the text

mykml = untangle.parse(inputFilename)  # Parse the XML input file

coords = []  # Prepare to store coordinates

for folder in mykml.kml.Document.Folder.Placemark:  # For each 'folder'...
    tmpcoordpair = latlonre.findall(folder.LineString.coordinates.cdata)  # Find all of the Regular Expression string matches

    for i in range(2):  # Since there are '2' pairs do the following...
        coord = LatLon_(tmpcoordpair[i*2], tmpcoordpair[i*2+1])
        coords.append({
            "folder": folder.name.cdata,
            "coord_deg": str(latlonDMS(coord, form='-d')).replace('°', ''),
            "coord_degmin": str(latlonDMS(coord, form='-dm')).replace('°', ' ').replace('′', ''),
            "coord_degminsec": str(latlonDMS(coord, form='-dms')).replace('°', ' ').replace('′', ' ').replace('″', ''),
        })

for coord in coords:
    print(coord)  # For debugging really...

csvHeaders = coords[0].keys()
with open(outputFilename, 'w', newline='', encoding='utf-8') as output_file:
    csv.register_dialect('easyout', delimiter=',', quoting=csv.QUOTE_ALL)
    dict_writer = csv.DictWriter(output_file, csvHeaders, dialect='easyout')
    dict_writer.writeheader()
    dict_writer.writerows(coords)
