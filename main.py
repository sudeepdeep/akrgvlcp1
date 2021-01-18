from flask import Flask,render_template,url_for
from flask import *
import random

import pyrebase


config = {
	"apiKey": "AIzaSyD0fzFslus_LRDNQI022QHTAJ5Ch0vgpZ0",
    "authDomain": "akrgtesting.firebaseapp.com",
    "databaseURL": "https://akrgtesting-default-rtdb.firebaseio.com",
    "projectId": "akrgtesting",
    "storageBucket": "akrgtesting.appspot.com",
    "messagingSenderId": "557661419296",
    "appId": "1:557661419296:web:e0e73026a6e2a2770a4945",
    "measurementId": "G-Y6P5JBQ7SV"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
app = Flask(__name__)
app.secret_key = "hellosudeep"


@app.route("/firebase")
def firebase():
	return render_template('firebase.html')

@app.route("/check")
def check():
	return render_template('final.html')

@app.route("/final", methods = ['GET','POST'])
def final():
	try:
		if request.method == 'POST':
			regid = request.form['registerno']
			semid = request.form['semid']
			res = db.child(regid).get()

			for task in res.each():
				if task.val()['Sem'] == semid:
					if semid == '1-1':
						res = task.val()
						return render_template('res.html',marks = res)
					elif semid == '1-2':
						res = task.val()
						return render_template('res1.html',marks = res)
					elif semid == '2-1':
						res = task.val()
						return render_template('res2.html',marks = res)
					elif semid == '2-2':
						res = task.val()
						return render_template('res3.html',marks = res)
					elif semid == '3-1':
						res = task.val()
						return render_template('res4.html',marks = res)
					elif semid == '3-2':
						res = task.val()
						return render_template('res5.html',marks = res)
					elif semid == '4-1':
						res = task.val()
						return render_template('res6.html',marks = res)
					elif semid == '4-2':
						res = task.val()
						return render_template('res7.html',marks = res)
	except Exception as e:
		return render_template('error.html')

	return render_template('firebase.html')

@app.route('/validate',methods = ['GET','POST'])
def validate():
	if request.method == 'POST':
		name = request.form.get('name')
		password = request.form.get('password')

		if name == 'akrg123@gmail.com' and  password == 'akrgadmincp':
			session['loggedin'] = True
			return render_template('s1.html')
	return render_template('firebase.html')

@app.route('/login')
def login():
	return render_template('logged.html')


@app.route('/delete',methods = ['GET','POST'])
def delete():
	try:
		if session['loggedin']:
			if request.method == 'POST':
				regno = request.form['registerno']
				semid = request.form['semid']
				del_list = db.child(regno).get()
				for a in del_list.each():
					if a.val()['Sem'] == semid:
						b = a.key()
				db.child(regno).child(b).remove()
				return render_template('update.html')
		else:
			return render_template('firebase.html')
	except Exception as e:
		return render_template('error.html')
	return render_template('update.html')
@app.route('/enter')
def enter():
	if session['loggedin']:
		return render_template('s1.html')
	else:
		return render_template('logged.html')

@app.route('/sone',methods = ['GET','POST'])
def sone():
	try:
		if session['loggedin']:
			if request.method == 'POST':
				regno = request.form['regno']
				sem = request.form['sem']
				session['regno'] = regno
				session['sem'] = sem
				if sem == '1-1':
					return render_template('oo.html')
				elif sem == '1-2':
					return render_template('ot.html')
				elif sem == '2-1':
					return render_template('to.html')
				elif sem == '2-2':
					return render_template('tt.html')
				elif sem == '3-1':
					return render_template('tho.html')
				elif sem == '3-2':
					return render_template('tht.html')
				elif sem == '4-1':
					return render_template('fo.html')
				elif sem == '4-2':
					return render_template('ft.html')
		else:
			return render_template('logged.html')
	except Exception as e:
		return render_template('error.html')
	return render_template('s1.html')

@app.route('/oo', methods = ['GET','POST'])
def oo():

	if 'loggedin' in session:
		if request.method == 'POST':
			regno = session['regno']
			sem = session['sem']
			e1 = request.form['e1']
			m1 = request.form['m1']
			m2 = request.form['m2']
			ap = request.form['ap']
			cp = request.form['cp']
			ed  = request.form['ed']
			ecl = request.form['ecl']
			pl = request.form['pl']
			cpl = request.form['cpl']
			data =  { 'Regno': regno,
	          'Sem': sem,
	          'english-1': e1,
	          'mathematics-1':m1,
	          'mathematics-2':m2,
	          'applied-physics':ap,
	          'computer programming':cp,
	          'engineering drawing':ed,
	          'englishb communications lab':ecl,
	          'physics lab':pl,
	          'computer programming lab':cpl
	          }
			result = db.child(regno).push(data)
			return render_template('sone.html')
	else:
		return render_template('logged.html')

@app.route('/ot', methods = ['GET','POST'])
def ot():
	try:
		if request.method == 'POST':
			regno = session['regno']
			sem = session['sem']
			s1 = request.form['s1']
			s2 = request.form['s2']
			s3 = request.form['s3']
			s4 = request.form['s4']
			s5 = request.form['s5']
			s6  = request.form['s6']
			l1 = request.form['l1']
			l2 = request.form['l2']
			l3 = request.form['l3']
			data =  { 'Regno': regno,
	          'Sem': sem,
	          'subject-1': s1,
	          'subject-2':s2,
	          'subject-3':s3,
	          'subject-4':s4,
	          'subject-5':s5,
	          'subject-6':s6,
	          'lab-1':l1,
	          'lab-2':l2,
	          'lab-3':l3
	          }
			result = db.child(regno).push(data)
		return render_template('sone.html')
	except Exception as e:
		return render_template('error.html')
	return render_template('firebase.html')

@app.route('/to', methods = ['GET','POST'])
def to():
	try:
		if request.method == 'POST':
			regno = session['regno']
			sem = session['sem']
			s1 = request.form['s1']
			s2 = request.form['s2']
			s3 = request.form['s3']
			s4 = request.form['s4']
			s5 = request.form['s5']
			l1 = request.form['l1']
			l2 = request.form['l2']
			data =  { 'Regno': regno,
	          'Sem': sem,
	          'subject-1': s1,
	          'subject-2':s2,
	          'subject-3':s3,
	          'subject-4':s4,
	          'subject-5':s5,
	          'lab-1':l1,
	          'lab-2':l2,
	         
	          }
			result = db.child(regno).push(data)
		return render_template('sone.html')
	except Exception as e:
		return render_template('error.html')
	return render_template('firebase.html')

@app.route('/tt', methods = ['GET','POST'])
def tt():
	try:
		if request.method == 'POST':
			regno = session['regno']
			sem = session['sem']
			s1 = request.form['s1']
			s2 = request.form['s2']
			s3 = request.form['s3']
			s4 = request.form['s4']
			s5 = request.form['s5']
			s6 = request.form['s6']
			l1 = request.form['l1']
			l2 = request.form['l2']
			data =  { 'Regno': regno,
	          'Sem': sem,
	          'subject-1': s1,
	          'subject-2':s2,
	          'subject-3':s3,
	          'subject-4':s4,
	          'subject-5':s5,
	          'subject-6':s6,
	          'lab-1':l1,
	          'lab-2':l2,
	         
	          }
			result = db.child(regno).push(data)
		return render_template('sone.html')
	except Exception as e:
		return render_template('error.html')
	return render_template('firebase.html')

@app.route('/tho', methods = ['GET','POST'])
def tho():
	try:
		if request.method == 'POST':
			regno = session['regno']
			sem = session['sem']
			s1 = request.form['s1']
			s2 = request.form['s2']
			s3 = request.form['s3']
			s4 = request.form['s4']
			s5 = request.form['s5']
			l1 = request.form['l1']
			l2 = request.form['l2']
			l3 = request.form['l3']
			s6 = request.form['s6']
			data =  { 'Regno': regno,
	          'Sem': sem,
	          'subject-1': s1,
	          'subject-2':s2,
	          'subject-3':s3,
	          'subject-4':s4,
	          'subject-5':s5,
	          'subject-6':s6,
	          'lab-1':l1,
	          'lab-2':l2,
	          'lab-3':l3,
	          }
			result = db.child(regno).push(data)
		return render_template('sone.html')
	except Exception as e:
		return render_template('error.html')
	return render_template('firebase.html')




@app.route('/tht', methods = ['GET','POST'])
def tht():
	try:
		if request.method == 'POST':
			regno = session['regno']
			sem = session['sem']
			s1 = request.form['s1']
			s2 = request.form['s2']
			s3 = request.form['s3']
			s4 = request.form['s4']
			s5 = request.form['s5']
			l1 = request.form['l1']
			l2 = request.form['l2']
			l3 = request.form['l3']
			s6 = request.form['s6']
			data =  { 'Regno': regno,
	          'Sem': sem,
	          'subject-1': s1,
	          'subject-2':s2,
	          'subject-3':s3,
	          'subject-4':s4,
	          'subject-5':s5,
	          'subject-6':s6,
	          'lab-1':l1,
	          'lab-2':l2,
	          'lab-3':l3,
	          }
			result = db.child(regno).push(data)
		return render_template('sone.html')
	except Exception as e:
		return render_template('error.html')
	return render_template('firebase.html')



@app.route('/fo', methods = ['GET','POST'])
def fo():
	try:
		if request.method == 'POST':
			regno = session['regno']
			sem = session['sem']
			s1 = request.form['s1']
			s2 = request.form['s2']
			s3 = request.form['s3']
			s4 = request.form['s4']
			s5 = request.form['s5']
			l1 = request.form['l1']
			l2 = request.form['l2']
			s6 = request.form['s6']
			data =  { 'Regno': regno,
	          'Sem': sem,
	          'subject-1': s1,
	          'subject-2':s2,
	          'subject-3':s3,
	          'subject-4':s4,
	          'subject-5':s5,
	          'subject-6':s6,
	          'lab-1':l1,
	          'lab-2':l2,
	          }
			result = db.child(regno).push(data)
		return render_template('sone.html')
	except Exception as e:
		return render_template('error.html')
	return render_template('firebase.html')



@app.route('/ft', methods = ['GET','POST'])
def ft():
	try:
		if request.method == 'POST':
			regno = session['regno']
			sem = session['sem']
			s1 = request.form['s1']
			s2 = request.form['s2']
			s3 = request.form['s3']
			s4 = request.form['s4']
			s5 = request.form['s5']
			s6 = request.form['s6']
			data =  { 'Regno': regno,
	          'Sem': sem,
	          'subject-1': s1,
	          'subject-2':s2,
	          'subject-3':s3,
	          'subject-4':s4,
	          'subject-5':s5,
	          'subject-6':s6,
	          }
			result = db.child(regno).push(data)
		return render_template('sone.html')
	except Exception as e:
		return render_template('error.html')
	return render_template('firebase.html')


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

@app.route('/cnpage')
def cnpage():
	lst2 = [0,1,2,3,4,5,6,7,8,9,10]
	random.shuffle(lst2)
	lst3 = lst2[0:5]
	
	return render_template('cnpaper.html',lst2 = lst3)

@app.route('/cnpaper',methods = ['GET','POST'])
def cnpaper():
	if request.method == 'POST':
		wrong_ans = []
		correct_ans = []
		wrong_qstn = []
		wrong_dict = {}
		i = 0
		try:
			opt0 = request.form['options0']
			if opt0 == 'c':
				res  = 'true'
				i = i+1
				
			else:
				ans  = 'c'
				wrong_ans.append(opt0)
				correct_ans.append(ans)
				wrong_qstn.append(0)
				wrong_dict[0] = 'c'

		except Exception as e:
			pass

		try:
			opt1 = request.form['options1']
			if opt1 == 'a':
				res  = 'true'
				i = i+1

			else:
				ans = 'a'
				wrong_ans.append(opt1)
				correct_ans.append(ans)
				wrong_qstn.append(1)
				wrong_dict[1] = 'a'
		except Exception as e:
			pass

		try:
			opt2 = request.form['options2']
			if opt2 == 'a':
				res  = 'true'
				i = i+1
			else:
				ans = 'a'
				wrong_ans.append(opt2)
				correct_ans.append(ans)
				wrong_qstn.append(2)
				wrong_dict[2] = 'a'
		except Exception as e:
			pass

		try:
			opt3 = request.form['options3']
			if opt3 == 'a':
				res  = 'true'
				i = i+1
			else:
				ans = 'a'
				wrong_ans.append(opt3)
				correct_ans.append(ans)
				wrong_qstn.append(3)
				wrong_dict[3] = 'a'
		except Exception as e:
			pass

		try:
			opt4 = request.form['options4']
			if opt4 == 'c':
				res  = 'true'
				i = i+1
			else:
				ans = 'c'
				wrong_ans.append(opt4)
				correct_ans.append(ans)
				wrong_qstn.append(4)
				wrong_dict[4] = 'c'
		except Exception as e:
			pass

		try:
			opt5 = request.form['options5']
			if opt5 == 'c':
				i = i+1
				res  = 'true'
			else:
				ans = 'c'
				wrong_ans.append(opt5)
				correct_ans.append(ans)
				wrong_qstn.append(5)
				wrong_dict[5] = 'c'
		except Exception as e:
			pass

		try:
			opt6 = request.form['options6']
			if opt6 == 'a':
				i = i+1
				res  = 'true'
			else:
				ans = 'a'
				wrong_ans.append(opt6)
				correct_ans.append(ans)
				wrong_qstn.append(6)
				wrong_dict[6] = 'a'
		except Exception as e:
			pass

		try:
			opt7 = request.form['options7']
			if opt7 == 'c':
				i = i+1
				res  = 'true'
			else:
				ans = 'c'
				wrong_ans.append(opt7)
				correct_ans.append(ans)
				wrong_qstn.append(7)
				wrong_dict[7] = 'c'
		except Exception as e:
			pass

		try:
			opt8 = request.form['options8']
			if opt8 == 'd':
				i = i+1
				res  = 'true'
			else:
				ans = 'd'
				wrong_ans.append(opt8)
				correct_ans.append(ans)
				wrong_qstn.append(8)
				wrong_dict[8] = 'd'
		except Exception as e:
			pass

		try:
			opt9 = request.form['options9']
			if opt9 == 'b':
				i = i+1
				res  = 'true'
			else:
				ans = 'b'
				wrong_ans.append(opt9)
				correct_ans.append(ans)
				wrong_qstn.append(9)
				wrong_dict[9] = 'b'
		except Exception as e:
			pass

		try:
			opt10 = request.form['options10']
			if opt10 == 'd':
				i = i+1
				res  = 'true'
			else:
				ans = 'd'
				wrong_ans.append(opt10)
				correct_ans.append(ans)
				wrong_qstn.append(10)
				wrong_dict[10] = 'd'
		except Exception as e:
			pass

		if i == 5:
			message = "You're Extraordinaray!!"
			color = 'green'
		elif i == 4:
			message = "You're Good!!"
			color = 'green'
		elif i == 3:
			message = "Average...Practice More!!"
			color = 'orange'
		else:
			message = "You're Poor in this subject!!"
			color = 'red'
		wrong1 = [wrong_dict]
		return render_template('cnres.html',score = i,color=color,message = message,wrong1 = wrong1,ca = correct_ans,wa = wrong_ans,lst2 = wrong_qstn)
	return render_template('cnpaper.html')


@app.route('/cppage')
def cppage():
	lst2 = [0,1,2,3,4,5,6,7,8,9,10]
	random.shuffle(lst2)
	lst3 = lst2[0:5]
	return render_template('cppaper.html',lst2 = lst3)

@app.route('/cppaper',methods = ['GET','POST'])
def cppaper():
	if request.method == 'POST':
		wrong_ans = []
		correct_ans = []
		wrong_qstn = []
		wrong_dict = {}
		i = 0
		try:
			opt0 = request.form['options0']
			if opt0 == 'd':
				res  = 'true'
				i = i+1
				
			else:
				ans  = 'd'
				wrong_ans.append(opt0)
				correct_ans.append(ans)
				wrong_qstn.append(0)
				wrong_dict[0] = 'd'

		except Exception as e:
			pass

		try:
			opt1 = request.form['options1']
			if opt1 == 'c':
				res  = 'true'
				i = i+1

			else:
				ans = 'c'
				wrong_ans.append(opt1)
				correct_ans.append(ans)
				wrong_qstn.append(1)
				wrong_dict[1] = 'c'
		except Exception as e:
			pass

		try:
			opt2 = request.form['options2']
			if opt2 == 'b':
				res  = 'true'
				i = i+1
			else:
				ans = 'b'
				wrong_ans.append(opt2)
				correct_ans.append(ans)
				wrong_qstn.append(2)
				wrong_dict[2] = 'b'
		except Exception as e:
			pass

		try:
			opt3 = request.form['options3']
			if opt3 == 'd':
				res  = 'true'
				i = i+1
			else:
				ans = 'd'
				wrong_ans.append(opt3)
				correct_ans.append(ans)
				wrong_qstn.append(3)
				wrong_dict[3] = 'd'
		except Exception as e:
			pass

		try:
			opt4 = request.form['options4']
			if opt4 == 'c':
				res  = 'true'
				i = i+1
			else:
				ans = 'c'
				wrong_ans.append(opt4)
				correct_ans.append(ans)
				wrong_qstn.append(4)
				wrong_dict[4] = 'c'
		except Exception as e:
			pass

		try:
			opt5 = request.form['options5']
			if opt5 == 'd':
				i = i+1
				res  = 'true'
			else:
				ans = 'd'
				wrong_ans.append(opt5)
				correct_ans.append(ans)
				wrong_qstn.append(5)
				wrong_dict[5] = 'd'
		except Exception as e:
			pass

		try:
			opt6 = request.form['options6']
			if opt6 == 'a':
				i = i+1
				res  = 'true'
			else:
				ans = 'a'
				wrong_ans.append(opt6)
				correct_ans.append(ans)
				wrong_qstn.append(6)
				wrong_dict[6] = 'a'
		except Exception as e:
			pass

		try:
			opt7 = request.form['options7']
			if opt7 == 'a':
				i = i+1
				res  = 'true'
			else:
				ans = 'a'
				wrong_ans.append(opt7)
				correct_ans.append(ans)
				wrong_qstn.append(7)
				wrong_dict[7] = 'a'
		except Exception as e:
			pass

		try:
			opt8 = request.form['options8']
			if opt8 == 'd':
				i = i+1
				res  = 'true'
			else:
				ans = 'd'
				wrong_ans.append(opt8)
				correct_ans.append(ans)
				wrong_qstn.append(8)
				wrong_dict[8] = 'd'
		except Exception as e:
			pass

		try:
			opt9 = request.form['options9']
			if opt9 == 'c':
				i = i+1
				res  = 'true'
			else:
				ans = 'c'
				wrong_ans.append(opt9)
				correct_ans.append(ans)
				wrong_qstn.append(9)
				wrong_dict[9] = 'c'
		except Exception as e:
			pass

		try:
			opt10 = request.form['options10']
			if opt10 == 'a':
				i = i+1
				res  = 'true'
			else:
				ans = 'a'
				wrong_ans.append(opt10)
				correct_ans.append(ans)
				wrong_qstn.append(10)
				wrong_dict[10] = 'a'
		except Exception as e:
			pass

		if i == 5:
			message = "You're Extraordinaray!!"
			color = 'green'
		elif i == 4:
			message = "You're Good!!"
			color = 'green'
		elif i == 3:
			message = "Average...Practice More!!"
			color = 'orange'
		else:
			message = "You're Poor in this subject!!"
			color = 'red'
		wrong1 = [wrong_dict]
		return render_template('cpres.html',score = i,color=color,message = message,wrong1 = wrong1,ca = correct_ans,wa = wrong_ans,lst2 = wrong_qstn)
	return render_template('cppaper.html')





@app.route('/dbmspage')
def dbmspage():
	lst2 = [0,1,2,3,4,5,6,7,8,9,10]
	random.shuffle(lst2)
	lst3 = lst2[0:5]

	return render_template('dbmspaper.html',lst2 = lst3)

@app.route('/dbmspaper',methods = ['GET','POST'])
def dbmspaper():
	if request.method == 'POST':
		wrong_ans = []
		correct_ans = []
		wrong_qstn = []
		wrong_dict = {}
		i = 0
		try:
			opt0 = request.form['options0']
			if opt0 == 'a':
				res  = 'true'
				i = i+1
				
			else:
				ans  = 'a'
				wrong_ans.append(opt0)
				correct_ans.append(ans)
				wrong_qstn.append(0)
				wrong_dict[0] = 'a'

		except Exception as e:
			pass

		try:
			opt1 = request.form['options1']
			if opt1 == 'b':
				res  = 'true'
				i = i+1

			else:
				ans = 'b'
				wrong_ans.append(opt1)
				correct_ans.append(ans)
				wrong_qstn.append(1)
				wrong_dict[1] = 'b'
		except Exception as e:
			pass

		try:
			opt2 = request.form['options2']
			if opt2 == 'd':
				res  = 'true'
				i = i+1
			else:
				ans = 'd'
				wrong_ans.append(opt2)
				correct_ans.append(ans)
				wrong_qstn.append(2)
				wrong_dict[2] = 'd'
		except Exception as e:
			pass

		try:
			opt3 = request.form['options3']
			if opt3 == 'c':
				res  = 'true'
				i = i+1
			else:
				ans = 'c'
				wrong_ans.append(opt3)
				correct_ans.append(ans)
				wrong_qstn.append(3)
				wrong_dict[3] = 'c'
		except Exception as e:
			pass

		try:
			opt4 = request.form['options4']
			if opt4 == 'a':
				res  = 'true'
				i = i+1
			else:
				ans = 'a'
				wrong_ans.append(opt4)
				correct_ans.append(ans)
				wrong_qstn.append(4)
				wrong_dict[4] = 'a'
		except Exception as e:
			pass

		try:
			opt5 = request.form['options5']
			if opt5 == 'a':
				i = i+1
				res  = 'true'
			else:
				ans = 'a'
				wrong_ans.append(opt5)
				correct_ans.append(ans)
				wrong_qstn.append(5)
				wrong_dict[5] = 'a'
		except Exception as e:
			pass

		try:
			opt6 = request.form['options6']
			if opt6 == 'b':
				i = i+1
				res  = 'true'
			else:
				ans = 'b'
				wrong_ans.append(opt6)
				correct_ans.append(ans)
				wrong_qstn.append(6)
				wrong_dict[6] = 'b'
		except Exception as e:
			pass

		try:
			opt7 = request.form['options7']
			if opt7 == 'a':
				i = i+1
				res  = 'true'
			else:
				ans = 'a'
				wrong_ans.append(opt7)
				correct_ans.append(ans)
				wrong_qstn.append(7)
				wrong_dict[7] = 'a'
		except Exception as e:
			pass

		try:
			opt8 = request.form['options8']
			if opt8 == 'c':
				i = i+1
				res  = 'true'
			else:
				ans = 'c'
				wrong_ans.append(opt8)
				correct_ans.append(ans)
				wrong_qstn.append(8)
				wrong_dict[8] = 'c'
		except Exception as e:
			pass

		try:
			opt9 = request.form['options9']
			if opt9 == 'c':
				i = i+1
				res  = 'true'
			else:
				ans = 'c'
				wrong_ans.append(opt9)
				correct_ans.append(ans)
				wrong_qstn.append(9)
				wrong_dict[9] = 'c'
		except Exception as e:
			pass

		try:
			opt10 = request.form['options10']
			if opt10 == 'b':
				i = i+1
				res  = 'true'
			else:
				ans = 'b'
				wrong_ans.append(opt10)
				correct_ans.append(ans)
				wrong_qstn.append(10)
				wrong_dict[10] = 'b'
		except Exception as e:
			pass

		if i == 5:
			message = "You're Extraordinaray!!"
			color = 'green'
		elif i == 4:
			message = "You're Good!!"
			color = 'green'
		elif i == 3:
			message = "Average...Practice More!!"
			color = 'orange'
		else:
			message = "You're Poor in this subject!!"
			color = 'red'
		wrong1 = [wrong_dict]
		return render_template('dbmsres.html',score = i,color=color,message = message,wrong1 = wrong1,ca = correct_ans,wa = wrong_ans,lst2 = wrong_qstn)
	return render_template('dbmspaper.html')


@app.route('/radio',methods = ['GET','POST'])
def radio():
	if request.method == 'POST':
		wrong_ans = []
		correct_ans = []
		wrong_qstn = []
		wrong_dict = {}
		i = 0
		try:
			opt0 = request.form['options0']
			if opt0 == 'd':
				res  = 'true'
				i = i+1
				
			else:
				ans  = 'd'
				wrong_ans.append(opt0)
				correct_ans.append(ans)
				wrong_qstn.append(0)
				wrong_dict[0] = 'd'

		except Exception as e:
			pass

		try:
			opt1 = request.form['options1']
			if opt1 == 'b':
				res  = 'true'
				i = i+1

			else:
				ans = 'b'
				wrong_ans.append(opt1)
				correct_ans.append(ans)
				wrong_qstn.append(1)
				wrong_dict[1] = 'b'
		except Exception as e:
			pass

		try:
			opt2 = request.form['options2']
			if opt2 == 'd':
				res  = 'true'
				i = i+1
			else:
				ans = 'd'
				wrong_ans.append(opt2)
				correct_ans.append(ans)
				wrong_qstn.append(2)
				wrong_dict[2] = 'd'
		except Exception as e:
			pass

		try:
			opt3 = request.form['options3']
			if opt3 == 'c':
				res  = 'true'
				i = i+1
			else:
				ans = 'c'
				wrong_ans.append(opt3)
				correct_ans.append(ans)
				wrong_qstn.append(3)
				wrong_dict[3] = 'c'
		except Exception as e:
			pass

		try:
			opt4 = request.form['options4']
			if opt4 == 'a':
				res  = 'true'
				i = i+1
			else:
				ans = 'a'
				wrong_ans.append(opt4)
				correct_ans.append(ans)
				wrong_qstn.append(4)
				wrong_dict[4] = 'a'
		except Exception as e:
			pass

		try:
			opt5 = request.form['options5']
			if opt5 == 'b':
				i = i+1
				res  = 'true'
			else:
				ans = 'b'
				wrong_ans.append(opt5)
				correct_ans.append(ans)
				wrong_qstn.append(5)
				wrong_dict[5] = 'b'
		except Exception as e:
			pass

		try:
			opt6 = request.form['options6']
			if opt6 == 'c':
				i = i+1
				res  = 'true'
			else:
				ans = 'c'
				wrong_ans.append(opt6)
				correct_ans.append(ans)
				wrong_qstn.append(6)
				wrong_dict[6] = 'c'
		except Exception as e:
			pass

		try:
			opt7 = request.form['options7']
			if opt7 == 'c':
				i = i+1
				res  = 'true'
			else:
				ans = 'c'
				wrong_ans.append(opt7)
				correct_ans.append(ans)
				wrong_qstn.append(7)
				wrong_dict[7] = 'c'
		except Exception as e:
			pass

		try:
			opt8 = request.form['options8']
			if opt8 == 'b':
				i = i+1
				res  = 'true'
			else:
				ans = 'b'
				wrong_ans.append(opt8)
				correct_ans.append(ans)
				wrong_qstn.append(8)
				wrong_dict[8] = 'b'
		except Exception as e:
			pass

		try:
			opt9 = request.form['options9']
			if opt9 == 'b':
				i = i+1
				res  = 'true'
			else:
				ans = 'b'
				wrong_ans.append(opt9)
				correct_ans.append(ans)
				wrong_qstn.append(9)
				wrong_dict[9] = 'b'
		except Exception as e:
			pass

		try:
			opt10 = request.form['options10']
			if opt10 == 'a':
				i = i+1
				res  = 'true'
			else:
				ans = 'a'
				wrong_ans.append(opt10)
				correct_ans.append(ans)
				wrong_qstn.append(10)
				wrong_dict[10] = 'a'
		except Exception as e:
			pass

		if i == 5:
			message = "You're Extraordinaray!!"
			color = 'green'
		elif i == 4:
			message = "You're Good!!"
			color = 'green'
		elif i == 3:
			message = "Average...Practice More!!"
			color = 'orange'
		else:
			message = "You're Poor in this subject!!"
			color = 'red'
		slist = session['lst2']
		wrong1 = [wrong_dict]
		return render_template('register.html',score = i,color=color,message = message,wrong1 = wrong1,ca = correct_ans,wa = wrong_ans,lst2 = wrong_qstn)
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
	app.secret_key = 'hai123'
	app.run(debug = True)
