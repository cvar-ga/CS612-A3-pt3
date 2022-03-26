# CS612-A3-pt3
The GitHub repository for Part 3 of Assignment 3 in CS 612 at Pace University.

The Python scripts in this repository are dom_parser_schema.py and dom_parser_dtd.py. They each load the students.xml file and validate it against students.xsd and students.dtd, respectively. Ecah of these scripts run independently and separately from each other. To run either script properly, clone this entire repostitory, ```cd``` into the directory from the Terminal, and run the following commands:

```
python3 dom_parser_schema.py
python3 dom_parser_dtd.py
```

The following text describes each of the individual files in this repository.

## dom_parser_schema.py
The Python script which validates the students.xml file against the schema written out in...

## students.xsd
The schema file written out to validate each of the attributes of the XML file.

## dom_parser_dtd.py
The Python script which vaildates the students.xml file against the DTD written out in...

## students.dtd
The DTD file written out to validate each of the attributes of the XML file.

## students.xml
The XML file representing a student directory, with some simple attributes, including student name, level of university, and major.
