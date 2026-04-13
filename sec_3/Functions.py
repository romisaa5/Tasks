# تعريف دالة بـ def
def my_sum(start, end):
    result = 0
    for i in range(start, end+1):
        result += i
    return result

print(my_sum(10, 20))   # 165

# default argument
def greet(name, country="Egypt"):
    print(name, "from", country)
greet("Ali")             # Ali from Egypt

# *args → tuple من arguments
def f(*kids):
    print(kids[2])        # العنصر الثالث