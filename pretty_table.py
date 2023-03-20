from prettytable import PrettyTable, from_csv, from_db_cursor
import sqlite3

# connection = sqlite3.connect("mydb.db")
# cursor = connection.cursor()
# cursor.execute("SELECT field1, field2, field3 FROM my_table")
# my_db_table = from_db_cursor(cursor)




with open("addresses.csv") as fp:
    my_csv_table = from_csv(fp)

dev_table = PrettyTable()
print(my_csv_table)
x = PrettyTable()
dev_table.add_column("Name", ["Ram", "Shyam", "Gita", "Hari", "Bheem", "Kareem"])
dev_table.add_column("Age", [35, 45, 22, 22, 56, 56])
dev_table.add_column("Money", [35, 45, 22, 22, 56, 56])
dev_table.add_column("Bike", ["Yamaha", "Honda", "Bullet", "Hero", "TVS", "Kawasaki"])
print(dev_table)

x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])

print(x)

y = PrettyTable()
y.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
y.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)
print(y)

print(x.get_string(fields=["City name", "Population"]))
print(x.get_string(start=1, end=4))

# Aligning
print(x)
x.align = "l"
print(x)

x.align["City name"] = "l"
x.align["Area"] = "c"
x.align["Population"] = "r"
x.align["Annual Rainfall"] = "c"
print(x)

# Shorting
print(x.get_string(sortby="Population"))

