
# set up environment
import json
import mne

# load inputs from config.json
with open('config.json') as config_json:
	config = json.load(config_json)

data_file = str(config.pop('input'))

raw = mne.io.read_raw_fif(data_file,allow_maxshield=True)

raw_sss = mne.preprocessing.maxwell_filter(raw,**config['params'])
 
raw_sss.save(raw_sss.filenames[0].replace('.fif','_%s.fif' %config['output_tag']))
