import xml.etree.ElementTree as ET

def extract_data_from_xml(xml_string, tag_name, attribute_name=None):
    try:
        root = ET.fromstring(xml_string)
    except ET.ParseError:
        return []
    
    data = []
    for elem in root.iter(tag_name):
        if attribute_name is not None:
            data.append(elem.get(attribute_name))
        else:
            data.append(elem.text)
    return data

# Example usage:
if __name__ == "__main__":
    sample_xml = """
    <catalog>
        <book id="bk101">
            <author>John Smith</author>
            <title>XML for Beginners</title>
            <genre>Computer</genre>
            <price>39.95</price>
        </book>
        <book id="bk102">
            <author>Jane Doe</author>
            <title>XML Basics</title>
            <genre>Computer</genre>
            <price>29.95</price>
        </book>
    </catalog>
    """
    
    # Extract all author names (text content)
    authors = extract_xml_data(sample_xml, 'author')
    print("Authors:", authors)
    
    # Extract all book IDs (attribute)
    book_ids = extract_xml_data(sample_xml, 'book', 'id')
    print("Book IDs:", book_ids)