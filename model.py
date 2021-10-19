# #Echo model
# #modelop.init
# def begin():
#     pass

# #modelop.score
# def action(datum):
#     yield datum

# #modelop.metrics
# def metrics(data):
#     yield dict(toy="output")

import logging
import xml.etree.ElementTree as ET
import warnings

logger = logging.getLogger(__name__)
logging.basicConfig()

# modelop.init
def init():
    pass
# this is OK / ignored
# modelop.score
def score(xml_string):
    # Parse xml_string as XML tree using xml library
    try:
        tree = ET.fromstring(xml_string)
    except ET.ParseError as ex:
        # Raise warning if string can't be parsed
        logger.exception("Exception caught")
        warnings.warn(message="Could not parse XML from string: " + str(ex))
    
    # Pull out two numbers from an x and y key in the xml tree
    x = tree.find("x")
    y = tree.find("y")

    # Raise warning if x and/or y keys aren't found
    if not x:
        warnings.warn(message="Key 'x' not found in input XML string")
    if not y:
        warnings.warn(message="Key 'y' not found in input XML string")

    # Multiply them together to return a new xml tree with just a z key
    z = float(x.text) * float(y.text)
    yield "<output><z>{}</z></output>".format(z)


# modelop.metrics
def metrics(data):
    yield {"x": 1}


# git model -> imported (model.py) to MOC
# imported -> run batch job via MOC
# job passed to -> engine via REST/MM/MLC
# engine 
    # -> jet_py.sh 
        # -> jet.py 
            # -> model.py = batchjob.json

# model.py raises Warning -> jet.py catches Warning for that record, then continues

# TODO: Don't let UserWarnings pass through without stopping

if __name__ == "__main__":
    filename = "good_input_record.xml"
    #filename = "bad_input_record.xml"
    #filename = "malformed_input_record.xml"

    with open(filename, "r") as f:
        input_string = f.read()

    print(next(score(input_string)))