# pathlib is a module
from pathlib import Path

path=Path()

# print(path.exists()) -to check if path exists
# print(path.mkdir())  -to mk new directory if does not exist
# print(path.rmdir())  -to remov directory in path
#  path.glob(' to iterate whatever dir,files .extenstion ') generator object

for files in path.glob("*.py"):     # forms a list display all .py files in path
    print(files)
