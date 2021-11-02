import cmath
from rich.console import Console
from rich.traceback import install
from rich import print
install()
console = Console()

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n1r, n1c = num1.split('+')
        n2r, n2c = num2.split('+')
        console.log(log_locals=True)
        n1 = complex(int(n1r), int(n1c[:-1]))
        n2 = complex(int(n2r), int(n2c[:-1]))
        ans = n1*n2
        real = ans.real
        imag = ans.imag
        return f"{int(real)}+{int(imag)}i"

        
num1 = "1+-1i"
num2 = "1+-1i"
Solution().complexNumberMultiply(num1, num2)
