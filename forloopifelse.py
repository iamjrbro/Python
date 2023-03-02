'''
FOR LOOP INSIDE A IF/ELSE CONDITION

Used to automitize messages, like emails.
'''

# This example will send an email with details of an online purchase (with a maximum of 3 attempts to make) for confirmed purchases only
# You can choose if the condition will be True or False

confirmedpurchase = True
purchasedetails = 'Purchase confirmed and being prepared for shipment'

for send in range(3):
    if confirmedpurchase:
        print(purchasedetails)
        print('Tracking details will be sent to your email')
        break
    else:
        print('Purchase failed')