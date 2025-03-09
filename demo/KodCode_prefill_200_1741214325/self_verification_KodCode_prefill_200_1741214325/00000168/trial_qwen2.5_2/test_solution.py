from solution import *

import xml.etree.ElementTree as ET
from solution import extract_data_from_xml

def test_extract_data_from_xml():
    xml_data = '''<data>
                    <country name="Liechtenstein">
                        < Ranking >2</ Ranking >
                        <year>2008</ year>
                        <gdppc>141100</ gdppc>
                    </country>
                    <country name="Singapore">
                        < Ranking >4</ Ranking >
                        <year>2011</ year>
                        <gdppc>59900</ gdppc>
                    </country>
                </data>'''
    expected_output = ['2', '4']
    assert extract_data_from_xml(xml_data, ' Ranking ') == expected_output

def test_extract_nonexistent_tag():
    xml_data = '''<data>
                    <country name="Liechtenstein">
                        < Ranking >2</ Ranking >
                        <year>2008</ year>
                        <gdppc>141100</ gdppc>
                    </country>
                    <country name="Singapore">
                        < Ranking >4</ Ranking >
                        <year>2011</ year>
                        <gdppc>59900</ gdppc>
                    </country>
                </data>'''
    expected_output = []
    assert extract_data_from_xml(xml_data, 'nonexistent_tag') == expected_output

def test_extract_data_with_whitespace():
    xml_data = '''<data>
                    <country name="Liechtenstein">
                        < Ranking >  2  </ Ranking >
                    </country>
                </data>'''
    expected_output = ['  2  ']
    assert extract_data_from_xml(xml_data, ' Ranking ') == expected_output

def test_empty_xml():
    xml_data = '<empty></empty>'
    expected_output = []
    assert extract_data_from_xml(xml_data, 'nonexistent_tag') == expected_output