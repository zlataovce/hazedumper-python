from urllib.request import urlretrieve
import os

def dump(debug=False):
    if os.path.exists("csgo.hpp"):
        os.remove("csgo.hpp")
    
    if os.path.exists("offsets.py"):
        os.remove("offsets.py")
    urlretrieve("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.hpp", "csgo.hpp")
    if debug == True:
        print("Got file!")
    with open("csgo.hpp", "r") as hazedumper:
        if debug == True:
            print("Opened file!")
        data = hazedumper.readlines()
        if debug == True:
            print("Read lines!")
    offsets = open("offsets.py", "a")
    for line in data:
        if debug == True:
            print("Going to iterate!")
        if "// " in line:
            if debug == True:
                print("Identified C++ comment!")
            if "UTC" in line:
                if debug == True:
                    print("Identified timestamp!")
                line = line.replace("//", "# hazedumper timestamp")
                offsets.write(line)
                if debug == True:
                    print("Wrote timestamp!")
            else:
                if debug == True:
                    print("Identified comment, but no timestamp!")
                line = ''
                offsets.write(line)
                if debug == True:
                    print("Wrote empty line!")
        elif "constexpr ::std::ptrdiff_t " in line:
            if debug == True:
                print("Identified offset!")
            line = line.replace("constexpr ::std::ptrdiff_t ", "")
            line = line.replace(";", ")")
            line = line.replace("= ", "= (")
            offsets.write(line)
            if debug == True:
                print("Wrote offset to pythonic form!")
        else:
            if debug == True:
                print("Not a valid offset!")
            line = ''
            offsets.write(line)
            if debug == True:
                print("Wrote an empty line!")
    offsets.close()

dump(debug=False)
