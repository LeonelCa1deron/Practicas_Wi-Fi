import network
import ubinascii

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print(mac)

print(wlan.config('channel'))
print(wlan.config('essid'))
print(wlan.config('txpower'))