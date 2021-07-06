"""This module declares the XmlParser class"""
import xml.etree.ElementTree as ET
import xmltodict


class NotInDatabaseError(Exception):
    """ Error for when the requested signal is not in database """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class XmlParser:
    """XMLParser class"""

    def __init__(self):
        self.data = None

    def load_file(self, file_path):
        """Method for loading a Json-file and adding it to self.data"""
        tree = ET.parse(file_path)
        data = tree.getroot()
        xml_string = ET.tostring(data, encoding="utf-8", method="xml")
        self.data = dict(xmltodict.parse(xml_string))

    def get_signal_title(self, identifier):
        """Returns title of signal with id "identifier" """

        for entry in self.data["services"]["service"]:
            if entry["@id"] == identifier:
                title = entry["title"]
                return title
        raise NotInDatabaseError("The requested id is not present in database")
