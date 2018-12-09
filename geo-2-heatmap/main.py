from src.heatmap import *

if __name__ == "__main__":
    hm = Heatmap()

    for row in open("tests/data/geodata.csv"):
        lat, long, id = row.split(",")
        hm.add_point(lat, long, radius=0)

    hm.save("testfile.jpg")
