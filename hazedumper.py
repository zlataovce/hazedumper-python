from urllib.request import urlretrieve
import os

def dump(debug=False):
    if os.path.exists("csgo.hpp"):
        os.remove("csgo.hpp")
    
    if os.path.exists("offsets.py"):
        os.remove("offsets.py")
    urlretrieve("https://raw.githubuser"
                "content.com/frk1/hazed"
                "umper/master/csgo.hpp", "csgo.hpp")
    if debug:
        print("Got file!")
    with open("csgo.hpp", "r") as hazedumper:
        if debug:
            print("Opened file!")
        data = hazedumper.readlines()
        if debug:
            print("Read lines!")
    offsets = open("offsets.py", "a")
    for line in data:
        if debug:
            print("Going to iterate!")
        if "// " in line:
            if debug:
                print("Identified C++ comment!")
            if "UTC" in line:
                if debug:
                    print("Identified timestamp!")
                line = line.replace("//", "# hazedumper timestamp")
                offsets.write(line)
                if debug:
                    print("Wrote timestamp!")
            else:
                if debug:
                    print("Identified comment, but no timestamp!")
                line = ''
                offsets.write(line)
                if debug:
                    print("Wrote empty line!")
        elif "constexpr ::std::ptrdiff_t " in line:
            if debug:
                print("Identified offset!")
            line = line.replace("constexpr ::std::ptrdiff_t ", "")
            line = line.replace(";", ")")
            line = line.replace("= ", "= (")
            offsets.write(line)
            if debug:
                print("Wrote offset to pythonic form!")
        else:
            if debug:
                print("Not a valid offset!")
            line = ''
            offsets.write(line)
            if debug:
                print("Wrote an empty line!")
    offsets.close()

dump(debug=False)
