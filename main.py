import requests
import time
from plyer import notification

def get_fees():
    url = "https://mempool.space/api/v1/fees/recommended"
    response = requests.get(url)
    fees = response.json()
    return fees['halfHourFee']  # adjust this key based on the actual JSON response

def notify(fee):
    notification.notify(
        title='Bitcoin Fee Alert',
        message=f'Current low priority fee: {fee} sat/vB',
        app_icon=None,  # You can specify an .ico file path here for the notification icon
        timeout=20,
    )

target_fee = 20
print("Script started. Monitoring Bitcoin fees...")

while True:
    current_fee = get_fees()
    print(f"Checked fees: {current_fee} sat/vB")  # Log the current fee
    if current_fee <= target_fee:
        print(f"Triggering notification for fee: {current_fee} sat/vB")
        notify(current_fee)
    else:
        print(f"No notification. Fee {current_fee} sat/vB is above the target of {target_fee} sat/vB")
    time.sleep(120)  # Sleep for 30 minutes
