import json, sys
# from xml.dom.expatbuilder import parseString
from xml.dom.minidom import parse, parseString, Node

class Xml_to_json_converter():
    def get_attributes_from_node(self, node):
        attributes = {}
        if node.attributes:
            for attrName, attrValue in node.attributes.items():
                attributes["@" + attrName] = attrValue
        return attributes

    def recursing_xml_to_dict(self, node):
        node_dict = dict()
        for child in node.childNodes:
            if child.nodeType == Node.ELEMENT_NODE:
                if child.nodeName in node_dict.keys():
                    node_dict[child.nodeName].append(self.recursing_xml_to_dict(child))
                else:
                    node_dict[child.nodeName] =[]
                    node_dict[child.nodeName].append(self.recursing_xml_to_dict(child))
        output_dict = self.get_attributes_from_node(node)
        output_dict.update((k, v if len(v) > 1 else v[0]) for k, v in node_dict.items())

        return output_dict

    def convert(self, xml_file_content):
            parsedXml = parseString(xml_file_content)
            return self.recursing_xml_to_dict(parsedXml)

if __name__ == "__main__":
    xml_file = sys.argv[1]
    xml2json = Xml_to_json_converter()
    new =xml2json.convert(xml_file)
    with open("new_json.json",'w') as out_json:
        json_obj = json.dumps(new, indent = 4)
        out_json.write(json_obj)
