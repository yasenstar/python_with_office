from openpyxl.utils import get_column_letter, column_index_from_string

col_letter = get_column_letter(20)
print(col_letter)

col_idx = column_index_from_string(col_letter)
print(col_idx)