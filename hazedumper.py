from urllib import urlretrieve

def dump():
    urlretrieve("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.hpp", "csgo.py")
    with open("csgo.py", "r+") as hazedumper:
        for line in hazedumper:
            if "constexpr ::std::int64_t timestamp" in line.rstrip():
