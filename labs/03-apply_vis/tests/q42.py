test = {   'name': 'q42',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> 'Total_Pay_Dollars' in compensation.columns\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': '>>> t = compensation.sort_values("Total_Pay_Dollars", ascending=False);\n>>> t.get(\'Total_Pay_Dollars\').values[0] == 53250000.0\nTrue',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
