from urllib import urlretrieve

def dump():
    urlretrieve("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.hpp", "csgo.py")
    with open("csgo.py", "r") as hazedumper:
        data = hazedumper.readlines()
    for line in data:
        if "// " in line:
            if "UTC" in line:
                line.replace("//", "# hazedumper timestamp")
        elif "constexpr ::std::ptrdiff_t " in line:
            line.replace("constexpr ::std::ptrdiff_t ", "")
            line.replace(";", "")
        else:
            line = ''
    with open("csgo.py", "w") as hazedumper:
        hazedumper.writelines(data)
