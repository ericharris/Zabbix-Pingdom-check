# Zabbix-Pingdom-check
This script was created to be used by Zabbix to check the status of a Pingdom check. It could be expanded to other uses fairly easily.

## Script usage
There are six command line arguments, 5 of which are required.
```bash
check_pingdom -u <api-url> -i <check-id> -k <app-key> -a <pingdom-username> -p <pingdom-password>
```
* -h shows the command line arguments
* -u is the API url for the check you are performing
* -i is the check ID that you want a status of
* -k is the application key you setup in Pingdom
* -a is the Pingdom username
* -p is the Pingdom password

The script has some error checking, and will return the text of errors supplied by Pingdom. It should also supply the error message when the script is not getting the Pingdom errors (connectivity, wrong API url, etc.)

I have setup Zabbix to pass these parameters to the check script, as shown below.

## Pingdom Setup
You will need to get an App-Key from your Pingdom account, and obtain the check's ID number.

To get an application key, you'll need to go to "Sharing", and then "The Pingdom API" where you can add keys.
![Pingdom App-Key](http://ericharris.github.io/repositories/Zabbix-Pingdom-check/images/PingdomAppKey.png)

To get your check's ID number, you can edit the check and see the ID in the URL.
![Pingdom Check ID](http://ericharris.github.io/repositories/Zabbix-Pingdom-check/images/PingdomFetchCheckID.png)

## Zabbix Setup
To get the check working in Zabbix, I set it up as a new Host.
![Zabbix Host Config](http://ericharris.github.io/repositories/Zabbix-Pingdom-check/images/ZabbixHostConfig.png)

Setup Macros on the host so that you can save and pass the URL, AppKey, username and password arguments.
![Zabbix Macros](http://ericharris.github.io/repositories/Zabbix-Pingdom-check/images/ZabbixMacros.png)

You can then setup an external check item for each service check you want to monitor. Here's the string I used for the key value. Note that you need to set the check ID value after "-i" manually.
```bash
check_pingdom.py["-u","{$PINGDOM_URL}","-i","00000","-k","{$PINGDOM_APPKEY}","-a","{$PINGDOM_USER}","-p","{$PINGDOM_PASSWORD}"]
```
![Zabbix Item](http://ericharris.github.io/repositories/Zabbix-Pingdom-check/images/ZabbixItem.png)

And finally, the trigger can be setup. The script returns the status text, so set it to trigger on anything other than "up".
![Zabbix Trigger](http://ericharris.github.io/repositories/Zabbix-Pingdom-check/images/ZabbixTrigger.png)
