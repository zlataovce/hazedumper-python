# hazedumper-python
A python module for parsing up-to date CS:GO offsets for use in Python

All credit for the offsets goes to the maintainers of the [hazedumper repository](https://github.com/frk1/hazedumper).

Using only modules from Python's default library.

## Usage
 - Copy the hazedumper.py from the repository.
 - Run the dump function and grab the offsets from the returned dict.

### Example
```
from hazedumper import dump

offsets = dump()

print("dwForceAttack: " + offsets["dwForceAttack"])
print("m_iFOV: " + offsets["m_iFOV"])
```
 
## Contribution
If you can contribute to this repository, you are welcome to do so. Just create a pull request.
Or if you have any ideas for functions to implement, please make an issue with the tag enhancement.
