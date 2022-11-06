from datetime import datetime
from collections import Counter


class SimpleReport:
    @classmethod
    def get_earliest_date_manufacture(cls, list):
        manufacture_date_list = [
          datetime.strptime(date["data_de_fabricacao"], "%Y-%m-%d").date()
          for date in list]

        return (manufacture_date_list)

    @classmethod
    def get_closest_expiration_date(cls, list):
        expiration_date_list = [
          datetime.strptime(date["data_de_validade"], "%Y-%m-%d").date()
          for date in list]

        return (expiration_date_list)

    @classmethod
    def get_company_with_more_products(cls, list):
        companies = Counter(
          company["nome_da_empresa"] for company in list).most_common()
        # print(company[0][0], line 26)

        return companies[0][0]

    @classmethod
    def generate(cls, list):
        earliest_date = SimpleReport.get_earliest_date_manufacture(list)
        closest_date = SimpleReport.get_closest_expiration_date(list)
        company = SimpleReport.get_company_with_more_products(list)

        return (
            f"Data de fabricação mais antiga: {min(earliest_date)}\n"
            f"Data de validade mais próxima: {min(closest_date)}\n"
            f"Empresa com mais produtos: {company}"
        )
