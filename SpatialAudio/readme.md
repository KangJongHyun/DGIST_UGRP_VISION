1. D455의 스펙은 수평각(방위각) 기준 87도 인식가능, 권남혁이 보내준 depth 파악 사진은 950 * 713정도였다. y값(현실 z값, 사진상 y값)을 무시하고 2차원상의 평면에서 공간음향을 구현한다고 하면 사진상 (x, y)좌표(픽셀)와 거리 d는

[사용자 기준 거리: arctan(24tan(43.5) / 950 * |x - 950/2| / d), 방위각: sqrt( (24tan(43.5) / 950 * |x - 950/2|)^2 + d^2)]이다.
2. 일단 이 87도가 너무 좁지 않은가..?
3. 지금 에어팟 2로 공간음향을 확인하고 있는데 너무 구리다 -> 헤드폰을 사자.
4. HRTF나 python 오디오 모듈(pyaudio, pydub, soundfile, librosa 등등)들을 사용해서 공간음향을 구현하고 이를 실용화하자는 것은 너무 오만한것 같다. 공간음향으로 유명한 Dolby Atmos사의 프로그램을 이용해보는 건 어떨까?(5.1, 7.1 channel과는 다름). 구현이 아예 안되는 것도 있어서..
https://www.avid.com/plugins/Dolby-Atmos-Renderer
![image](https://github.com/KangJongHyun/DGIST_UGRP_VISION/assets/134807177/8325195b-1743-470f-b790-fb83f4ab18de)
90일 무료체험/정가 299$
https://dolby.io/project-gallery/
https://dashboard.dolby.io/dashboard/applications/summary/
https://github.com/dolbyio-samples/comms-app-react-videocall
----
헤드폰 추천
1. 오디지 모비우스(해외배송): https://www.11st.co.kr/products/4142836227?service_id=elecdn&utm_term=&utm_campaign=%B4%D9%B3%AA%BF%CDpc_%B0%A1%B0%DD%BA%F1%B1%B3%B1%E2%BA%BB&utm_source=%B4%D9%B3%AA%BF%CD_PC_PCS&utm_medium=%B0%A1%B0%DD%BA%F1%B1%B3
2. 스틸 시리즈 Arctis Nova Pro: https://prod.danawa.com/info/?pcode=17655659#bookmark_product_information
3. 젠하이저 모멘텀4: https://prod.danawa.com/info/?pcode=17703695#bookmark_product_information
4. 젠하이저 HD 660S: https://prod.danawa.com/info/?pcode=5562038&relationMenuType=recommend#bookmark_relation_product
5. 오디지 펜로즈, X: https://prod.danawa.com/info/?pcode=14904935&relationMenuType=recommend#bookmark_cm_opinion, https://prod.danawa.com/info/?pcode=14904911#bookmark_cm_opinion
6. 오디오테크니카 ATH-M50x(싸다, 가성비): https://prod.danawa.com/info/?pcode=2563515#bookmark_cm_opinion
7. 커세어 HS80(싼데 Dolby지원): https://prod.danawa.com/info/?pcode=15050054
