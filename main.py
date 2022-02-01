# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

def greet(name, greeting_template = 'Hello, <name>!'):
        if '<name>' in greeting_template:
            greeting_template = greeting_template[:greeting_template.find("<")] + name + greeting_template[greeting_template.find('>') +1:]
            return greeting_template
        else:
            #if the user forget to put <name> 
            return f'{greeting_template} {name}'
        


gravity = {
    'sun' : 274,
    'jupiter' : 24.92,
    'neptune' : 11.15,
    'saturn' : 10.44,
    'earth' : 9.798,
    'uranus': 8.87,
    'venus' : 8.87,
    'mars' : 3.71,
    'mercury' : 3.7,
    'moon' : 1.62,
    'pluto' : 0.58
}

def force(mass,body ='earth'):
    force_of_item = mass * round(gravity[body], 1)
    return force_of_item

def pull(m1, m2, d):
    g = 6.674*(10**-11)
    f = g *((m1 * m2) /d ** 2)
    return f

print(greet('bob' ,'hello <name> how are you'))