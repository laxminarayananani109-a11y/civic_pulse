from utils.database import *

create_table()

add_complaint("Water supply issue", "Water", "Hyderabad", "2026-05-30")

print(get_all_complaints())
