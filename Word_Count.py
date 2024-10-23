a="hi there how u doing today how how"
def Count():
    c=0
    b="how"
    for i in a.split(" "):
      if i==b:
         c=c+1
    return c

print(Count())