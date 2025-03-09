from solution import *

import xml.etree.ElementTree as ET
from solution import extract_data_from_xml

def test_extract_data_from_xml():
    test_xml = '''
    <root>
        <data>First Data</data>
        <data>Second Data</data>
    </root>
    '''
    expected_output = ['First Data', 'Second Data']
    assert extract_data_from_xml(test_xml, 'data') == expected_output

def test_extract_empty_xml():
    test_xml = ''
    expected_output = []
    assert extract_data_from_xml(test_xml, 'data') == expected_output

def test_extract_no_matching_tag():
    test_xml = '''
    <root>
        <info>Some Info</info>
    </root>
    '''
    expected_output = []
    assert extract_data_from_xml(test_xml, 'data') == expected_output

def test_extract_with_whitespace():
    test_xml = '''
    <root>
        <data>\n\tFirst Data\n</data>
        <data>\nSecond Data\n</data>
    </root>
    '''
    expected_output = ['First Data', 'Second Data']
    assert extract_data_from_xml(test_xml, 'data') == expected_output

def test_extract_empty_tag():
    test_xml = '''
    <root>
        <data></data>
        <data>Empty Data</data>
    </root>
    '''
    expected_output = ['Empty Data']
    assert extract_data_from_xml(test_xml, 'data') == expected_output