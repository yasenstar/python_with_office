from openpyxl import load_workbook

# Read Student List from Prepared Excel file
def read_excel(path):
    wb = load_workbook(path)
    ws = wb.active
    student_list = list()
    for i, row in enumerate(ws.rows):
        if i == 0:
            continue
        stu_dict = {
            "name": row[0].value,
            "college": row[1].value,
            "major": row[2].value,
            "class": row[3].value,
            "association": row[4].value,
            "join_year": row[5].value,
            "prove_date": row[6].value,
        }
        if isinstance(row[6].value, int):
            raise Exception("请先在Excel把日期转换成文本格式")
        student_list.append(stu_dict)
    return student_list

if __name__ == '__main__':
    students = read_excel("./7-6-5.xlsx")
    print(students)
    # print(len(students))