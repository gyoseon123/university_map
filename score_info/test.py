from openpyxl import Workbook

d = {1:3, 2:4}

for i,(j,k) in enumerate(d.items()):
    print(i,j,k)


print(len(d))
wb = Workbook()
sheet = wb.active

for i in range(1,10):
    sheet[f'A{i}'] = 'test1'
    sheet[f'B{i}'] = 'test3'



wb.save('C:/Users/H/OneDrive/바탕 화면/visual_studio_code/website/score_info/test.xlsx')