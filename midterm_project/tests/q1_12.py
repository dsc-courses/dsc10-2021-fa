test = {   'name': 'q1_12',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(invest_segment_categories, np.ndarray)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(invest_segment_categories) == 3 # Pick 3 segment categories to invest in.\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> invest_segment_categories[0] in np.unique(chains.get('Segment_Category')) # Check for a spelling mistake in your segment category.\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> invest_segment_categories[1] in np.unique(chains.get('Segment_Category')) # Check for a spelling mistake in your segment category.\nTrue",
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': ">>> invest_segment_categories[2] in np.unique(chains.get('Segment_Category')) # Check for a spelling mistake in your segment category.\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}