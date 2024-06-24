from flask import Flask

app = Flask(__name__)		#name 이름을 이용한 flask객체생성

@app.route("/")		#라우팅을위한 뷰함수 등록
def hello():
	return "Son jin-yong"

if __name__ == "__main__":	# 터미널에서 직접실행시키면 실행파일이 실행 파일이 main 으로 바뀜
	app.run(host = "0.0.0.0", port = "10111", debug = True)	# 실행을 위한 명령문으로 보면 됨
