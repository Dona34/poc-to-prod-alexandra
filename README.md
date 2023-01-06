# Poc-to-prod

The goal is to predict some #thematic linked to a title forum from stackoverflow. We want to return the top-k predictions #thematics from 50 available for a given title, to automate the process of #.

## Description

We went from the test_utils realisation and functions implementation in utils, to an API that can return the top-k thematics from your given title, passing by the realization of train and predict files, with their tests associated.

## Getting Started

### Dependencies

* It was done with python 3.10.9 64 bit
* conda

### Installing
```
git clone https://github.com/Dona34/poc-to-prod-alexandra.git
```
```
conda env create -n poctoprod
```
```
conda activate poctoprod
```

### Executing program

* How to run the program:
```
python3 ./predict/predict/app.py
```
For example, we want to know which topic is linked to "I don't understand this php error" :
```
curl -X POST -H "Content-Type: application/json" -d '{"text": ["I don't understand this php error"], "topk":5}' http://localhost:5000/predict_request
```

## Help

If the curl doesn't work on http://localhost:5000/predict_request, you can go directly in ./predict/predict/app.py and change the variable "text" manually.
Itwill appear on http://localhost:5000/predict_text

## Author

Contributor name

ex. Dominique Pizzie  
ex. [@Dona34](https://github.com/Dona34)

