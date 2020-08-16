import os


dir = "peru"

for file in os.listdir(dir):
    # print(file[len(file)-3:])
    if(file[len(file)-3:] == "hgt"):
        name = file[:len(file)-4]
        print(name)
        os.system("gdal_translate -ot Byte -of PNG -scale {}\{}.hgt {}\{}.png".format(dir, name, dir, name))
