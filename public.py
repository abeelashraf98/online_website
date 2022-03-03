from flask import *
from database import *
import uuid 
public=Blueprint('public',__name__)

@public.route('/')

def home():
	return render_template('home.html')


@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(uname,password)
		res=select(q)
		print(res)
		if res:
			session['lid']=res[0]['login_id']
			lid=session['lid']
			if res[0]['usertype']=='admin':
				return redirect(url_for('admin.adminhome'))
			if res[0]['usertype']=='institution':
				q="select * from institution where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['insti_id']=res[0]['institution_id']
				return redirect(url_for('institute.institute_home'))
			if res[0]['usertype']=='speaker':
				q="select * from speaker where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['speak_id']=res[0]['speaker_id']
				return redirect(url_for('speaker.speaker_home'))

			if res[0]['usertype']=='user':
				q="select * from user where login_id='%s'"%(lid)
				res=select(q)
				if res:
					session['user_id']=res[0]['user_id']
				return redirect(url_for('user.user_home'))
		else:
			flash("invalid username and password")


	return render_template('login.html')

@public.route('/institute_signup',methods=['get','post'])
def institute_signup():
	if 'submit' in request.form:
		iname=request.form['iname']
		email=request.form['email']
		uname=request.form['uname']
		password=request.form['password']
		phone=request.form['phone']
		place=request.form['place']
		pincode=request.form['pincode']
		q="select * from login where username='%s'"%(uname)
		res=select(q)
		if res:
			flash("username is already exists")
		else:
			q="insert into login values(null,'%s','%s','institution')"%(uname,password)
			id=insert(q)
			q="insert into institution values(null,'%s','%s','%s','%s','%s','%s')"%(id,iname,place,phone,email,pincode)
			insert(q)

	return render_template('institute_register.html')

@public.route('/user_signup',methods=['get','post'])
def  user_signup():
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		email=request.form['email']
		uname=request.form['uname']
		password=request.form['password']
		phone=request.form['phone']
		place=request.form['place']
		q="select * from login where username='%s'"%(uname)
		res=select(q)
		if res:
			flash("username is already exists")
		else:
			q="insert into login values(null,'%s','%s','user')"%(uname,password)
			id=insert(q)
			q="insert into user values(null,'%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email)
			insert(q)
	return render_template('user_register.html')

@public.route('/speaker_signup',methods=['get','post'])
def speaker_signup():
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		email=request.form['email']
		uname=request.form['uname']
		password=request.form['password']
		phone=request.form['phone']
		place=request.form['place']
		subject=request.form['sub']
		designation=request.form['designation']
		description=request.form['description']
		image=request.files['image']
		path='static/'+str(uuid.uuid4())+image.filename
		image.save(path)
		q="select * from login where username='%s'"%(uname)
		res=select(q)
		if res:
			flash("username is already exists")
		else:
			q="insert into login values(null,'%s','%s','pending')"%(uname,password)
			id=insert(q)
			q="insert into speaker values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(id,fname,lname,place,phone,email,description,subject,path,designation)
			insert(q)
	return render_template('speaker_register.html')

