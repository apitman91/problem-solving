# OverTheWire - Bandit

## [Bandit Level 0 → Level 1](http://overthewire.org/wargames/bandit/bandit1.html)

### solution:
```
ssh -p 2220 bandit0@bandit.labs.overthewire.org
```
password: **bandit0**<br>
once logged in:
```
cat readme
```
 password for level 1: **boJ9jbbUNNfktd78OOpsqOltutMc3MY1**

## [Bandit Level 1 → Level 2](http://overthewire.org/wargames/bandit/bandit2.html)

### solution:
```
cat ./-
```
password for level 2: **CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9**

#### References:
https://unix.stackexchange.com/questions/16357/usage-of-dash-in-place-of-a-filename

## [Bandit Level 2 → Level 3](http://overthewire.org/wargames/bandit/bandit3.html)

### Solution:
```
cat ./spaces\ in\ this\ filename
```
password for level 3: **UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK**

## [Bandit Level 3 → Level 4](http://overthewire.org/wargames/bandit/bandit4.html)

### Solution:
```
cat inhere/.hidden
```
password for level 4: **pIwrPrtPN36QITSp3EQaw936yaFoFgAB**

## [Bandit Level 4 → Level 5](http://overthewire.org/wargames/bandit/bandit5.html)

### Solution:
```bash
bandit4@bandit:~$ file ./inhere/*
./inhere/-file00: data
./inhere/-file01: data
./inhere/-file02: data
./inhere/-file03: data
./inhere/-file04: data
./inhere/-file05: data
./inhere/-file06: data
./inhere/-file07: ASCII text
./inhere/-file08: data
./inhere/-file09: data
bandit4@bandit:~$ cat ./inhere/-file07 
koReBOKuIDDepwhWk7jZC0RTdopnAYKh
```

## [Bandit Level 5 → Level 6](http://overthewire.org/wargames/bandit/bandit6.html)

### Solution:
```bash
bandit5@bandit:~$ find . -type f -size 1033c ! -executable 
./inhere/maybehere07/.file2
bandit5@bandit:~$ cat ./inhere/maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

## [Bandit Level 6 → Level 7](http://overthewire.org/wargames/bandit/bandit7.html)

### Solution:
```bash
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2> /dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password 
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

## [Bandit Level 7 → Level 8](http://overthewire.org/wargames/bandit/bandit8.html)

### Solution:
```
bandit7@bandit:~$ grep millionth data.txt 
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

## [Bandit Level 8 → Level 9](http://overthewire.org/wargames/bandit/bandit9.html)

### Solution:
```
bandit8@bandit:~$ sort data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

## [Bandit Level 9 → Level 10](http://overthewire.org/wargames/bandit/bandit10.html)

### Solution:
```
bandit9@bandit:~$ strings data.txt | grep "="
2========== the
========== password
>t=	yP
rV~dHm=
========== isa
=FQ?P\U
=	F[
pb=x
J;m=
=)$=
========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk
iv8!=
```

## [Bandit Level 10 → Level 11](http://overthewire.org/wargames/bandit/bandit11.html)

### Solution:
```
bandit10@bandit:~$ base64 -d data.txt 
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

## [Bandit Level 11 → Level 12](http://overthewire.org/wargames/bandit/bandit12.html)

### Solution:
```
bandit11@bandit:~$ cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```

## [Bandit Level 12 → Level 13](http://overthewire.org/wargames/bandit/bandit13.html)

### Solution:
```bash
bandit12@bandit:~$ mkdir /tmp/some-unique-dir
bandit12@bandit:~$ cp data.txt /tmp/some-unique-dir
bandit12@bandit:~$ cd /tmp/some-unique-dir
bandit12@bandit:/tmp/some-unique-dir$ xxd -r data.txt dump
bandit12@bandit:/tmp/some-unique-dir$ file dump
dump: gzip compressed data, was "data2.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/some-unique-dir$ mv dump dump.gz
bandit12@bandit:/tmp/some-unique-dir$ gzip -d dump.gz 
bandit12@bandit:/tmp/some-unique-dir$ ls
data.txt  dump
bandit12@bandit:/tmp/some-unique-dir$ file dump
dump: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/some-unique-dir$ mv dump dump.bz
bandit12@bandit:/tmp/some-unique-dir$ bzip2 -d dump.bz
bandit12@bandit:/tmp/some-unique-dir$ ls
data.txt  dump
bandit12@bandit:/tmp/some-unique-dir$ file dump
dump: gzip compressed data, was "data4.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/some-unique-dir$ mv dump dump.gz
bandit12@bandit:/tmp/some-unique-dir$ gzip -d dump.gz 
bandit12@bandit:/tmp/some-unique-dir$ ls
data.txt  dump
bandit12@bandit:/tmp/some-unique-dir$ file dump
dump: POSIX tar archive (GNU)
bandit12@bandit:/tmp/some-unique-dir$ mv dump dump.tar
bandit12@bandit:/tmp/some-unique-dir$ tar -xf dump.tar 
bandit12@bandit:/tmp/some-unique-dir$ ls
data5.bin  data.txt  dump.tar
bandit12@bandit:/tmp/some-unique-dir$ file data5.bin 
data5.bin: POSIX tar archive (GNU)
bandit12@bandit:/tmp/some-unique-dir$ mv data5.bin data5.tar
bandit12@bandit:/tmp/some-unique-dir$ tar -xf data5.tar
bandit12@bandit:/tmp/some-unique-dir$ ls
data5.tar  data6.bin  data.txt  dump.tar
bandit12@bandit:/tmp/some-unique-dir$ file data6.bin
data6.bin: bzip2 compressed data, block size = 900k
bandit12@bandit:/tmp/some-unique-dir$ mv data6.bin data6.bz
bandit12@bandit:/tmp/some-unique-dir$ bzip2 -d data6.bz
bandit12@bandit:/tmp/some-unique-dir$ ls
data5.tar  data6  data.txt  dump.tar
bandit12@bandit:/tmp/some-unique-dir$ file data6
data6: POSIX tar archive (GNU)
bandit12@bandit:/tmp/some-unique-dir$ mv data6 data6.tar
bandit12@bandit:/tmp/some-unique-dir$ tar -xf data6.tar 
bandit12@bandit:/tmp/some-unique-dir$ ls
data5.tar  data6.tar  data8.bin  data.txt  dump.tar
bandit12@bandit:/tmp/some-unique-dir$ file data8.bin 
data8.bin: gzip compressed data, was "data9.bin", last modified: Tue Oct 16 12:00:23 2018, max compression, from Unix
bandit12@bandit:/tmp/some-unique-dir$ mv data8.bin data8.gz
bandit12@bandit:/tmp/some-unique-dir$ gzip -d data8.gz 
bandit12@bandit:/tmp/some-unique-dir$ ls
data5.tar  data6.tar  data8  data.txt  dump.tar
bandit12@bandit:/tmp/some-unique-dir$ file data8
data8: ASCII text
bandit12@bandit:/tmp/some-unique-dir$ cat data8
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL
```

## [Bandit Level 13 → Level 14](http://overthewire.org/wargames/bandit/bandit14.html)

### Solution:
```bash
bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost
bandit14@bandit:~$ cat /etc/bandit_pass/bandit14 
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
```

## [Bandit Level 14 → Level 15](http://overthewire.org/wargames/bandit/bandit15.html)

### Solution:
```bash
bandit14@bandit:~$ nc localhost 30000
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr
```

## [Bandit Level 15 → Level 16](http://overthewire.org/wargames/bandit/bandit16.html)

### Solution:
```bash
bandit14@bandit:~$ openssl s_client -connect localhost:30001
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEfkeLojANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMTkwODAzMDc0OTMxWhcNMjAwODAyMDc0OTMxWjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMDGwHmT
GntqHvPYiM0wm4Dsmhlmiywaj0CGZKW1Cx6ze9pH+iWXEvcnWga4Kfevqh0LJLeS
jmgE6hFRK9rTwq+q6UE0hADazxb7r8jpthnHwKyRGEtFmsFTv/JqJDk+V5cngA4Y
m4scTjF+r1Y7jQA5VkUPHy+eYoNoqRqGh7JhAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBAEICbhntCy/wyg56HQpox3nt8YtTkr6g21P4akxso7m08u6FuyiY
t/8yd+iph6qlRDHQ+D8T4TcpflsV8YKPXIgMoJQtGkuVgqHeCfgBEJcx+T52F8aX
84l5d7tEr9XEuCPKIlf4/GL8wOQLww2a2+sjlSwa8S1XlkbC61JzPyS3
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 12F6177748915C4EE29E6CE09612FFC60C8FBD8EA1752C42D1AF7FC6D7F1C63D
    Session-ID-ctx: 
    Master-Key: 5A1D1A0A4362F7E539EC333D6DDEF78F3B5F130CF997D96B43F8A49392C005919E8030B4F6E48EF0C4EF3278EA40948D
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 6a 32 a6 c7 27 26 f0 c8-b4 75 99 96 41 ed a8 13   j2..'&...u..A...
    0010 - 62 ed 2d fd 4e 24 60 78-8d 6b 87 f6 44 4a 89 37   b.-.N$`x.k..DJ.7
    0020 - 76 9b 04 f7 a3 fa 26 25-ed ee 04 72 a2 68 52 0c   v.....&%...r.hR.
    0030 - fa a2 9c a4 da 7e 09 cb-c4 f3 d1 3d 51 52 c9 b7   .....~.....=QR..
    0040 - 20 7b 54 cf 34 50 b2 2a-9e 91 6c ae a1 09 27 6d    {T.4P.*..l...'m
    0050 - 7b fb de 18 d4 f8 68 9a-db 7e 8c 7e 60 c8 21 84   {.....h..~.~`.!.
    0060 - c8 f1 40 48 9e 4b 6a 62-59 fa 2c 1f 34 06 42 c7   ..@H.KjbY.,.4.B.
    0070 - 67 37 b5 aa 08 0e 21 e9-3e 50 9e 73 6e 65 26 64   g7....!.>P.sne&d
    0080 - e8 f1 be 30 90 aa a6 db-84 42 54 4c c4 b8 87 e4   ...0.....BTL....
    0090 - 6f e0 16 8d 5c b4 39 89-5f a9 87 ab 8e 10 29 f5   o...\.9._.....).

    Start Time: 1569175843
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
BfMYroe26WYalil77FoDi9qh59eK5xNr
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd
```

## [Bandit Level 16 → Level 17](http://overthewire.org/wargames/bandit/bandit17.html)

### Solution:
```
bandit16@bandit:~$ nmap -sT -A -p 31000-32000 localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2019-09-22 20:39 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00025s latency).
Not shown: 998 closed ports
PORT      STATE    SERVICE     VERSION
31337/tcp open     tcpwrapped
31518/tcp filtered unknown
31790/tcp open     ssl/unknown
| fingerprint-strings: 
|   FourOhFourRequest, GenericLines, GetRequest, HTTPOptions, Help, Kerberos, LDAPSearchReq, LPDString, RTSPRequest, SIPOptions, SSLSessionReq, TLSSessionReq: 
|_    Wrong! Please enter the correct current password
| ssl-cert: Subject: commonName=localhost
| Subject Alternative Name: DNS:localhost
| Not valid before: 2019-09-11T17:25:04
|_Not valid after:  2020-09-10T17:25:04
|_ssl-date: TLS randomness does not represent time
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port31790-TCP:V=7.40%T=SSL%I=7%D=9/22%Time=5D87BFF1%P=x86_64-pc-linux-g
SF:nu%r(GenericLines,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20cu
SF:rrent\x20password\n")%r(GetRequest,31,"Wrong!\x20Please\x20enter\x20the
SF:\x20correct\x20current\x20password\n")%r(HTTPOptions,31,"Wrong!\x20Plea
SF:se\x20enter\x20the\x20correct\x20current\x20password\n")%r(RTSPRequest,
SF:31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\
SF:n")%r(Help,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x
SF:20password\n")%r(SSLSessionReq,31,"Wrong!\x20Please\x20enter\x20the\x20
SF:correct\x20current\x20password\n")%r(TLSSessionReq,31,"Wrong!\x20Please
SF:\x20enter\x20the\x20correct\x20current\x20password\n")%r(Kerberos,31,"W
SF:rong!\x20Please\x20enter\x20the\x20correct\x20current\x20password\n")%r
SF:(FourOhFourRequest,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20c
SF:urrent\x20password\n")%r(LPDString,31,"Wrong!\x20Please\x20enter\x20the
SF:\x20correct\x20current\x20password\n")%r(LDAPSearchReq,31,"Wrong!\x20Pl
SF:ease\x20enter\x20the\x20correct\x20current\x20password\n")%r(SIPOptions
SF:,31,"Wrong!\x20Please\x20enter\x20the\x20correct\x20current\x20password
SF:\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 94.54 seconds
bandit16@bandit:~$ openssl s_client --connect localhost:31790
CONNECTED(00000003)
depth=0 CN = localhost
verify error:num=18:self signed certificate
verify return:1
depth=0 CN = localhost
verify return:1
---
Certificate chain
 0 s:/CN=localhost
   i:/CN=localhost
---
Server certificate
-----BEGIN CERTIFICATE-----
MIICBjCCAW+gAwIBAgIEH1uatTANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
b2NhbGhvc3QwHhcNMTkwOTExMTcyNTA0WhcNMjAwOTEwMTcyNTA0WjAUMRIwEAYD
VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMEGArXj
fEcR7ZHlgpHdzr5wlMHuitMnDFnfVRLSmmRb9bKFnFy3Ct7lTR1PqNIa+629KRDm
rIEEK+JU74ZrRA5VWOLNtXjXOAtehMlXteAunhii/JJwSsr+H1i/3HgDZeT8uh7m
slAEJA1qWGUOqDez+NAeuVbhcWtzh7q6IeFlAgMBAAGjZTBjMBQGA1UdEQQNMAuC
CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
DQEBBQUAA4GBABLBkY0sI9L+uDRBMAiMv1lvI0DYsZTX0KqL+GoKeeQLumvXZAyq
xYEEGao2lWiidbwlmA63+Oh/Xab67B1yiQan8MLAmjKPS9gVTB3sDlqyv8n/6mQe
iqHkQcXl2AmRetJVb8dJGt1nWC/zW0uGWC0euAEL6uhyppef2H6dA8hS
-----END CERTIFICATE-----
subject=/CN=localhost
issuer=/CN=localhost
---
No client certificate CA names sent
Peer signing digest: SHA512
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 1019 bytes and written 269 bytes
Verification error: self signed certificate
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 1024 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: E9A86D92075F3229A5ACDE8501CEE287BA5CDB30AC106F233E51BEED93E2174A
    Session-ID-ctx: 
    Master-Key: 727CDD55548FA911D9EB9E19F5D3B72EE4FEDE49A4F8FFB182F54E8CC224EE0D82056B2779B6287CCC1D3D7E1888E86D
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 7200 (seconds)
    TLS session ticket:
    0000 - 7b 34 4b 79 49 fe 28 d8-2c 40 77 81 a8 33 84 29   {4KyI.(.,@w..3.)
    0010 - 79 f3 bc 39 7e a2 df 41-ae 8e 46 d5 cd 9a 2d 19   y..9~..A..F...-.
    0020 - 73 53 4c 77 06 b9 a5 f1-18 cc d3 e7 d8 10 c8 81   sSLw............
    0030 - f9 d2 cd 42 63 0c 0f 7a-2c ef 1e ea d5 69 9c 06   ...Bc..z,....i..
    0040 - 68 87 fc 8c a3 db 5f f6-ff b9 68 99 19 a3 e9 2e   h....._...h.....
    0050 - 3b 1d df a8 de 9a 5c b8-c5 98 8d 66 da 9b a6 72   ;.....\....f...r
    0060 - 29 3a 01 58 97 e4 f7 c0-9f e0 b8 df 45 6a 11 c9   ):.X........Ej..
    0070 - 0e 33 fc f8 c6 15 e8 b4-2c b6 0c 4e 94 2a 69 77   .3......,..N.*iw
    0080 - 3d bc 59 2c f9 29 2d 32-f6 78 ae 18 9c a9 ac 1d   =.Y,.)-2.x......
    0090 - 9a 75 41 89 14 d0 8f 00-01 be da 83 59 5d 21 29   .uA.........Y]!)

    Start Time: 1569177763
    Timeout   : 7200 (sec)
    Verify return code: 18 (self signed certificate)
    Extended master secret: yes
---
cluFn7wTiGryunymYOu4RcffSxQluehd
Correct!
-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAvmOkuifmMg6HL2YPIOjon6iWfbp7c3jx34YkYWqUH57SUdyJ
imZzeyGC0gtZPGujUSxiJSWI/oTqexh+cAMTSMlOJf7+BrJObArnxd9Y7YT2bRPQ
Ja6Lzb558YW3FZl87ORiO+rW4LCDCNd2lUvLE/GL2GWyuKN0K5iCd5TbtJzEkQTu
DSt2mcNn4rhAL+JFr56o4T6z8WWAW18BR6yGrMq7Q/kALHYW3OekePQAzL0VUYbW
JGTi65CxbCnzc/w4+mqQyvmzpWtMAzJTzAzQxNbkR2MBGySxDLrjg0LWN6sK7wNX
x0YVztz/zbIkPjfkU1jHS+9EbVNj+D1XFOJuaQIDAQABAoIBABagpxpM1aoLWfvD
KHcj10nqcoBc4oE11aFYQwik7xfW+24pRNuDE6SFthOar69jp5RlLwD1NhPx3iBl
J9nOM8OJ0VToum43UOS8YxF8WwhXriYGnc1sskbwpXOUDc9uX4+UESzH22P29ovd
d8WErY0gPxun8pbJLmxkAtWNhpMvfe0050vk9TL5wqbu9AlbssgTcCXkMQnPw9nC
YNN6DDP2lbcBrvgT9YCNL6C+ZKufD52yOQ9qOkwFTEQpjtF4uNtJom+asvlpmS8A
vLY9r60wYSvmZhNqBUrj7lyCtXMIu1kkd4w7F77k+DjHoAXyxcUp1DGL51sOmama
+TOWWgECgYEA8JtPxP0GRJ+IQkX262jM3dEIkza8ky5moIwUqYdsx0NxHgRRhORT
8c8hAuRBb2G82so8vUHk/fur85OEfc9TncnCY2crpoqsghifKLxrLgtT+qDpfZnx
SatLdt8GfQ85yA7hnWWJ2MxF3NaeSDm75Lsm+tBbAiyc9P2jGRNtMSkCgYEAypHd
HCctNi/FwjulhttFx/rHYKhLidZDFYeiE/v45bN4yFm8x7R/b0iE7KaszX+Exdvt
SghaTdcG0Knyw1bpJVyusavPzpaJMjdJ6tcFhVAbAjm7enCIvGCSx+X3l5SiWg0A
R57hJglezIiVjv3aGwHwvlZvtszK6zV6oXFAu0ECgYAbjo46T4hyP5tJi93V5HDi
Ttiek7xRVxUl+iU7rWkGAXFpMLFteQEsRr7PJ/lemmEY5eTDAFMLy9FL2m9oQWCg
R8VdwSk8r9FGLS+9aKcV5PI/WEKlwgXinB3OhYimtiG2Cg5JCqIZFHxD6MjEGOiu
L8ktHMPvodBwNsSBULpG0QKBgBAplTfC1HOnWiMGOU3KPwYWt0O6CdTkmJOmL8Ni
blh9elyZ9FsGxsgtRBXRsqXuz7wtsQAgLHxbdLq/ZJQ7YfzOKU4ZxEnabvXnvWkU
YOdjHdSOoKvDQNWu6ucyLRAWFuISeXw9a/9p7ftpxm0TSgyvmfLF2MIAEwyzRqaM
77pBAoGAMmjmIJdjp+Ez8duyn3ieo36yrttF5NSsJLAbxFpdlc1gvtGCWW+9Cq0b
dxviW8+TFVEBl1O4f7HVm6EpTscdDxU+bCXWkfjuRb7Dy9GOtt9JPsX8MBTakzh3
vBgsyi/sN3RqRBcGU40fOoZyfAMT8s1m/uYv52O6IgeuZ/ujbjY=
-----END RSA PRIVATE KEY-----

closed
```

## [Bandit Level 17 → Level 18](http://overthewire.org/wargames/bandit/bandit18.html)

### Login Using:
```bash
chmod 400 17.pem
ssh bandit17@bandit.labs.overthewire.org -p 2220 -i 17.pem
```
### Solution:
```bash
bandit17@bandit:~$ diff passwords.old passwords.new
42c42
< hlbSBPAWJmL6WFDb06gpTx1pPButblOA
---
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd
```

## [Bandit Level 18 → Level 19](http://overthewire.org/wargames/bandit/bandit19.html)

### Login Using:
```bash
chmod 400 17.pem
ssh bandit17@bandit.labs.overthewire.org -p 2220 /bin/sh
```
### Solution:
```bash
pwd
/home/bandit18
ls
readme
cat readme
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x
```

## [Bandit Level 19 → Level 20](http://overthewire.org/wargames/bandit/bandit20.html)

### Solution:
```bash
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20 
GbKksEFF4yrVs6il55v6gwY5aVje5f0j
```

## [Bandit Level 20 → Level 21](http://overthewire.org/wargames/bandit/bandit21.html)

### Solution:
```bash
bandit20@bandit:~$ nc -l -p 1234 < /etc/bandit_pass/bandit20 &
[2] 16018
bandit20@bandit:~$ ./suconnect 1234
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr
```

## [Bandit Level 21 → Level 22](http://overthewire.org/wargames/bandit/bandit22.html)

### Solution:
```bash
bandit21@bandit:/etc/cron.d$ ls /etc/cron.d
cronjob_bandit22  cronjob_bandit23  cronjob_bandit24
bandit21@bandit:/etc/cron.d$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
bandit21@bandit:/etc/cron.d$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI
```

## [Bandit Level 22 → Level 23](http://overthewire.org/wargames/bandit/bandit23.html)

### Solution:
```
bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh 
#!/bin/bash

myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)

echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"

cat /etc/bandit_pass/$myname > /tmp/$mytarget
bandit22@bandit:~$ myname=bandit23
bandit22@bandit:~$ mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
bandit22@bandit:~$ echo $mytarget
8ca319486bfbbc3663ea0fbe81326349
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n
```

# REDO 23-24

UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ

## [Bandit Level 24 → Level 25](http://overthewire.org/wargames/bandit/bandit25.html)

### Solution:

```bash
bandit24@bandit:~$ mkdir /tmp/pit24
bandit24@bandit:~$ for i in {0000..9999}
> do
> echo UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ $i >> /tmp/pit24/out
> done
bandit24@bandit:~$ cat /tmp/pit24/out | nc localhost 30002 | grep password
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG
```

## [Bandit Level 25 → Level 26](http://overthewire.org/wargames/bandit/bandit26.html)

### Solution:

5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z

## [Bandit Level 26 → Level 27](http://overthewire.org/wargames/bandit/bandit27.html)

### Solution:

```bash
bandit26@bandit:~$ ./bandit27-do 
Run a command as another user.
  Example: ./bandit27-do id
bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
3ba3118a22e93127a4ed485be72ef5ea
```

## [Bandit Level 27 → Level 28](http://overthewire.org/wargames/bandit/bandit28.html)

### Solution:
```
bandit27@bandit:~$ mkdir /tmp/pit27
bandit27@bandit:~$ cd /tmp/pit27
bandit27@bandit:/tmp/pit27$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
Cloning into 'repo'...
Could not create directory '/home/bandit27/.ssh'.
The authenticity of host 'localhost (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:98UL0ZWr85496EtCRkKlo20X3OPnyPSB5tB5RPbhczc.
Are you sure you want to continue connecting (yes/no)? yes
Failed to add the host to the list of known hosts (/home/bandit27/.ssh/known_hosts).
This is a OverTheWire game server. More information on http://www.overthewire.org/wargames

bandit27-git@localhost's password: 
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
bandit27@bandit:/tmp/pit27$ ls
repo
bandit27@bandit:/tmp/pit27$ cd repo
bandit27@bandit:/tmp/pit27/repo$ ls
README
bandit27@bandit:/tmp/pit27/repo$ cat README 
The password to the next level is: 0ef186ac70e04ea33b4c1853d2526fa2
```

## [Bandit Level 28 → Level 29](http://overthewire.org/wargames/bandit/bandit29.html)

### Solution:

```bash
bandit28@bandit:/tmp/pit28/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: xxxxxxxxxx

bandit28@bandit:/tmp/pit28/repo$ git log --oneline
073c27c fix info leak
186a103 add missing data
b67405d initial commit of README.md
bandit28@bandit:/tmp/pit28/repo$ git checkout 186a103
Note: checking out '186a103'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at 186a103... add missing data
bandit28@bandit:/tmp/pit28/repo$ cat README.md 
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: bbc96594b4e001778eee9975372716b2
```