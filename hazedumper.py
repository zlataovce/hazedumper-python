from urllib.request import urlretrieve
import os


def dump():
    offsets = {}
    urlretrieve("https://raw.githubuser"
                "content.com/frk1/hazed"
                "umper/master/csgo.hpp", "csgo.hpp")
    with open("csgo.hpp", "r") as hazedumper:
        data = hazedumper.readlines()
    for line in data:
        if "constexpr ::std::ptrdiff_t " in line:
            line = line.replace("constexpr ::std::ptrdiff_t ", "").replace(";", "").rstrip()
            item_list = line.split(" = ")
            offsets[item_list[0]] = item_list[1]
    os.remove("csgo.hpp")
    return offsets

print(dump())
