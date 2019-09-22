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