from time import process_time_ns


DATA = [
    {
        'name': 'Carlos',
        'age': 72,
        'organization': 'Ciancoders',
        'position': 'Technical Leader',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Ciancoders',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 35,
        'organization': 'Ciancoders',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'internship',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    # Comprehensions solutions

    # 1. obtener todos los desarrolladores de python
    dev_python = [dev for dev in DATA if dev['language'] == 'python']
    #print(dev_python)

    # 2. obtener todos los desarrolladores de python que tienen una edad mayor a 20
    dev_python20 = [ dev for dev in DATA if dev['language'] == 'python' and dev['age'] > 20]
    #print(dev_python20)
              
    # 3. obtener todos los trabajadores de ciancoders
    devs = [dev for dev in DATA if dev['organization'] == 'Ciancoders']
    #print(devs)

    # 4. obtener todos los trabajadores de ciancoders que tienen una edad mayor a 30
    devs30 = [dev for dev in DATA if dev['organization'] == 'Ciancoders' and dev['age'] > 30]
    #print(devs30)

    # 5. obtener todos los trabajadores de mayores de 18 años
    devs18 = [dev for dev in DATA if dev['age'] > 18]
    print(devs18)

    # 6. obtener todos los trabajadores de mayores a 70 años
    devs70 = [dev for dev in DATA if dev['age'] > 70]
    #print(devs70)
    


if __name__ == '__main__':
    run()
