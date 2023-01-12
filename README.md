# autoKakaoSender
카톡 1:1 메시지 자동 발송 프로그램

## 참고 레퍼런스
https://gitlab.com/Whackur/kakaoautomsgsender

기본적인 소스는 위의 소스를 참고하였습니다. 훌륭한 아이디어를 제공해 주신 Whackur 님께 감사드립니다.

## 개선내용
* 메시지 내용은 msg.txt 파일의 내용으로만 전송 하도록 변경.
* 친구 검색 개수 입력 삭제 (자동으로 마지막 친구 목록 확인)
* 이미지 전송이 가능하도록 기능 추가.

## 설치
<pre>
> git clone https://github.com/hwantage/autoKakaoSender.git

> python -m pip install --upgrade pip
> pip3 install opencv-contrib-python==4.6.0.66
> pip install opencv-python
> pip install pyperclip
> pip install pyautogui
> pip install numpy
</pre>

## 실행 준비
* msg.txt 파일에 메시지 작성
* 이미지가 있다면 msg.jpg 파일로 저장
* 이미지를 전송하지 않으려면 msg.jpg 삭제

## 실행
<pre>
> python autoKakao.py
</pre>

## Limitation
카카오톡의 테마 변경이나 아이콘 변경 등 이미지 변경사항 발생시 프로그램 오류 발생.

변경된 상태에 따라 img 폴더의 이미지를 다시 캡처해야 함.

* PC 카톡 실행 후 아래의 빨간색 부분을 캡처(Shift+Window+S)하여 img 폴더에 저장 
<img src='https://user-images.githubusercontent.com/82494320/211988665-e0640f58-76d3-44a3-9002-34adc01440e2.png'>
[캡처된 이미지]
<img src='https://user-images.githubusercontent.com/82494320/211989746-1d64ddf7-7747-4820-bde8-463fa0f6058a.png'>
⚠️ person_icon.png 파일이 짤려 있는 이유는 새로운 친구가 등록될 경우 우측 상단에 배너 아이콘이 추가로 생겨서 이미지 인식이 실패하기 때문에 빨간색 부분을 피해서 캡처해야 한다. <img src='https://user-images.githubusercontent.com/82494320/211989946-cc1fc8cd-9cc6-4f19-af87-506d37c1fd28.png'>




## Reference

[[파이썬 업무자동화] 04.카카오톡 메세지를 자동으로 보내보자!](https://www.youtube.com/watch?v=oNjRH1Cz9k4)

[python clipboard 파일복사 이미지 보내기](https://miero.tistory.com/1183)

[AttributeError: partially initialized module 'cv2' has no attribute 'gapi_wip_gst_GStreamerPipeline' (most likely due to a circular import)](https://stackoverflow.com/questions/72706073/attributeerror-partially-initialized-module-cv2-has-no-attribute-gapi-wip-gs)

[Welcome to PyAutoGUI's documentation! - PyAutoGUI documentation](https://pyautogui.readthedocs.io/en/latest/index.html)
