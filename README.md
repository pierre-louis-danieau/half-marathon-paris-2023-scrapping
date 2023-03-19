# Scrapping of the Paris 2023 half marathon results

## Context

The objective of this directory is to present a method used to obtain the results of 45000 runners of the Paris 2023 half marathon in a structured data format.

All the public results can be found on this page : [results](https://resultscui.active.com/events/HarmonieMutuelleSemideParis2023)

<img width="1106" alt="Capture d’écran 2023-03-19 à 11 38 19" src="https://user-images.githubusercontent.com/67114372/226169847-8ead76bb-955f-415c-a71b-a4959859a708.png">

We then want to automate the collection of these data.

The results are in the file `results.csv`.

Overview of results: 

<img width="575" alt="Capture d’écran 2023-03-19 à 11 41 55" src="https://user-images.githubusercontent.com/67114372/226170033-f3c7ed37-39d2-43c2-b743-dcf3274fab7c.png">

It takes around 13 hours to execute the `final_semi_marathon.py` as it takes a long time to load the whole page (press "load more" and wait for the page to load 850 times)

## Stack 

- Python
- [Undetected Chrome driver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) in order to avoid being detected as a bot. Thanks  [ultrafunkamsterdam](https://github.com/ultrafunkamsterdam). 👏👏
- Selenium to scroll the page
- Beautiful soup to parse the web page


## Execute the code locally

1. Clone this repo with `git clone`

2. Create a virtual env and activate it

`virtualenv env`

`source env/bin/activate`

3. Install the dependencies

`pip install -r requirements.txt`

4. Execute the main code

`python3 final_semi_marathon.py`

## Backtesting : 

- With `charger_plus_function(driver, n=10)` it takes around 3 minutes to get the 550 first results.

- With `charger_plus_function(driver, n=900)` it takes around 13 hours to get the 45k (all) results.
