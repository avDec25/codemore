vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
def countVowels(s: str) -> int:
  count = 0
  for x in s:
    if x in vowels:
      count = count + 1
  return count

def halvesAreAlike(s: str) -> bool:
  n = len(s)
  fh = countVowels(s[0:n//2])
  sh = countVowels(s[n//2:n])
  if fh == sh:
    return True
  else:
    return False


print(halvesAreAlike("ZbCdEfGh"))