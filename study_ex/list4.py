vec = [-4, 2, -1, 5, 6]
print(vec)

vec2 = [x*2 for x in vec]
print(vec2)

vec3 = [x for x in vec if x>0]
print(vec3)

vec4 = [abs(x) for x in vec]
print(vec4)

freshfruit = ['  banana','  loganberry  ','passsion fruit   ']
print(freshfruit)

print([weapon.strip() for weapon in freshfruit])
print(freshfruit)

x2x = [(x, x**2) for x in range(10)]
print(x2x)

mi2 = [(x, 2**x) for x in range(32)]
print(mi2)

