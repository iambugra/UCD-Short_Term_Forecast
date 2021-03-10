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
pynput 1.6.8: `pip3 install pynput ` <br>
statistics 1.0.3.5: `pip3 install statistics` <br>
sklearn 0.23.2: `pip3 install sklearn`

### Data
Source of the data used in this work is Central Control Room for Air Quality Management - Delhi NCR ([See here](https://app.cpcbccr.com/ccr/#/caaqm-dashboard/caaqm-landing/caaqm-comparison-data)). You can reach the samples used in this work from [here](https://drive.google.com/drive/folders/1sIITvGDrgwuL7oD5GS2AbD_0d4TyzOYL?usp=sharing).

### Scripts
- `automate.py`: This file is used to download the required data files from above-mentioned link automatically. One can download the csv files directly from the second link in the data section or run this python file (downloaded excel files should be saved as csv files).
- `defns.py`: Definitions of some functions used in `automate.py`.
- `stropns.py`: Some string operations.
- `ljungbox.py`: Implementation of Ljung-Box test. Work is done by [Bhavesh Bhatt](github.com/bhattbhavesh91/time_series_notebooks)
- `rand_5_data.txt`: 5 randomly selected samples used in this work.
- `short-term-fcast-sarima.ipynb`: A program that step by step forecasts a pollution data.
- `make_test.py`: Main program that runs the model and produces results in seperate text files.
- `read_results.py` : Evaluates the results from `make_test.py` and creates the statistics of __Results__ section in the paper.
