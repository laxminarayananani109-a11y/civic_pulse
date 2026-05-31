from utils.database import *

create_table()

add_complaint("Road damaged near bus stop", "Road", "Hyderabad", "2026-05-30")

add_complaint("Power outage in colony", "Electricity", "Hyderabad", "2026-05-30")

add_complaint("Garbage not collected", "Garbage", "Hyderabad", "2026-05-30")

print(get_all_complaints())
