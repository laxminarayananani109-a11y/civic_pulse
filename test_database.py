from utils.database import create_table, add_complaint, get_all_complaints

create_table()

add_complaint("Water supply issue", "Water", "Hyderabad")

print(get_all_complaints())