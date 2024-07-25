<h1>Fullstack Service Networking Season.2 <br />HTTP/1.1 RESTful API Program</h1>	

Server : Python

Client : Web Browser (PyScript : Python in HTML, Pico.css)

Networking : HTTP/1.1

Packaging : Poetry (추가 패키지: 없음)

<br />
<br />

<h2>실행 방법</h2>	

프로젝트를 다운로드 함

src/server/server.py를 실행하여 RESTful API 서버를 실행함 (포트 8080 사용)<br />
> python server.py

src/client/ 폴더로 이동함

Python의 http.server를 실행함 (기본으로 포트 8000 사용)<br />
> python -m http.server

웹브라우저로 http://localhost:8000/client_pyscript.html에 접속함

화면 위쪽의 “Please wait, program is starting …” 문구가 다음처럼 바뀌기를 기다림<br />
Please fills key/value and executes menu :

CREATE 동작을 위하여,<br />
CREATE 버튼 왼쪽의 Key와 Value에 각각 apple과 1000을 입력하고, CREATE 버튼을 클릭함<br />
CREATE 결과를 웹브라우저 화면과 서버 출력 화면에서 확인함

READ 동작을 위하여,<br />
READ 버튼 왼쪽의 Key에 apple을 입력하고, READ 버튼을 클릭함<br />
READ 결과를 웹브라우저 화면과 서버 출력 화면에서 확인함

UPDATE 동작을 위하여,<br />
UPDATE 버튼 왼쪽의 Key와 Value에 각각 apple과 2000을 입력하고, UPDATE 버튼을 클릭함<br />
UPDATE 결과를 웹브라우저 화면과 서버 출력 화면에서 확인함

DELETE 동작을 위하여,<br />
DELETE 버튼 왼쪽의 Key에 apple을 입력하고, DELETE 버튼을 클릭함<br />
DELETE 결과를 웹브라우저 화면과 서버 출력 화면에서 확인함

서버 종료를 위하여 ctrl-c 키보드 입력을 수행함

Client를 실행하기 위해서, 실행한 Python http.server를 ctrl-c 키보드 입력으로 종료함

<br />
<br />

<h2>실행 화면</h2>	

<img src="/screen/client-create.png" width="1000"/>

<img src="/screen/client-read.png" width="1000"/>

<img src="/screen/client-update.png" width="1000"/>

<img src="/screen/client-delete.png" width="1000"/>

<img src="/screen/server.png" width="1000"/>
