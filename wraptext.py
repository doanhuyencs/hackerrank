import textwrap
def wrap(string, max):
    a = textwrap.fill(string, max)
    return a

string, max = input(), int(input())
print(wrap(string, max))
