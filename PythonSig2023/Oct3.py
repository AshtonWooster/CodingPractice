x = []
y = ()

for i in range(10):
    x.append(str(i))
x[5] = 5

def has_type(l, t):
    for i in range(len(l)):
        if isinstance(l, t):
            return True
    return False

print(has_type(x, int))

if hasattr(y, "sort"):
    print("Yes!")
else:
    print("No!")

def pedantic_function(x: [list, dict[str, any]]):
    try:
        x[0]
    except Exception as e:
        raise e from None

print(pedantic_function(5))
