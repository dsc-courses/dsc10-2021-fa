test = {   'name': 'q3_3',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(resample_means, np.ndarray)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(resample_means) == 1000\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': ">>> np.all(resample_means == mcd_mean) == False # It looks like all of your resamples have the same mean – take a closer look at how you're "
                                               'resampling!\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
