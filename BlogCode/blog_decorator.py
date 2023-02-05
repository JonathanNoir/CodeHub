
#Example 1: --------------------------------------------------
def weapon_decorator(func):
    def wrapper():
        print("Dark Knight equips a new weapon ====")
        func()
        print("Dark Knight discards the used weapon ^^^")
        print('')
    return wrapper

@weapon_decorator
def fight_with_sword():
    print("Dark Knight fights with a sword")

@weapon_decorator
def fight_with_axe():
    print("Dark Knight fights with an axe")

@weapon_decorator
def fight_with_bow():
    print("Dark Knight fights with a bow")

#Execute the method
fight_with_sword()
fight_with_axe()


#Example 2: --------------------------------------------------
def log_decorator(func):
    def wrapper():
        print(f"== Calling: {func.__name__}() Before ==")
        func()
        print(f"*** calling {func.__name__}() after ***")
        print('')
    return wrapper

def eng_greeting():
    print('Hi there !')

#Execute the method
greet = log_decorator(eng_greeting)
greet()

#Using the Decorator
@log_decorator
def fr_greeting():
    print('Bonjour.')

#Execute the method
fr_greeting()

#Example 3: --------------------------------------------------
def reverse_decorator(func):
    def wrapper():
       #return func()[::-1]
       return ''.join(reversed(func()))
    return wrapper

@reverse_decorator    
def bye_greeting():
    return'Goodbye !'

#Execute the method
bye_greeting()

def cap_decorator(func):
    def wrapper():
       return func().capitalize()
    return wrapper

@reverse_decorator  
@cap_decorator  
def say_hello():
    return 'hello'
#Execute the method
say_hello()


#Example 4: --------------------------------------------------
def log_decorator_arg(func):
    def wrapper(*args, **kwargs):
        print(f"== Calling: {func.__name__}() Before ==")
        result =  func(*args, **kwargs)
        print(f"*** calling {func.__name__}() after ***")
        print('')
        return result
    return wrapper

@log_decorator_arg
def multiply(i:int, j:int) -> int:
    return i * j

#Execute the method
multiply(8,6)

#Example 5: --------------------------------------------------
class DarkKnight:
    def __init__(self):
        self.weapons = ['sword']
        
    def weapon_decorator(func):
        def wrapper(self, *args, **kwargs):
            print(f"Dark Knight equips {args[0]}")
            func(self, *args, **kwargs)
            print(f"Dark Knight discards {args[0]}")
        return wrapper
    
    @weapon_decorator
    def fight(self, weapon):
        self.weapons.append(weapon)
        print(f"Dark Knight fights with {weapon}")

#Execute the method
bruce_wayne = DarkKnight()
bruce_wayne.fight('axe')
bruce_wayne.fight('bow')

