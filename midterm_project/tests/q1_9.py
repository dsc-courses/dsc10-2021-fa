test = {   'name': 'q1_9',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(chains_growth, bpd.DataFrame)\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> # Make sure chains_YOY remains unchanged.;\n'
                                               ">>> list(chains_YOY.columns)  == ['Rank', 'Restaurant', 'Sales', 'YOY_Sales', 'Segment_Category', 'Sales_2019']\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> np.all(chains_growth.get('Growth_Category').take(np.arange(10)) == np.array([4, 4, 5, 4, 4, 3, 4, 4, 4,4]))\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
