import csv
from pprint import pprint

""" Data Quality Dimension
:return: quality report"""


class DQ_dimension:
    @classmethod
    def read_report(cls, file_path):
        with open(file_path, 'r')as csvfile:
            reader = csv.DictReader(csvfile)
            headers = reader.fieldnames  # column name list
            print(headers)
            trans_reader = list(reader)
            row_len = len(trans_reader)  # row length
        return headers, row_len, trans_reader

    def __init__(self, fp):
        self.column_list, self.row_length, self.reader = self.read_report(fp)

    def amount_of_data(self):
        # check the volume of data is appropriate

        pass

    def col_completeness(self, col):
        # completeness at column level
        null_c = 0  # missing values count at column
        col_values = []
        for row in self.reader:
            col_values.append(row[col])
        for val in col_values:
            if not val or val == "":
                null_c += 1
        missing_ratio = round(null_c / self.row_length, 2)
        return 1 - missing_ratio

    def row_completeness(self):
        # completeness at row level
        null_c = 0  # missing values count at row
        for row in self.reader:
            if any(val in (None, "") for val in row.values()):
                null_c += 1
        print(null_c)
        missing_ratio = round(null_c / self.row_length, 2)
        print(missing_ratio)
        return 1 - missing_ratio

    def validity_of_data(self):
        # the degree to which the data conform to defined business rules or constraints
        violation_ratio = 0.0
        return 1 - violation_ratio

    def timeliness_of_data(self):
        return NotImplemented

    def accuracy_of_data(self):
        # data correctness
        #
        return NotImplemented

    def duplicate_of_data(self):
        # entity resolution
        # rule-based
        return NotImplemented


def main():
    report = open('report.log', 'w')
    # quality_check = DQ_dimension(fp='../Dataset/NYCtree1.csv')
    # quality_check = DQ_dimension(fp='demo.csv')
    quality_check = DQ_dimension(fp='../Dataset/food_inspections_1.csv')
    col_list = quality_check.column_list
    for col in col_list:
        ratio = quality_check.col_completeness(col)
        # print(f'column is {col}, the complete ratio is {ratio}')
        report.write(f'column is {col}, the complete ratio is {ratio}\n')
    report.write(f'the complete ratio at row level is {quality_check.row_completeness()}\n')


if __name__ == '__main__':
    main()
