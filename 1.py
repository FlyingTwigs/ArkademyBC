import json


def data_diri():
    data = {'name': 'Theodore Fabian Rudy',
            'address': 'Magelang, Central Java',
            'hobbies': ['Game', 'Reading'],
            'is_married': False,
            'school': {'highSchool': "SMA Negeri 1 Magelang",
                       'university': ""},
            'skills': [{'name': 'Singing', 'score': 'Decent'},
                       {'name': 'Slacking Off', 'score': 'Master'}],
            }
    result = json.dumps(data, indent=4)
    print(result)


data_diri()
