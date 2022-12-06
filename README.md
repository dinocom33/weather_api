# Weather API
This simple script makes a request to https://home.openweathermap.org/ and displays the current weather, temperature(+ feels like), humidity and wind speed for the city set by the user.
In order to use it, you will need to register in https://home.openweathermap.org/users/sign_in, which is free (no credit card required), to generate an API key that you need to put in the script. You also need to install Python module "requests"(pip install requests) to be able to send requests to this API.
The response to the request is returned as a Jason file. All details about it can be found at the following link:
https://openweathermap.org/current

My idea is that this script, with some improvements and additions, will become an addon for Home Assistant.

Below you can see some screenshots of the script execution.

![image](https://user-images.githubusercontent.com/59865649/202232030-bba87246-af29-4620-9ff6-cc509d4598d6.png)

![image](https://user-images.githubusercontent.com/59865649/202232457-a57314f7-31f3-4a0f-8f09-9b5127d4b548.png)

![image](https://user-images.githubusercontent.com/59865649/202232609-b438fdb3-e89c-49c6-b80f-bb0b5ce0af88.png)

If the specified city name is wrong, or is not in the site's database, or your API key has expired, you will receive an error message like the one below:

![image](https://user-images.githubusercontent.com/59865649/202233805-e84b67a9-168a-4997-b16d-fd7eaf2c7b66.png)

