class smallcase_model:
    def __init__(self, name, index, investment, value, pnl, actual_pnl, bought_on, timestamp):
        self.name = name.strip()
        self.index = float(index)
        self.investment = float(investment.replace('Rs.', '').replace(',', '').strip())
        self.value = float(value.replace('Rs.', '').replace(',', '').strip())
        self.pnl = float(pnl.replace('%', ''))
        self.actual_pnl = float(actual_pnl.replace('Rs.', '').replace(',', '').strip())
        self.bought_on = bought_on
        self.timestamp = timestamp
        self.nindex = self.index - 100.00

        print(self.name, ':', self.timestamp, self.index, self.investment, self.value, self.actual_pnl, self.pnl)

    def get_ordered_data(self):
        return [self.timestamp, str(self.index), str(self.investment), str(self.value), str(self.actual_pnl), str(self.pnl), str(self.nindex)]