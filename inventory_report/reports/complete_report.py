from collections import Counter
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def get_companies(cls, list):
        companies = Counter(
            company["nome_da_empresa"] for company in list
        ).most_common()
        nameAndQuantity = ""
        for company, quantity in companies:
            nameAndQuantity += f"- {company}: {quantity}\n"
        return nameAndQuantity

    @classmethod
    def generate(cls, list):
        simpleReportReturning = super().generate(list)
        nameAndQuantity = CompleteReport.get_companies(list)
        return (
            f"{simpleReportReturning}\n"
            f"Produtos estocados por empresa:\n"
            f"{nameAndQuantity}"
        )
