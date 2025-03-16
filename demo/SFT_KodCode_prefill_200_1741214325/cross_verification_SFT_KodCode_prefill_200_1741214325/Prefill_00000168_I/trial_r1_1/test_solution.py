from solution import *

import xml.etree.ElementTree as ET
from solution import extract_data_from_xml

def test_extract_data_from_xml():
    xml_string = '<root><data>extract this</data><ignore>other text</ignore></root>'
    assert extract_data_from_xml(xml_string, 'data') == 'extract this'

def test_extract_nonexistent_tag():
    xml_string = '<root><data>extract this</data><ignore>other text</ignore></root>'
    assert extract_data_from_xml(xml_string, 'nonexistent') is None

def test_multiple_elements_same_tag():
    xml_string = '<root><data>text1</data><data>text2</data></root>'
    assert extract_data_from_xml(xml_string, 'data') == 'text1'  # Only the first one is extracted

def test_empty_xml():
    xml_string = '<root></root>'
    assert extract_data_from_xml(xml_string, 'data') is None