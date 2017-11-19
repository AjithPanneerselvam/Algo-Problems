"""
# Oracle

Excel Spreadsheet - Column Name to Number
We're sure you've used Microsoft Excel or Google Sheets at some point. Given a column name of the spreadsheet, return the corresponding column number.

Note: Column name "A" corresponds to column number 1

Examples:
Input  : A
Output : 1

Input  : AA
Output : 27
"""

def excel_column_name_to_number(column_title):
    columnNumber = 0

    for char in column_title:
        columnNumber = columnNumber * 26 + (ord(char) - ord('A')) + 1

    return columnNumber
