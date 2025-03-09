import xml.etree.ElementTree as ET

def extract_data_from_xml(xml_string, tag_name):
    """
    Parses the provided XML string and extracts the text associated with the specified tag.
    
    Args:
        xml_string (str): The XML data as a string.
        tag_name (str): The tag name whose value is to be extracted.
    
    Returns:
        list: A list of text values for the specified tag. Returns an empty list if the tag is not found.
    """
    root = ET.fromstring(xml_string)
    return [node.text for node in root.iter(tag_name)]