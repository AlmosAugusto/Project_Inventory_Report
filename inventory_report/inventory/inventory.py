import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import json
import xmltodict


class Inventory:
    @classmethod
    def read_files(cls, path):
        if path.endswith(".csv"):
            with open(path) as csvfile:
                reader = csv.DictReader(csvfile, delimiter=",")
                return list(reader)

        elif path.endswith(".json"):
            with open(path) as jsonfile:
                reader = json.load(jsonfile)
                return list(reader)

        elif path.endswith(".xml"):
            with open(path) as xmlfile:
                reader = xmltodict.parse(xmlfile.read())["dataset"]["record"]
                return list(reader)

    @classmethod
    def import_data(cls, path, type):
        products_data = Inventory.read_files(path)
        # print(products_data, "line 29")
        if type == "simples":
            return SimpleReport.generate(products_data)
        elif type == "completo":
            return CompleteReport.generate(products_data)
