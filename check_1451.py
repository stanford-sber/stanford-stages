

import sklearn.metrics

# read in data from LSTM auto scoring
with open('data/1451_edf_autostage_test.hypnogram.txt', 'r') as f:
    ss_hypno = f.read().split('\n')

# downsample
ss_hypno = ss_hypno[0:len(ss_hypno):2]

# read in data from profusion
with open('data/1451_profusion_hypno.txt', 'r') as f:
    pf_hypno = f.read().split('\n')

# dictionary to translate values in hypnogram
translate_dict = {'0': '?',
                  '1': 'N1',
                  '2': 'N2',
                  '3': 'N3',
                  '4': 'N4',
                  '5': 'R'}

# replace values in ss hypnogram with profusion scoring labels
for i, v in enumerate(ss_hypno):
    ss_hypno[i] = translate_dict[v]

# calculate cohens kappa
sklearn.metrics.cohen_kappa_score(ss_hypno[0:len(pf_hypno)], pf_hypno[0:len(ss_hypno)])