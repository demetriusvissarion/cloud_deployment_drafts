brew install telnet
brew install termshark

telnet xf.mkrs.link
sudo termshark -f "port 23"


telnet xf.mkrs.link


curl -vvv http://www.example.org

url -vvv "ftp://ftp.bit.nl/OpenBSD/songs/song30.mp3" --output /tmp/song30.mp3
afplay /tmp/song30.mp3


telnet www.example.org 80
# paste both lines together:
GET / HTTP/1.1
Host: www.example.org


nslookup example.org
dig example.org A
dig example.org NS


cat - | openssl pkeyutl -encrypt -inkey kay-public.pem -pubin | base64

openssl aes-256-cbc -pbkdf2 -d -in secret.txt.enc