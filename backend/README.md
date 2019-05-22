Tission backend

- Functions
• Twitch tv의 API를 사용하여 로그인 기능을 제공.

• Tission에서 로그아웃을 하여도 Twitch 로그아웃이 되지 않도록 session을 활용하여 Tission 서버에서만 로그아웃함.

• 로그인 시, Twitch api에서 받아온 정보를 바탕으로 사용자의 정보를 표시함.

• 매 일정 주기마다 후원 목록을 twip으로부터 가져옴.

• 가져온 정보를 NLP 모델에 넣어 미션인지 확인, 그 후 맞을 시 ElasticSearch DB에 저장.

• 매 일정 주기마다 ElasticSearch에서 로그인한 사용자에 해당하는 미션 데이터를 검색, 표시함.

- Development Tool
• Node.js / ElasticSearch
