import xml.etree.ElementTree as ET

def extract_data_from_xml(xml_string):
    """
    Parse an XML string and extract data from each <record> element.
    
    Args:
        xml_string (str): The XML string to parse.
    
    Returns:
        list: A list of dictionaries, each containing data from a <record>.
    """
    root = ET.fromstring(xml_string)
    records = root.findall('record')
    result = []
    
    for record in records:
        data = {
            'name': record.find('name').text,
            'age': record.find('age').text,
            'position': record.find('position').text
        }
        result.append(data)
    
    return result

# Example usage
xml_example = '''
<root>
    <record>
        <name>John Doe</name>
        <age>35</age>
        <position>Software Engineer</position>
    </record>
    <record>
        <name>Jane Smith</name>
        <age>28</age>
        <position>Designer</position>
    </record>
</root>
'''

parsed_data = parse_xml(xml_example)
print(parsed_data)