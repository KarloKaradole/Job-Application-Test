import xml.etree.ElementTree as ET

class XmlNavigator:
    def __init__(self, xml=None):
        self._root = None
        self.raw_xml = xml  # The raw XML string is stored directly in the raw_xml attribute for reference.
        if xml is not None:
            doc = ET.fromstring(xml) # The XML string is parsed into an ElementTree object (doc), which represents the root of the XML document.
            self._root = self._parse_node(doc) # This method is called to recursively parse the XML document and convert it into a structure of custom Python objects, starting from the root element (<State>).
            self.text = ET.tostring(doc, encoding='unicode').strip()  # The entire XML structure is stored as a string in self.text using ET.tostring, so you can easily retrieve the entire XML as a string later.

    def _parse_node(self, node):
        # Create a dynamic node object with text and attributes
        obj = type('XmlNode', (), {})() # This line creates a new, empty object dynamically, using the type function. This object acts as a container for the XML node's information and
                                        # is custom-created for each node in the XML tree and contains the node's information (e.g., <State> or <City>).
        obj.text = (node.text or '').strip() # This stores the inner text of the node. If there is no text, it defaults to an empty string.
        obj.attrib = node.attrib  # If the node has any XML attributes (like <City name="New York">), they are stored in a dictionary.
        obj.tag = node.tag  # The tag (name) of the node (like State or City) is stored for reference.
        obj.raw = ET.tostring(node, encoding='unicode').strip()  # The entire XML of the current node, including its children, is stored as a string. 
                                                                 #This allows easy retrieval of the node's full XML representation (e.g., <City>New York</City>).
        obj.children = {}

        # The for loop processes each child node of the current node recursively, calling _parse_node(child) for each one.
        # If there are multiple children with the same tag (e.g., multiple <City> elements), they are stored in a list.
        for child in node:
            # Check if the tag already exists
            if child.tag not in obj.children:
                obj.children[child.tag] = self._parse_node(child)
            else:
                # Handle multiple children with the same tag by storing them in a list
                if not isinstance(obj.children[child.tag], list):
                    obj.children[child.tag] = [obj.children[child.tag]]
                obj.children[child.tag].append(self._parse_node(child))

        return obj # This method returns the parsed object, which includes the node's text, attributes, tag, raw XML, and children.

    def get(self, name):
        """This method allows you to retrieve a child node by its tag name. For example, if you want to access the <City> node within <State>, you can call xml_obj.get("City")."""
        if self._root and name in self._root.children:
            return self._root.children[name]
        return None

# Example usage:
xml = """<?xml version="1.0" encoding="UTF-8"?>
<State>
    <City>New York</City>
</State>"""

xml_obj = XmlNavigator(xml)

# 1. Output: Entire XML

print(xml_obj.text + "\n" )  # Output: <State><City>New York</City></State>

# 2. Output: <City> New York </City>

state = xml_obj._root  # This accesses the root object directly, which corresponds to the <State> node.
if state:
    city = state.children.get('City')  # This retrieves the City node from the State node's children dictionary.
    if city:
        print(city.raw + "\n")  # Output the raw XML: <City>New York</City>

# 3. Output: New York

city = xml_obj.get("City") # This directly accesses the City node using the get() method.
if city:
    print(city.text)  # Output the text content: New York
    
    
"""   
Summary of Key Concepts:

1.Dynamic Object Creation:
 -Each XML node is parsed into a custom dynamic Python object, allowing flexible access to its text, attributes, tag, and children.

2.Recursive Parsing:
 -The _parse_node() method uses recursion to handle nested XML elements and creates a tree structure of Python objects.

3.Convenient Access to XML Elements:
 -The get() method and direct access to children allow you to navigate through the parsed XML tree easily and retrieve specific nodes or text content.

Your implementation effectively parses and navigates XML using a custom object structure, providing a flexible way to access both the full XML and its individual components.
        
"""


