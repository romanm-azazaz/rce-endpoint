# rce-endpoint
Simple python http server to demonstrate RCE vulnerabilities.

### Run
```
lomaha@ping-pong % python3 main.py -a=0.0.0.0 -p=80
```
### Use
#### Client side:
```
lomaha@rce-endpoint % curl -G "http://127.0.0.1/ping?ip=8.8.8.8;ls"

b'PING 8.8.8.8 (8.8.8.8): 56 data bytes\n64 bytes from 8.8.8.8: icmp_seq=0 ttl=111 time=5.806 ms\n64 bytes from 8.8.8.8: icmp_seq=1 ttl=111 time=7.035 ms\n64 bytes from 8.8.8.8: icmp_seq=2 ttl=111 time=17.179 ms\n\n--- 8.8.8.8 ping statistics ---\n3 packets transmitted, 3 packets received, 0.0% packet loss\nround-trip min/avg/max/stddev = 5.806/10.007/17.179/5.096 ms\n.git\nREADME.md\nmain.py\n'
```
#### Server side:
```
Server started http://127.0.0.1:80
127.0.0.1 - - [25/Dec/2021 19:20:31] "GET /ping?ip=8.8.8.8;ls HTTP/1.1" 200 -
path: '/ping'
query_params: 'ip'
quer_value: '8.8.8.8;ls'
```