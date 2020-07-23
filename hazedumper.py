from urllib.request import urlretrieve

def dump(debug=False):
    urlretrieve("https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.hpp", "csgo.hpp")
    if debug == True:
        print("Got file!")
    with open("csgo.hpp", "r") as hazedumper:
        if debug == True:
            print("Opened file!")
        data = hazedumper.readlines()
        if debug == True:
            print("Read lines!")
        for line in data:
            if debug == True:
                print("Going to iterate!")
            if "// " in line.rstrip():
                if debug == True:
                    print("Identified C++ comment!")
                if "UTC" in line.rstrip():
                    if debug == True:
                        print("Identified timestamp!")
                    line = line.replace("//", "# hazedumper timestamp")
                    if debug == True:
                        print("Wrote timestamp!")
                else:
                    if debug == True:
                        print("Identified comment, but no timestamp!")
                    line = ''
                    if debug == True:
                        print("Wrote empty line!")
            elif "constexpr ::std::ptrdiff_t " in line.rstrip():
                if debug == True:
                    print("Identified offset!")
                line = line.replace("constexpr ::std::ptrdiff_t ", "")
                line = line.replace(";", ")")
                line = line.replace("= ", "= (")
                if debug == True:
                    print("Wrote offset to pythonic form!")
            else:
                if debug == True:
                    print("Not a valid offset!")
                line = ''
                if debug == True:
                    print("Wrote an empty line!")
        with open("offsets.py", "w") as offsetwrite:
            if debug == True:
                print("Wrote data to python file!")
            offsetwrite.writelines(data)

dump(debug=False)
