import requests

headers={
    'authorization': 'Token Here'
}

while True:
    r = requests.put('https://discord.com/api/v6/channels/GROUPID/recipients/USERID', headers=headers)
    if r.status_code == 204:
        print('Success')
    if r.status_code == 400:
        print('Unauthorized')
    else:
        print('Somthing Fucked Up')
# I Was Just Fucking Around With This Shit Lol, Not Ment To Look Good lol
