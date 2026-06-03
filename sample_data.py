from utils.database import create_table, add_complaint, get_all_complaints

create_table()

add_complaint("Road damaged near bus stop", "Road", "Hyderabad")
add_complaint("Power outage in colony", "Electricity", "Hyderabad")
add_complaint("Garbage not collected", "Garbage", "Hyderabad")

print(get_all_complaints())
