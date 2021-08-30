from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()
import math


all_equal = True
for p in range(1, 100):
    for s in range(1, 100):
        if int(math.ceil(p/s)) != ((p-1) // (s+1)):
            all_equal = False
            print(f"Failed at p={p}/s={s}")
            print(f"{int(math.ceil(p/s))} != {((p-1) // (s+1))}")

if all_equal:
    print("Safe")
else:
    print("not safe")