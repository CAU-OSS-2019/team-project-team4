#Tission backend
![Tission](https://github.com/CAU-OSS-2019/team-project-team4/blob/front/front/vue-front/public/img/brand/tission2.png?raw=true)

## Functions
* Provide [Sign In with Twitch API](https://dev.twitch.tv/)

* Maintain twitch login session even if you log off on tission server

* Show Information like ID and Image from Twich API when you sign in

* At scheduled time, the system get donation list from twip.kr

* Classify mission to from donation list from twip.kr.

* If the message is determined as mission, insert message into ElasticSearch DB on server

* At scheduled time, find datas from ElasticSearch with user's id. And Display it.

* You can determine the mission will success or failed, and also delete when you don't want to accept it.

* ~~You can create your own mission, and modify it~~

## File Structure
```
backend
 │  app.js
 │  package.json
 │  README.md
 │  twipcrawler.py
 ├─bin
 │      www
 └─routes
         index.js
```
## Development Tool
* Node.js
* ElasticSearch
