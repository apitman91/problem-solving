# OverTheWire - Bandit

## [Bandit Level 0 → Level 1](http://overthewire.org/wargames/bandit/bandit1.html)

## solution:
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

## solution:
```
cat ./-
```
password for level 2: **CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9**

#### References:
https://unix.stackexchange.com/questions/16357/usage-of-dash-in-place-of-a-filename

## [Bandit Level 2 → Level 3](http://overthewire.org/wargames/bandit/bandit3.html)

## Solution:
```
cat ./spaces\ in\ this\ filename
```
password for level 3: **UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK**

## [Bandit Level 3 → Level 4](http://overthewire.org/wargames/bandit/bandit4.html)

## Solution:
```
cat inhere/.hidden
```
password for level 4: **pIwrPrtPN36QITSp3EQaw936yaFoFgAB**

## [Bandit Level 4 → Level 5](http://overthewire.org/wargames/bandit/bandit5.html)

## Solution:
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

## Solution:
```bash
bandit5@bandit:~$ find . -type f -size 1033c ! -executable 
./inhere/maybehere07/.file2
bandit5@bandit:~$ cat ./inhere/maybehere07/.file2
DXjZPULLxYr17uwoI01bNLQbtFemEgo7
```

## [Bandit Level 6 → Level 7](http://overthewire.org/wargames/bandit/bandit7.html)

## Solution:
```bash
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c 2> /dev/null
/var/lib/dpkg/info/bandit7.password
bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password 
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs
```

## [Bandit Level 7 → Level 8](http://overthewire.org/wargames/bandit/bandit8.html)

## Solution:
```
bandit7@bandit:~$ grep millionth data.txt 
millionth	cvX2JJa4CFALtqS87jk27qwqGhBM9plV
```

## [Bandit Level 8 → Level 9](http://overthewire.org/wargames/bandit/bandit9.html)

## Solution:
```
bandit8@bandit:~$ sort data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR
```

## [Bandit Level 9 → Level 10](http://overthewire.org/wargames/bandit/bandit10.html)

## Solution:
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

## Solution:
```
bandit10@bandit:~$ base64 -d data.txt 
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR
```

## [Bandit Level 11 → Level 12](http://overthewire.org/wargames/bandit/bandit12.html)

## Solution:
```
bandit11@bandit:~$ cat data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu
```