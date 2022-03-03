from flask import *
from database import *
import uuid
speaker=Blueprint('speaker',__name__)

@speaker.route('/speaker_home')
def speaker_home():
	return render_template('speaker_home.html')


@speaker.route('/speaker_Profile',methods=['get','post'])
def speaker_Profile():
	data={}
	lid=session['lid']
	spid=session['speak_id']
	q="SELECT * FROM `speaker` INNER JOIN `login` USING(`login_id`) WHERE `login_id`='%s'"%(lid)
	res=select(q)
	if res:
		data['my_profile']=res
		print(res)

	if 'action' in request.args:
		action=request.args['action']
		lids=request.args['lids']
		q="SELECT * FROM `speaker` INNER JOIN `login` USING(`login_id`) WHERE `login_id`='%s'"%(lids)
		ress=select(q)
		data['edit_profile']=ress

	if 'esubmit' in request.form:
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

		q="UPDATE `login` SET `username`='%s',`password`='%s' where `login_id`='%s'"%(uname,password,lids)
		print(q)
		update(q)
		if image.filename =="":
			q="UPDATE `speaker` SET `first_name`='%s',`last_name`='%s',`place`='%s',`phone`='%s',`email`='%s',`description`='%s',`subject`='%s',`designation`='%s' WHERE `login_id`='%s'"%(fname,lname,place,phone,email,description,subject,designation,lids)
			update(q)
		else:
			
			q="UPDATE `speaker` SET `first_name`='%s',`last_name`='%s',`place`='%s',`phone`='%s',`email`='%s',`description`='%s',`subject`='%s',`image`='%s',`designation`='%s' WHERE `login_id`='%s'"%(fname,lname,place,phone,email,description,subject,path,designation,lids)
			update(q)
		
		return redirect(url_for('speaker.speaker_Profile'))

	q="SELECT * FROM `education` WHERE `speaker_id`='%s'"%(spid)
	res=select(q)
	if res:
		data['edu']=res
	q2="SELECT * FROM `experience` WHERE `speaker_id`='%s'"%(spid)
	res1=select(q2)
	if res1:
		data['exp']=res1

	q2="SELECT * FROM `interest` WHERE `speaker_id`='%s'"%(spid)
	res1=select(q2)
	if res1:
		data['interest']=res1

	return render_template('speaker_Profile.html',data=data)

@speaker.route('/speaker_complaint',methods=['get','post'])
def speaker_complaint():
	lid=session['lid']
	q="select * from complaint where login_id='%s'"%(lid)
	res=select(q)
	data={}
	data['reply']=res
	if 'submit' in request.form:
		complaint=request.form['complaint']
		print(complaint)
		q="insert into complaint values(null,'%s','%s','pending',now())"%(lid,complaint)
		insert(q)
		return redirect(url_for('speaker.speaker_complaint'))
	return render_template('speaker_complaint.html',data=data)
@speaker.route('/speaker_chat',methods=['get','post'])
def speaker_chat():
	data={}
	inslid=session['lid']
	data['inslid']=inslid
	lid=request.args['lid']
	name=request.args['name']
	data['name']=name
	data['lid']=lid
	if 'submit' in request.form:
		msg=request.form['msg']
		q="insert into chat values(NULL,'%s','%s','%s',NOW())"%(inslid,lid,msg)
		insert(q)
		return redirect(url_for('speaker.speaker_chat',lid=lid,name=name))
	q="select * from chat where (sender_id='%s' and reciever_id='%s')or (sender_id='%s' and reciever_id='%s')"%(lid,inslid,inslid,lid)
	res=select(q)
	print(q)
	print(res)
	data['chat']=res
	return render_template('spaeker_chat.html',data=data)
@speaker.route('/speakerview_inst')
def speakerview_inst():
	data={}
	q="select * from institution" 
	res=select(q)
	data['institute']=res
	print(res)
	return render_template('speakerview_institute.html',data=data)




@speaker.route('/speaker_view_user_chat',methods=['get','post'])
def speaker_view_user_chat():
	data={}
	lid=session['lid']
	q="SELECT * FROM `chat` INNER JOIN user on `chat`.`sender_id` = `user`.`login_id` WHERE `reciever_id`='%s'  GROUP BY `sender_id`"%(lid)
	print(q)
	res=select(q)
	data['chated_users']=res
	print(res)
	return render_template('speaker_view_user_chat.html',data=data)

@speaker.route("/speaker_chat_with_user",methods=['get','post'])
def speaker_chat_with_user():
	data={}
	inslid=session['lid']
	data['inslid']=inslid
	lid=request.args['lid']
	name=request.args['name']
	data['name']=name
	data['lid']=lid
	if 'submit' in request.form:
		msg=request.form['msg']
		q="insert into chat values(NULL,'%s','%s','%s',NOW())"%(inslid,lid,msg)
		insert(q)
		return redirect(url_for('speaker.speaker_chat_with_user',lid=lid,name=name))
	q="select * from chat where (sender_id='%s' and reciever_id='%s')or (sender_id='%s' and reciever_id='%s')"%(lid,inslid,inslid,lid)
	res=select(q)
	print(q)
	print(res)
	data['chat']=res

	return render_template("speaker_chat_with_user.html",data=data)


@speaker.route('/speaker_ed',methods=['get','post'])
def speaker_ed():
	sid=session['speak_id']
	# lids=request.args['lids']

	if 'submit' in request.form:
		degree=request.form['degree']
		unv=request.form['unv']
		year=request.form['year']
		q="insert into education values(null,'%s','%s','%s','%s')"%(sid,degree,unv,year)
		insert(q)
		return redirect(url_for('speaker.speaker_Profile'))
	data={}
	q="select * from education"
	res=select(q)
	data['view_ed']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="edit":
		q="SELECT * FROM `education` WHERE `ed_id`='%s'"%(id)
		ress=select(q)
		data['ued']=ress

	if 'usubmit' in request.form:
		degree=request.form['degree']
		unv=request.form['unv']
		year=request.form['year']
		q="UPDATE `education` SET `degree`='%s',`university`='%s',`year`='%s' WHERE `ed_id`='%s'"%(degree,unv,year,id)
		update(q)
		return redirect(url_for('speaker.speaker_Profile'))


	

	return render_template('speaker_ed.html',data=data)


@speaker.route('/speaker_exp',methods=['get','post'])
def speaker_exp():
	sid=session['speak_id']
	if 'submit' in request.form:
		cname=request.form['cname']
		desg=request.form['desg']
		year=request.form['year']
		
		q="insert into experience values(null,'%s','%s','%s','%s')"%(sid,cname,desg,year)
		insert(q)
		return redirect(url_for('speaker.speaker_Profile'))

	return render_template('speaker_exp.html')


@speaker.route('/speaker_area',methods=['get','post'])
def speaker_area():
	sid=session['speak_id']
	if 'submit' in request.form:
		interest=request.form['interest']
		
		q="insert into interest values(null,'%s','%s')"%(sid,interest)
		insert(q)
		return redirect(url_for('speaker.speaker_Profile'))

	return render_template('speaker_area.html')