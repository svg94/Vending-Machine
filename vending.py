from flask import Flask, request, render_template
from motor import Motor

app = Flask(__name__, template_folder="./")
m1 = Motor(7,11,13,15)
m2 = Motor(19,21,23,29)
m3 = Motor(8,10,12,16)
m4 = Motor(18,22,24,26)

@app.route('/Vending-Machine/', methods=['GET'])
def index():
	status = request.args.get('status')
	text=""
	if status == 'succ1':
		m1.Turn_Right(500)
		text="Snack retrieved. Don't get any more, bro. It's for your own health."
		return render_template("index.html",name=text)
	if status == 'succ2':
		m2.Turn_Right(500)
		text="Snack retrieved. Don't get any more, bro. It's for your own health."
		return render_template("index.html",name=text)
	if status == 'succ3':
		m3.Turn_Right(500)
		text="Snack retrieved. Don't get any more, bro. It's for your own health."
		return render_template("index.html",name=text)
	if status == 'succ4':
		m4.Turn_Right(500)
		text="Snack retrieved. Don't get any more, bro. It's for your own health."
		return render_template("index.html",name=text)


	return render_template("index.html",name =text)

if __name__ == "__main__":
	app.run()
