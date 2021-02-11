from flask import Flask,render_template,url_for
from flask import *
from pandas import *
import random
import pyrebase
from fpdf import FPDF
import json
import random
import string
import os
from datetime import datetime
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
storage = firebase.storage()
authen = firebase.auth()
db = firebase.database()

app = Flask(__name__)

app.secret_key = "hellosudeep"
@app.route('/')

def home():
	if 'loggedin' in session:
		return render_template('home.html',btn = 'logout')
	else:
		return render_template('home.html')


@app.route('/register1')
def register1():
	if 'loggedin' in session:
		return render_template('home.html')
	else:
		return render_template('userregister.html')
@app.route('/authentication',methods = ['GET','POST'])
def authentication():
	if request.method == 'POST':
		if 'loggedin' in session:
			return render_template('home.html',btn = 'logout')
		else:
			regno = request.form['regno']

			password = request.form['password']
			repassword = request.form['re-password']
			if password == repassword:
				data = {'regno':regno,'password':password}
				db.child(regno).push(data)
				return render_template('userlogin.html',msg = "Registration Successfull..")
			else:
				return render_template('userregister.html',msg = "Password incorrect")
			
	return render_template('userregister.html')
	

@app.route('/signin')
def signin():
	if 'loggedin' in session:
		return render_template('home.html')
	else:
		return render_template('userlogin.html')
@app.route('/auth',methods = ['GET','POST'])
def auth():
	if request.method == 'POST':
		if 'loggedin' in session:
			return render_template('home.html', btn = 'logout')
		else:
			regno = request.form['regno']
			password = request.form['password']
			try:
				user = db.child(regno).get()
				if user:
					for details in user.each():
						for a,b in details.val().items():
							if a == 'password':
								if b == password:
									session['loggedin'] = True
									session['reg'] = regno
									return render_template('home.html',btn = 'logout')
								else:
									return render_template('userlogin.html',msg = "Credentials Incorrect")

			except:
				return "Incorrect Details....."
	return render_template('home.html',btn = 'logout')
@app.route('/logout')
def logout():
	session.pop('loggedin', None)
	session.pop('reg', None)
	return render_template('home.html')


@app.route('/checkmarks')
def checkmarks():
	if 'loggedin' in session:
		reg = session['reg']
		return render_template('checkmarks.html',reg = reg)
	else:
		return redirect(url_for('signin'))


@app.route('/checking',methods = ['GET','POST'])
def checking():
	if 'loggedin' in session:
		if request.method == 'POST':
			reg = session['reg']
			ear = request.form['ear']

			try:
				res1 = db.child(ear).child(reg).child("mid 1").get()
				res2 = db.child(ear).child(reg).child("mid 2").get()
				mid1 = ""
				mid2 = ""
				data = {}
				data1 = {}
				ft = {}
				for marks in res1.each():
					for a,b in marks.val().items():
						a = str(a)
						b = str(b)
						mid1 =  mid1 + f" {a} --> {b} ||"
				for marks1 in res2.each():
					for a,b in  marks1.val().items():
						a = str(a)
						b = str(b)
						mid2 = mid2 + f" {a} --> {b} ||"
				for task in res1.each():
					for task1 in res2.each():
						for a,b in task.val().items():
							for a2,b2 in task1.val().items():
								if a == a2:
									v1 = int(b)
									v2 = int(b2)
									if v1 > v2:
										ep = (v1*80)/100
										tp = (v2*20)/100
										fp = ep+tp
										ft[a2] = fp
										data[a2] = ep
										data1[a2] = tp
									elif v1 <= v2:
										ep = (v2*80)/100
										tp = (v1*20)/100
										fp = ep+tp
										ft[a2] = fp
										data[a2] = ep
										data1[a2] = tp
				pdf = FPDF()

				pdf.add_page() 

				pdf.set_font("Arial", size = 15)
				pdf.cell(200, 10, txt = "mid 1",ln = 1, align = 'C')
				pdf.cell(200, 10, txt = mid1,ln = 1, align = 'C')
				pdf.cell(200, 10, txt = "mid 2",ln = 1, align = 'C')
				pdf.cell(200, 10, txt = mid2,ln = 2, align = 'C')
				random1 = ''.join([random.choice(string.ascii_letters 
			            + string.digits) for n in range(10)]) 
				filen = f'{reg}-{ear}-{random1}.pdf'
				session['filen'] = filen
				pdf.output(filen)
				storage.child(f"pdf/{filen}").put(filen)
				url1 = storage.child(f'pdf/{filen}').get_url(None)
				return render_template('ress.html',res1=res1, res2 = res2,data = data,data1 = data1,ft = ft,url = url1,reg = reg,ear = ear)

			except:
				mid1 = ""
				mid2 = "No Data Found"
				res1 = db.child(ear).child(reg).child("mid 1").get()
				res2 = "No Data Found"
				for marks in res1.each():
					for a,b in marks.val().items():
						a = str(a)
						b = str(b)
						mid1 = mid1 + f" {a} --> {b} ||"
				pdf = FPDF()

				pdf.add_page() 

				pdf.set_font("Arial", size = 15)
				pdf.cell(200, 10, txt = "mid 1",ln = 1, align = 'C')
				pdf.cell(200, 10, txt = mid1,ln = 1, align = 'C')
				pdf.cell(200, 10, txt = "mid 2",ln = 1, align = 'C')
				pdf.cell(200, 10, txt = mid2,ln = 2, align = 'C')
				random1 = ''.join([random.choice(string.ascii_letters 
			            + string.digits) for n in range(10)]) 
				filen = f'{reg}-{ear}-{random1}.pdf'
				session['filen'] = filen
				pdf.output(filen)
				storage.child(f"pdf/{filen}").put(filen)
				url1 = storage.child(f'pdf/{filen}').get_url(None)
				return render_template('ress.html',res1 = res1,res2 = res2,url = url1,reg = reg,ear = ear)
	else:
		return render_template('userlogin.html')
	
	return render_template('checkmarks.html')

@app.route('/dashboard')
def dashboard():
	if 'loggedin' in session:
		return render_template('dashboard.html')
	else:
		return render_template('userlogin.html')


@app.route('/feescheck')
def feescheck():
	if 'loggedin' in session:
		regno = session['reg']
		return render_template('feescheck.html',regno = regno)
	else:
		return render_template('userlogin.html')

@app.route('/fee',methods = ['GET','POST'])
def fee():
	if 'loggedin' in session:
		if request.method == "POST":
			regno = request.form['regno']
			sem = request.form['sem']
			fee_det = db.child("fees").child(regno).child(sem).get()
			return render_template('feeres.html',fee = fee_det,reg = regno,sem = sem)
	else:
		return render_template('userlogin.html')

	return render_template('home.html')



@app.route('/attendfirst')
def attendfirst():
	if 'loggedin' in session:
		regno = session['reg']
		hour = []
		status = []
		main_data = []
		no = 0
		months = ['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sept','Oct','Nov','Dec']
		today = datetime.today()
		a = today.month - 1
		curr_month = months[a]
		date = today.date()
		data = db.child("attendence").child(curr_month).child(date).child(regno).get()
		print(data.each())
		for att in data.each():
			for a in att.val().items():
				hour.append(a[0])
				if a[1] == "1":

					status.append('Present')
					no = no+1
					
				elif a[1] == "0":
			
					status.append('Absent')
		per = int((no/7)*100)
		
		ac = []
		pc =[]
		data1 =  db.child("attendence").child(curr_month).child(regno).get()
		for att in data1.each():
			for m,n in att.val().items():
				
				ac.append(m)
				pc.append(n)
		return render_template('attendcheck.html',hour = hour,status = status,reg = regno,per = per,ac = ac,pc = pc)
	else:
		return render_template('userlogin.html')

	return render_template('attendcheck.html')

@app.route('/attendcheck')
def attendcheck():
	
	regno = session['reg']
	hour = []
	status = []
	main_data = []
	months = ['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sept','Oct','Nov','Dec']
	today = datetime.today()
	a = today.month - 1
	curr_month = months[a]
	date = today.date()
	data = db.child("attendence").child(curr_month).child(date).child(regno).get()
	for att in data.each():
		for a in att.val().items():
			hour.append(a[0])
			status.append(a[1])

	data = {
	"status":status
	}


	return data
















@app.route('/adminlogin')
def adminlogin():
	if 'adminlogin' in session:
		return render_template('adminpage.html')
	else:
		return render_template('adminlogin1.html')
@app.route('/validate',methods = ['GET','POST'])
def validate():
	
	if request.method == 'POST':
		name = request.form.get('name')
		password = request.form.get('password')

		if name == 'akrg123@gmail.com' and  password == 'akrgadmincp':
			session['adminlogin'] = True
			return render_template('adminpage.html')
		else:
			return render_template('adminlogin1.html')
	return render_template('home.html')

@app.route('/select')
def select():
	if 'adminlogin' in session:
		return render_template('files1.html')
	else:
		return render_template('adminlogin1.html')
@app.route('/upload', methods = ['GET','POST'])
def upload():
	if request.method == 'POST':
		f = request.files['file']
		ear = request.form['ear']
		mid = request.form['mid']
		f.save(f.filename)
		with open(f.filename,mode = 'r') as f:
			csv_list = [[val.strip() for val in r.split(",")] for r in f.readlines()]

		(_, *header), *data = csv_list
		csv_dict = {}
		for row in data:
			key, *values = row
			csv_dict[key] = {key: value for key, value in zip(header, values)}
		for a,b in csv_dict.items():
			db.child(ear).child(a).child(mid).push(b)
			msg =  "Successfully uploaded"
		return render_template('files1.html',msg = msg)
		
	return render_template('files1.html')

@app.route('/deletefile')
def deletefile():
	if 'adminlogin' in session:
		return render_template('deletefile.html')
	else:
		return render_template('adminlogin1.html')
@app.route('/delete',methods = ['GET','POST'])
def delete():
	if 'adminlogin' in session:
		if request.method == 'POST':
			regno = request.form['registerno']
			mid = request.form['mid']
			semid = request.form['semid']
			db.child(semid).child(regno).child(mid).remove()
			message = 'Data Deleted Successfully'
			return render_template('deletefile.html',msg = message)
		else:
			return "OOPSS....No Data Found...!!"
	else:
		return render_template('adminlogin1.html')
	return render_template('deletefile.html')

@app.route('/fees')
def fees():
	if 'adminlogin' in session:
		return render_template('feeselect.html')
	else:
		return render_template('adminlogin1.html')

@app.route('/feesdetails',methods = ['GET','POST'])
def feesdetails():
	if request.method == 'POST':
		f = request.files['file']
		sem = request.form['sem']
		
		f.save(f.filename)
		with open(f.filename,mode = 'r') as f:
			csv_list = [[val.strip() for val in r.split(",")] for r in f.readlines()]

		(_, *header), *data = csv_list
		csv_dict = {}
		for row in data:
			key, *values = row
			csv_dict[key] = {key: value for key, value in zip(header, values)}
		for a,b in csv_dict.items():
			db.child("fees").child(a).child(sem).push(b)
		msg =  "Successfully uploaded"
		return render_template('feeselect.html',msg = msg)
		

	return render_template('feeselect.html')

@app.route('/updatefees')
def updatefees():
	return render_template('selectupdatef.html')
@app.route('/feeupdation',methods = ['GET','POST'])
def feeupdation():
	if request.method == 'POST':
		f = request.files['file']
		sem = request.form['sem']
		
		f.save(f.filename)
		with open(f.filename,mode = 'r') as f:
			csv_list = [[val.strip() for val in r.split(",")] for r in f.readlines()]

		(_, *header), *data = csv_list
		csv_dict = {}
		for row in data:
			key, *values = row
			csv_dict[key] = {key: value for key, value in zip(header, values)}
		for a,b in csv_dict.items():
			data = db.child("fees").child(a).child(sem).get()
			main_data = db.child("fees").child(a).child(sem).get()
			db.child("fees").child(a).child(sem).remove()
		for a,b in csv_dict.items():
			db.child("fees").child(a).child(sem).push(b)
			msg = "Successfully updated....."
		return render_template("selectupdatef.html",msg = msg)

	return render_template('feeupdation.html')



@app.route('/selectattendence')
def selectattendence():
	if 'adminlogin' in session:
		return render_template('selectattendence.html')
	else:
		return render_template('adminlogin1.html')

@app.route('/attendenceupdate',methods = ['GET','POST'])
def attendenceupdate():
	if request.method == 'POST':
		ac = 0
		pc = 0
		months = ['Jan','Feb','Mar','Apr','May','June','Jul','Aug','Sept','Oct','Nov','Dec']
		today = datetime.today()
		a = today.month - 1
		curr_month = months[a]
		f = request.files['file']
		date = today.date()
		f.save(f.filename)
		with open(f.filename,mode = 'r') as f:
			csv_list = [[val.strip() for val in r.split(",")] for r in f.readlines()]

		(_, *header), *data = csv_list
		csv_dict = {}
		for row in data:
			key, *values = row
			csv_dict[key] = {key: value for key, value in zip(header, values)}
		for a,b in csv_dict.items():
			db.child("attendence").child(curr_month).child(date).child(a).push(b)
		for a1,b1 in csv_dict.items():
			data = db.child("attendence").child(curr_month).child(date).child(a1).get()
			for att in data.each():
				for a in att.val().items():

					if a[1] == "1":
		
						pc = pc+1
					elif a[1] == "0":
						ac = ac+1

			b = {
			'total absent':ac,
			'total present':pc
			}

			ac = 0
			pc =0

			data = db.child("attendence").child(curr_month).child(a1).push(b)
			msg =  "Successfully uploaded"
		return render_template('selectattendence.html',msg = msg)

	return render_template('selectattendence.html')

@app.route('/adminout')
def adminout():
	session.pop('adminlogin',None)
	return render_template('home.html')





















@app.route('/resu')
def resu():
	
	return render_template('resu.html')
@app.route('/home')


@app.route('/sd')
def sd():
	if 'loggedin' in session:
		return render_template('sd.html')
	else:
		return render_template('login.html')


@app.route('/nodata')
def nodata():
	return render_template('noda	ta.html')
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
	session['lst2'] = lst3
	return render_template('testpaper.html',lst2 = lst3)

@app.route('/cnpage')
def cnpage():
	lst2 = [0,1,2,3,4,5,6,7,8,9,10]
	random.shuffle(lst2)
	lst3 = lst2[0:5]
	session['lst2'] = lst3
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
	session['lst2'] = lst3
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
	session['lst2'] = lst3
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
