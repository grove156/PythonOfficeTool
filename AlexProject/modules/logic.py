import numpy as np
import pandas as pd
from datetime import date as dt

class Search_customer:
    def __init__(self, filename, name, expire_date, etc):
        self.name = name
        self. expire_date = expire_date
        self.etc = etc
        self.filename = filename

        today = dt.today()
        m = today.strftime("%m")
        d = today.strftime("%d")
        self.today_ko = str(m) + "월 " + str(d) + "일"

        day_ko = expire_date
        day_ko = day_ko.replace("/", "월 ", 1)
        day_ko = day_ko.replace("/", "일 ", 2)

        year = day_ko[-4:]
        day_ko = day_ko.replace(year, "")
        self.day_ko =year + "년 " + day_ko



    def search(self):
        excel_file = self.filename

        df = pd.read_excel(excel_file)

        search_by_name = df["투자자명"] == self.name
        search_by_expire_date = df["만기일"] == self.expire_date
        #search_by_invest_amount = df["투자금액"] == self.invest_amount

        subset_df = df[search_by_name & search_by_expire_date]
        return subset_df

    def get_actual_return(self):
        dataset = self.search()
        actual_returns = dataset["실지급액"].tolist()
        actual_return_sum = 0
        for actual_return in actual_returns:
            if type(actual_return)== type(1):
                actual_return_sum += actual_return
            else:
                actual_return = actual_return.replace("원","")
                actual_return = actual_return.replace(",","")
                actual_return_sum += int(actual_return)
        return actual_return_sum

    def get_highest_times(self):
        dataset = self.search()
        times = dataset["납입회차"].tolist()
        times_only_numbers = []
        for time in times:
            time = int(time.replace("회차",""))
            times_only_numbers.append(time)
        times_only_numbers.sort()
        highest_time = times_only_numbers[-1]
        return highest_time

    def get_invested_sum(self):
        dataset = self.search()
        invests = dataset["투자금액"].tolist()
        invested_sum = 0
        for invest in invests:
            if type(invest) == type(1):
                invested_sum += invest
            else:
                invest = invest.replace("원","")
                invest = invest.replace(",","")
                invested_sum += int(invest)
        return invested_sum


    def get_income_sum(self):
        dataset = self.search()
        incomes = dataset["수익금"].tolist()
        income_sum = 0
        for income in incomes:
            if type(income) == type(1):
                income_sum += income
            else:
                income = income.replace("원","")
                income = income.replace(",","")
                income_sum += int(income)
        return income_sum

    def get_product(self):
        dataset = self.search()
        products = dataset["투자상품"].tolist()
        product = products[0]
        return product

    def print_result(self):
        result = '''
{0}님 안녕하세요. 레디펀 운영현황 알려드립니다.
현재 ({1} 기준)
- 가입상품: {2}
- 만기일 : {3}
- 총 투자금액 : {4:,}원
- 납입회차 : {5:,}회
- 수익금 : {6:,}원
- 실지급액 : {7:,}원 
{8} 
        '''.format(self.name, self.today_ko, self.get_product(), self.day_ko, self.get_invested_sum(), self.get_highest_times(), self.get_income_sum(), self.get_actual_return(), self.etc)
        return result
