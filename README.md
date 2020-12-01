[![Abcdspec-compliant](https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg)](https://github.com/brain-life/abcd-spec)
[![Run on Brainlife.io](https://img.shields.io/badge/Brainlife-bl.app.444-blue.svg)](https://doi.org/10.25663/bl.app.444)

# a Maxwell filtering app
This app applies Maxwell filtering to raw MEG data using the MNE-python implementation documented [here](https://mne.tools/stable/generated/mne.preprocessing.maxwell_filter.html#mne-preprocessing-maxwell-filter).

# documentation

This app reads in a .fif raw MEG file, applies Maxwell filtering to it, and saves the resulting data to disk.
This is a customary first processing step for any data file obtained from a MEGIN (former Elekta) MEG system. Explanation can be found [here](https://mne.tools/stable/auto_tutorials/preprocessing/plot_60_maxwell_filtering_sss.html#background-on-sss-and-maxwell-filtering).   

Expected input: a raw .fif file

Output: a processed _sss.fif or _tsss.fif file.


### Author
- [Maximilien Chaumon](maximilien.chaumon@sorbonne-universite.fr)


#### Copyright (c) 2020 brainlife.io The University of Texas at Austin and Indiana University

### Funding Acknowledgement
brainlife.io is publicly funded and for the sustainability of the project it is helpful to Acknowledge the use of the platform. We kindly ask that you acknowledge the funding below in your code and publications. Copy and past the following lines into your repository when using this code.

[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-1636893](https://img.shields.io/badge/NSF_BCS-1636893-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-ACI-1916518](https://img.shields.io/badge/NSF_ACI-1916518-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1916518)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://grantome.com/grant/NIH/R01-EB029272-01)

### Citations

## Running the App 

### On Brainlife.io

You can submit this App online at [https://doi.org/10.25663/bl.app.444](https://doi.org/10.25663/bl.app.444) via the "Execute" tab.

### Running Locally (on your machine)

1. git clone this repo.
2. Inside the cloned directory, create `config.json` with something like the following content with paths to your input files.

```json
{
  "Input": "rest.fif"
}
```

3. Launch the App by executing `main`

```bash
./main
```

### Sample Datasets

If you don't have your own input file, you can download sample datasets from Brainlife.io, or you can use [Brainlife CLI](https://github.com/brain-life/cli).

```
npm install -g brainlife
bl login
mkdir input
bl dataset download 5a0f0fad2c214c9ba8624376#5a050966eec2b300611abff2 && mv 5a0f0fad2c214c9ba8624376#5a050966eec2b300611abff2 .
```

## Output

All output file (a resampled T1w NIFTI-1 file) will be generated inside the current working directory (pwd), inside a specifc directory called:

```
out_dir
```

### Dependencies

This App only requires DIPY.org to run. 
