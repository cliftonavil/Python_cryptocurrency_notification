# cliftonavil@gmail.com
import urllib.request, json
from win10toast import ToastNotifier
import schedule
import time

#MAKE SURE YOUR WINDOWS 10 NOTIFICATION IS ON
print("---few sample Coin Name---")
print("1) bitcoin"
      " 2) edgeless"
      " 3) ripple"
      " 4) litecoin")
print("--------------------------")
coin_name =input("ENTER COIN NAME :")
print('Notification Started.. please wait for Just 1 Minute')
try:
    def job():
        #coin_name="bitcoin"   #For default coin
        toast = ToastNotifier()  # Notifiction function
        #Source for Coin Data feed
        with urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/" + str(coin_name) + "/?convert=INR") as url:
            data = json.loads(url.read().decode())
        name = data[0]['name']  # Name of Coin
        btc_value = data[0]['price_btc']  # Value in terms of Bitcoin
        dollar_value = data[0]['price_usd'] # Bitcin value against Bitcin
        in_rupees = data[0]['price_inr']    # Value of Coin in Indian Rupees
        check = float(data[0]['percent_change_1h'])# % Change for 1 Hour only
        print('Name:', name)
        print('BTC value:', btc_value)
        print('Dollar Rate:', dollar_value)
        print('Rupee Rate:', in_rupees)


        if check > 0:
            print("Green: +", check, "%") # % Change for 1 Hour only
            print("------Completed 1 Minute--------")
            toast.show_toast("Name : " + name + "\nBTC Value :" + btc_value,
                         "In $ :" + dollar_value + "\nINR :" + in_rupees , icon_path="green.ico",
                         duration=50)
        else:
            print("Red:", check, "%")
            print("------Completed 1 Minute--------")
            toast.show_toast("Name : " + name + "\nBTC Value :" + btc_value,
                             "In $ :" + dollar_value + "\nINR  :" + in_rupees, icon_path="red.ico",
                             duration=50)
    schedule.every(1).minutes.do(job)#seting time for  in Minutes
    #schedule.every().hour.do(job)# Set 1 Notifcation for 1 Hour
    while 1:
        schedule.run_pending()
        time.sleep(1)
except:
        print("Somethig went wrong")