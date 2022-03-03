from imghdr import what
import gspread

gc = gspread.service_account(filename='google.json')
sh = gc.open_by_key("1uGEyi2CirxZs1G1saetekm1LOIFdf7cGZMuf3Ypse7I") # or by sheet name: gc.open("TestList")
worksheet = sh.sheet1
res = worksheet.get_all_values()

#worksheet.update_cell(6,5, )


'''
user = [data.id, data.name, data.full_name]
        worksheet.append_row(user)
############################################################
for i in range(len(res)):
    val = worksheet.row_values(i+1)
    if val[0] == 'mo':
        print('done')
        print(val[0],val[1])
##################################
#print(len(res))
d = ''
for i in range(len(res)):
    if res[i][0] == 'mohmme':
        if res[i][1] == '1234':
            print('dooone')
            d = 'done'
        else:
            print('pass rong')
            d = 'pass rong'
            break
if d == '':
    print('wrong user name')




values_list = worksheet.row_values(1)
print(values_list)
values_list = worksheet.col_values(1)
print(values_list)

print(worksheet.row_count, worksheet.col_count)
print(worksheet.get('A1'))
#print(worksheet.get('A1:C1'))

# INSERT UPDATE

#user = ["Susan", "28", "Sydney"]
#worksheet.insert_row(user, 3)
#worksheet.insert_row(user, 2) #same with column
#worksheet.append_row(user)
#worksheet.update_cell(1,2, value)

# DELETE
#worksheet.delete_rows(1)
#worksheet.delete_columns(1)

'''