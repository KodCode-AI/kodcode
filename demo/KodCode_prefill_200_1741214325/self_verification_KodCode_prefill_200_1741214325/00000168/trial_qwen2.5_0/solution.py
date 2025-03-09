import xml.etree.ElementTree as ET

def extract_data_from_xml(xml_string, tag_name):
    """
    Parses the XML string and extracts the text content of elements with the specified tag name.
    
    :param xml_string: The XML content as a string.
    :param tag_name: The tag name of the elements to extract.
    :return: A list of text contents of the found elements.
    """
    root = ET.fromstring(xml_string)
    extracted_data = [element.text for element in root.findall(tag_name)]
    return extracted_data