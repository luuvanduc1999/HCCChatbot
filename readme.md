## Install Rasa + Các module khác
- > pip3 install -r requirements.txt i

# HCCChatbot

## Train model
- > rasa train

hoặc chỉ train nlu:
- > rasa train nlu

## Run
**Nếu có custom action cần chạy song song 2 terminal**
- > rasa run actions
- > rasa shell

**Run API**
- > rasa run actions
- > rasa run --enable-api

# DEMO UI
**Terminal 1+2:**
- > cd HCCChatbot
- > rasa run --enable-api


localhost:5002
- > rasa run actions


localhost:5055


**Terminal 3:**
- > node NodeServer/server.js
localhost:8080


