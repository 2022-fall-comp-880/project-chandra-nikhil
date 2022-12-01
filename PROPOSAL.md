# Currency Exchange Rate comparison

**Author**: Bala Chandra Sekhar Reddy Jannavarapu & Nikhileswar Reddy
**Date**: 11/16/2022


## Motivation 

What specific investigation will the project carry out?
In this project,I want to investigate about the Currency ExChange Rate comparison between indian rupee and USA dollar.


## Investigative Questions 

1. What are the exchange rate of Indian Rupee and US dollar based upon the particular date?

Result:
{date1:{'inr':'inr value','usa':'usa value'},date2:{'inr':'inr value', 'usa':'usa value'}}

First dictonary 

date: key
value : Nested dictonary of Exchange rates of the particular country 

nested dictonary
key:currency_name of that country
value:currency value of that country

2. Exchange rates of each country in range of date?

[INR:{value1,value2...},GBP:{value1,value2...}]

3.The curreny exchange rate values are extracted based upon the date?

Dictonary 
key : date
value : dictonary of currency_name,currency value

Nested dictonary
key:currency_name
value:currency_value

{
date1:{'inr':'inr value','gbp':'gbp value','eur':'eur value'}
date2:{'inr':'inr value','gbp':'gbp value','eur':'eur value'}
}

## Approach 

Description of the data set:
* The dataset  contains exchange rates of US Dollar to other currencies, i.e. 1 USD = x EUR. 
* The column index is a list of currencies and row index is a list of dates.
* The dataset describes the exchange rates of most foreign currencies to US Dollar in the past years, i.e. 1 USD = x EUR
* The economy has not been booming in recent years, so it could be interesting to look at the trends of some exchange
 rates and gain some insight out of it because exchange rates can be a great indicator of the economy.

## Expected Results 


1. List of dictionary with key value pairs with country name as keys and country exchange rate as values.
2. List of dictionary with key value pairs with country name as keys and the exchange rate of that country as values.
3. List of dictionary with key value pairs with country name as key and the value is highest exchange rate of that particular country.



## New Python Packages or Modules 

The python packages used in this module is 
1. Numpy
2. pandas
3. matplotlib
4. seaborn
5. MinMaxScaler
6. os



## Dataset Documentation

A data set is collection of relevant data.
The dataset is consists of exchange rate of each and every country form date 1/1/2012 to 10/28/2022.
The row values are the dates and the currency names are in column.
The exchange rates of each country are mapped as per the date in the rows


It has 3955 rows and 53 columns of data

Author : Boyuan Lyu
Last updated ; 21 days ago

