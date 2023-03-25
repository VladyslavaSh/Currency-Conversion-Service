# Currency-Conversion-Service
The Python program that provides non-direct currency conversions using an intermediate currency.

## Description:
This code creates a web service that allows clients to perform currency conversions that involve an intermediate currency. This means that a currency can be converted to another currency indirectly. For example we can convert USD to EUR like USD to UAH and UAH to EUR, where UAH is considered a third-party currency.

The code uses a currency exchange API to obtain the necessary data and performs the currency conversions using Python libraries such as NumPy. The results of the conversions are returned to the client in a dictionary format that includes conversion variants, the best conversion options for the customer and brokers, and the currencies involved in the conversion.

To use the program, execute the app.py file and open the local link http://127.0.0.1:5000 in your browser.

Libraries: requests, numpy, Flask, Flask Bootstrap

Api: https://v6.exchangerate-api.com
