# Short Term Forecasting on Air Pollutants of Delhi
<br>
With the spirit of reproducible research, this repository contains all the codes required to produce the results in the manuscript:
<br> <br>

> Alparslan, B., Dev, S., Short Term Forecasting on Atmospheric Air Pollutants Using SARIMA Method, *under review*.

Throuhout this project, `python3` is used.

### Dependencies

numpy: `pip3 install numpy`  
pandas 1.0.5: `pip3 install pandas` <br>
matplotlib 3.3.0: `pip3 install matplotlib` <br>
statsmodels 0.11.1: `pip3 install statsmodels` <br>
selenium 3.141.0: `pip3 install selenium` <br>
pynput 1.6.8: `pip3 install pynput `

### Data
Source of the data used in this work is Central Control Room for Air Quality Management - Delhi NCR ([See here](https://app.cpcbccr.com/ccr/#/caaqm-dashboard/caaqm-landing/caaqm-comparison-data)). You can reach the samples used in this work from [here](https://drive.google.com/drive/folders/1sIITvGDrgwuL7oD5GS2AbD_0d4TyzOYL?usp=sharing).

### Scripts
- `automate.py`: This file is used to download the required data files from above-mentioned link automatically. One can download the csv files directly from the second link in the data seciton or run this python file.
- `defns.py`: Definitions of some functions used in `automate.py`.
- `ljungbox.py`:
- `short-term-fcast-sarima.ipynb`:
