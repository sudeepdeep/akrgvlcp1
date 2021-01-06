from flask import Flask,render_template,url_for
from flask import *
import random
app = Flask(__name__)

@app.route('/')

def home():
	return render_template('home.html')
@app.route('/resu')
def resu():
	
	return render_template('resu.html')

@app.route('/nodata')
def nodata():
	return render_template('nodata.html')
@app.route('/res')
def res():
	return render_template('res.html')

@app.route('/131')
def three():
	return render_template('131.html')
@app.route('/161')
def six():
	return render_template('161.html')

@app.route('/162')
def sixx():
	return render_template('162.html')
@app.route('/163')
def sixxx():
	return render_template('163.html')


@app.route('/191')
def nine():
	return render_template('191.html')

@app.route('/192')
def ninee():
	return render_template('192.html')

@app.route('/193')
def nineee():
	return render_template('193.html')

@app.route('/132')
def three1():
	return render_template('132.html')
@app.route('/sub')
def sub():
	return render_template('subjects.html')
@app.route('/testpaper')
def testpaper():
	lst2 = [0,1,2,3,4,5,6,7,8,9,10]
	random.shuffle(lst2)
	lst3 = lst2[0:5]
	return render_template('testpaper.html',lst2 = lst3)

@app.route('/radio',methods = ['GET','POST'])
def radio():
	if request.method == 'POST':
		i = 0
		try:
			opt0 = request.form['options0']
			if opt0 == 'd':
				i = i+1
		except Exception as e:
			pass

		try:
			opt1 = request.form['options1']
			if opt1 == 'b':
				i = i+1
		except Exception as e:
			pass

		try:
			opt2 = request.form['options2']
			if opt2 == 'd':
				i = i+1
		except Exception as e:
			pass

		try:
			opt3 = request.form['options3']
			if opt3 == 'c':
				i = i+1
		except Exception as e:
			pass

		try:
			opt4 = request.form['options4']
			if opt4 == 'a':
				i = i+1
		except Exception as e:
			pass

		try:
			opt5 = request.form['options5']
			if opt5 == 'b':
				i = i+1
		except Exception as e:
			pass

		try:
			opt6 = request.form['options6']
			if opt6 == 'c':
				i = i+1
		except Exception as e:
			pass

		try:
			opt7 = request.form['options7']
			if opt7 == 'c':
				i = i+1
		except Exception as e:
			pass

		try:
			opt8 = request.form['options8']
			if opt8 == 'b':
				i = i+1
		except Exception as e:
			pass

		try:
			opt9 = request.form['options9']
			if opt9 == 'b':
				i = i+1
		except Exception as e:
			pass

		try:
			opt10 = request.form['options10']
			if opt10 == 'a':
				i = i+1
		except Exception as e:
			pass
		return render_template('register.html',score = i)
	return render_template('testpaper.html')

@app.route('/test1')
def test1():
	return render_template('test1.html')
@app.route('/reg1')
def reg1():
	return render_template('reg1.html')
@app.route('/register')
def register():
	return render_template('register.html')
@app.route('/c')
def c():
	return render_template('c.html')

@app.route('/c1')
def c1():
	return render_template('c++.html')

@app.route('/python')
def python():
	return render_template('python.html')

@app.route('/java')
def java():
	return render_template('java.html')

@app.route('/ds')
def ds():
	return render_template('ds.html')
@app.route('/ads')
def ads():
	return render_template('ads.html')

@app.route('/htm')
def htm():
	return render_template('htm.html')

@app.route('/ml')
def ml():
	return render_template('ml.html')
@app.route('/rp')
def rp():
	return render_template('rp.html')

@app.route('/nix')
def nix():
	return render_template('nx.html')
@app.route('/sql')
def sql():
	return render_template('sql.html')

@app.route('/c11')
def c11():
	return render_template('c11.html')

@app.route('/c12')
def c12():
	return render_template('c12.html')

@app.route('/p1')
def p1():
	return render_template('p1.html')

@app.route('/j1')
def j1():
	return render_template('j1.html')

@app.route('/ml1')
def ml1():
	return render_template('ml1.html')

@app.route('/r1')
def r1():
	return render_template('r1.html')

@app.route('/dbms1')
def dbms1():
	return render_template('dbms1.html')

@app.route('/nix1')
def nix1():
	return render_template('nix1.html')

@app.route('/ds1')
def ds1():
	return render_template('ds1.html')

@app.route('/ds2')
def ds2():
	return render_template('ds2.html')

@app.route('/html1')
def html1():
	return render_template('html1.html')








@app.route('/submit',methods = ['GET','POST'])
def submit():
	if request.method == 'POST':
		return render_template('home.html')

		
if __name__ == "__main__":
	app.run(debug = True)
