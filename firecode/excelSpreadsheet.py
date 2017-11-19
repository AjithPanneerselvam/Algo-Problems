"""
# Excel Spreadsheet - Column Number to Column Name
Time-Complexity - O(log n)
Space Complexity - O(1)

We're sure you've used Microsoft Excel or Google Sheets at some point. Given a column number of a spreadsheet, find it's corresponding column name.
Note: "1" denotes column Name "A"

Examples:
Input  : 2
Output : B

Input  : 27
Output : AA
"""

# Necessary modules have already been imported.
def excel_column_number_to_name(column_number):
    result = []

    while column_number > 0:
        remainder = int(column_number % 26)

        if remainder == 0:
            result.append('Z')
            column_number = int(column_number / 26) - 1
        else:
            result.append(chr((remainder-1) + ord('A')))
            column_number = int(column_number / 26)

    result = result[::-1]
    return ("".join(result))

val = int(input())
print (excel_column_number_to_name(val))
