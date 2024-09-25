import xml.etree.ElementTree as ET

class XmlNavigator:
    def __init__(self, xml=None):
        self._root = None
        self.raw_xml = xml  
        if xml is not None:
            doc = ET.fromstring(xml) 
            self._root = self._parse_node(doc) 
            self.text = ET.tostring(doc, encoding='unicode').strip() 

    def _parse_node(self, node):
        obj = type('XmlNode', (), {})() 
        obj.text = (node.text or '').strip()
        obj.attrib = node.attrib  
        obj.tag = node.tag 
        obj.raw = ET.tostring(node, encoding='unicode').strip() 
        obj.children = {}

        for child in node:
            if child.tag not in obj.children:
                obj.children[child.tag] = self._parse_node(child)
            else:
                if not isinstance(obj.children[child.tag], list):
                    obj.children[child.tag] = [obj.children[child.tag]]
                obj.children[child.tag].append(self._parse_node(child))

        return obj 

    def get(self, name):
        """This method allows you to retrieve a child node by its tag name. For example, if you want to access the <City> node within <State>, you can call xml_obj.get("City")."""
        if self._root and name in self._root.children:
            return self._root.children[name]
        return None

xml = """<?xml version="1.0" encoding="UTF-8"?>
<State>
    <City>New York</City>
</State>"""

xml_obj = XmlNavigator(xml)


print(xml_obj.text + "\n" )  

state = xml_obj._root  
if state:
    city = state.children.get('City')  
    if city:
        print(city.raw + "\n")  

city = xml_obj.get("City") 
if city:
    print(city.text)  