import xml.etree.ElementTree as ET

def extract_data_from_xml(xml_str, tag_name, attribute_name=None):
    data = []
    root = ET.fromstring(xml_str)
    for element in root.iter(tag=tag_name):
        if attribute_name is not None:
            data.append(element.get(attribute_name))
        else:
            data.append(element.text)
    return data