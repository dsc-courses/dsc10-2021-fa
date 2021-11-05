test = {   'name': 'q03',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> expectancy_per_group_test = recent_sample.groupby("Status").mean().get(["Life expectancy"]);\n'
                                               ">>> np.isclose(expectancy_per_group.loc['Developed'].iloc[0], expectancy_per_group_test.loc['Developed'].iloc[0]) \n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
