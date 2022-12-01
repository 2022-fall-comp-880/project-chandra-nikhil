COMP-880 Integrated Practicum - Fall 2022 - Project
Design Document
Authors : Bala Chandra, Nikhil

## Algorithm for Class ExchangeRates
* The class `ExchangeRates` contains three methods to develop the script for the investigative questions.
* The methods are write method ,exchange_rates_country method,exchange_rates_range_of_dates method,exchangerate_on_date method,read_dataset method.
* The main method is used to run the example code with some print statements.

## Algorithm for write function

* This method is to write a CSV file with exchange rates data.
* Open the file in write 'w' mode by using the `open()
* In for loop, iterate the variables date,currency_name,currency_value in exchangerate info
* Create a variable exchangerate_info_row and assign it with the date,currency_name,currency_value by using the f-string.
* Write the exchangerate_info_row into the file opened in write mode.

## Algorithm for exchange_rates_by_country
* Create a empty dictionary to store the output 
* Iterate the for loop until the key value pairs of Indian Rupee and European Euro
* Create a variable date to store the date value
* create a empty variable val ,to store the exchange rate of particular country.
* The nested dictionary will be created.
* Dictonary 
  date: key
  value : Nested dictonary of Exchange rates of the particular country 
* nested dictonary
   key:currency_name of that country
   value:currency value of that country
## Algorithm for exchange_rates_range_by_dates
* Create a empty list to store the output .
* Create a variable date to store the range of date.
* Based upon the given range of date the exchange rates are returned.
* In dictionary the  keys is Currency name and the value is exchange rate of that particular country.
* List of dictionary will be returned.

## Algorithm for exchangerate_by_date
* Create a empty dictionary to stor the output.
*  Iterate the for loop until the key value pairs of exchange rates of each country of that particular date generated.
* Create a variable date to store the date value.
* create a empty variable val ,to store the exchange rate of particular country.
* The nested dictionary will be created.
* Dictionary 
key : date
value : dictionary of currency_name,currency value

Nested dictionary
key:currency_name
value:currency_value


# Algorithm for read_dataset

* Step 1: Create variable player_data and initialize it with empty list.
* Step 2:Crete variable fp and assign the open the file in the reading mode.( Need to open the files from the tests folder)
*	Step 3: In for loop, iterate the content of the file.
*	Step 4: Create a variable as tmp and split the file by using the split funtion.
*	Step 5: store the values to the tmp1 variable.
*	Step 6: create a variable x and removes any leading (spaces at the beginning) and trailing (spaces at the end) characters) by using strip method.
*	Step 7: By using the append function ,append the values to the tmp1 variable.
*	Step 8: close the opened file with reading mode.
*	step 9: Finally it returns the PlayerData
