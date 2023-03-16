def cans(height, width, coverage):
    area = int(height) * int(width)
    cans_required = area/int(coverage)
    import math
    cans_required = math.ceil(cans_required)
    print(f"Total cans required for wall {area} meter squire is: {cans_required} ")


height = input("enter height in meters: ")
width = input("enter width in meters: ")
coverage = input("Enter area coverage per can")
cans(height, width, coverage)