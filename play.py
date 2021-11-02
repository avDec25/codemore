from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()

for i in range(10):
    console.log(log_locals=True)
    print(i)