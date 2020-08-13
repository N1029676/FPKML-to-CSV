# Flight plan KML to CSV conversion
This quick project exists to convert a specifically formatted KML file containing pair's of coordinates into a CSV file where they are displayed in Degrees, DegreesMinutes, and DegreesMinutesSeconds.

# Procedures
## Converting KML to CSV
1. Open command prompt or powershell and navigate to the folder the script/executable is stored in
2. Call the script where the first argument is the `inputFile` and the optional second argument is the `outputFile`
    - As script: `python parser.py [inputFile] [outputFile]`
    - As executable: `parser.py [inputFile] [outputFile]`
    - If the `outputFile` argument is not specified it will default to using the original path and filename while appending `.csv` to the end
3. After a few seconds the output file should appear where directed while also displaying to the screen

## Created the executable from script
Only needed if developing the script
1. Using pyinstaller run `pyinstaller --onefile parser.py` 

# Caveats
1. This seems to accurately convert coordinates for the given formats, but you should absolutely check that yourself before relying on this
2. If you want to have different formats in the output, you will have to modify the source code yourself
3. Because Excel gets weird with the UTF-8 encoding when you open a CSV, I've removed some characters that caused issues but this may affect readability