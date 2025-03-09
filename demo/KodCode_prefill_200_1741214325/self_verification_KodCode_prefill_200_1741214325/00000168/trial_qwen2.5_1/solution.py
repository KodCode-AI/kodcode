import xml.etree.ElementTree as ET

def extract_data_from_xml(xml_string, tag_name):
    """
    Parses the provided XML string and extracts the text content of the first occurrence of the specified tag.

    :param xml_string: The XML data as a string.
    :param tag_name: The name of the tag to extract the text from.
    :return: The text content of the first <tag_name> element or None if not found.
    """
    root = ET.fromstring(xml_string)
    tag = root.find(tag_name)
    if tag is not None:
        return tag.text
    return None