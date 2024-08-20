import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creads = Credentials.from_service_account_file("info.json", scopes=scopes)
client = gspread.authorize(creads)

sheet_id = "10L8nDdWTUaq1vIOr5HUbcsYznjp3MnALQUhqPBarifU"
workbook = client.open_by_key(sheet_id)


# sheets = map(lambda x: x.title, workbook.worksheets()) #this is use to only display the title of the sheets
# print(list(sheets))

sheet = workbook.worksheet("Mcare Mgmt")
# sheet.update_title("Mcare Mgmt") #this is used to change the title name in worksheet
# print("!Title Changed")


# sheet.update_cell(17, 1, "hey brother are you mad!") #this is used to write in the specefic cell

# for i in range(3, 10):
#     temp = "A" + str(i)
#     value = sheet.acell(temp).value
#     print(value)
# value = sheet.acell("A6").value
# print(value)

# cell = sheet.find("hey brother are you mad!") #this is used to search the value inside ".."
# print(cell.row, cell.col) # this is used to return the row and colum from the sheets
# sheet.format("E4:E8", {"textFormat": {"bold": True}}) # this is used to format the range to bold

temp = "G4:G8"
# value = sheet.get_all_cells()
range_sheet = sheet.batch_get((temp,))[0]
print(range_sheet)
sum = 0
