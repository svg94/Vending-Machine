from flask import Flask, request, render_template
from motor import Motor
from insult import Insults

app = Flask(__name__)
m2 = Motor(7,11,13,15)
m1 = Motor(19,21,23,29)
m4 = Motor(8,10,12,16)
m3 = Motor(18,22,24,26)
i = Insults()

@app.route('/', methods=['GET'])
def index():
	status = request.args.get('status')
	text=i.getRdmInsult()
	if status == 'succ1':
		m1.Turn_Right(500)
		return render_template("index.html",name=text)
	if status == 'succ2':
		m2.Turn_Right(500)
		return render_template("index.html",name=text)
	if status == 'succ3':
		m3.Turn_Right(500)
		return render_template("index.html",name=text)
	if status == 'succ4':
		m4.Turn_Right(500)
		return render_template("index.html",name=text)
	return render_template("index.html", name="")
@app.route('/settings.html', methods=['GET'])
def settings():
    status = request.args.get('status')
    text=""
    if status == 'bacc1':
        m1.Turn_Left(500)
        text="Gimme more"
        return render_template('settings.html')
    if status == 'bacc2':
        m2.Turn_Left(500)
        text="Gimme more"
        return render_template('settings.html')
    if status == 'bacc3':
        m3.Turn_Left(500)
        text="Gimme more"
        return render_template('settings.html')
    if status == 'bacc4':
        m4.Turn_Left(500)
        text="Gimme more"
        return render_template('settings.html')
    return render_template("settings.html")

#if __name__ == "__main__":
#	app.run()
