class Report:
    def get_summary(self):
        return "This is a general report summary"

class SalesReport(Report):
    def get_summary(self):
        return "This is a sales report summary, " + super().get_summary()

sales_report = SalesReport()
print(sales_report.get_summary())