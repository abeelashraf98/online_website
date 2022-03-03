from flask import *
from database import *

user=Blueprint('user',__name__)


@user.route('/user_home',methods=['get','post'])
def user_home():
	data={}
	# if 'action' in request.args:
	# 	val=request.args['val']

		
	# 	return redirect(url_for('user.user_view_speaker',val=val))
	# if 'submit' in request.form:
	# 	search=request.form['search']
	# 	search=search+"%"
	# 	print(search)
	# 	q="select * from speaker where first_name like '%s'"%(search)
	# 	res=select(q)
	# 	data={}
	# 	data['search']=res
	# 	print(res)


	q="select DISTINCT place from speaker"
	res2=select(q)
	data['place']=res2

	q="select DISTINCT subject from speaker"
	res3=select(q)
	data['subject']=res3

	q="select DISTINCT designation from speaker"
	res4=select(q)
	data['designation']=res4


	if 'action' in request.args:
		val=request.args['val']
		return redirect(url_for('institute.institute_view_speaker',val=val))

	q="select * from speaker"
	res1=select(q)
	data['sp']=res1

	if 'search' in request.form:
		search=request.form['searchs']
		print(search)
		q="SELECT * FROM speaker WHERE  `place`='%s' OR `subject`='%s' OR `designation`='%s'"%(search,search,search)
		print(q)
		res1=select(q)
		data['sp']=res1


		
	return render_template('user_home.html',data=data)



@user.route('/user_view_speaker')
def user_view_speaker():
	data={}
	val=request.args['val']
	q="select * from speaker where subject='%s'"%(val)
	print(q)
	res=select(q)
	data['sp']=res
	# print(res)
	if 'action' in request.args:
		id=request.args['id']
		# q="select * from speaker where login_id='%s'"%(id)
		# res=select(q)
		if res:
			return redirect(url_for('user.user_viewdetail',id=id))
	return render_template('user_viewspeaker.html',data=data,val=val)

@user.route('/user_viewdetail')
def user_viewdetail():
	data={}
	id=request.args['id']
	q="select * from speaker where speaker_id='%s'"%(id)
	res=select(q)
	data['speak']=res

	q="SELECT * FROM `education` WHERE `speaker_id`='%s'"%(id)
	res=select(q)
	data['edu']=res
	q2="SELECT * FROM `experience` WHERE `speaker_id`='%s'"%(id)
	res1=select(q2)
	data['exp']=res1


	q5="SELECT *,AVG(`rate`) AS avrate FROM `rating` WHERE `rated_for_id`=(SELECT `login_id` FROM `speaker` WHERE `speaker_id`='%s')"%(id)
	ress=select(q5)
	data['star_rate']=ress[0]['avrate']
	print(data['star_rate'])

	q3="SELECT * FROM `interest` WHERE `speaker_id`='%s'"%(id)
	res2=select(q3)
	data['interest']=res2
	print(res)
	return render_template('user_viewdetail.html',data=data)

@user.route('/user_complaint',methods=['get','post'])
def user_complaint():
	lid=session['lid']
	if 'submit' in request.form:
		complaint=request.form['complaint']
		print(complaint)
		q="insert into complaint values(null,'%s','%s','pending',now())"%(lid,complaint)
		insert(q)
	q="select * from complaint where login_id='%s'"%(lid)
	res=select(q)
	data={}
	data['reply']=res
	return render_template('user_complaint.html',data=data)

@user.route('/search')
def search():
	d=request.args['data']
	print(d)
	print(d['search'])

	return render_template('user_search.html',data=d)

@user.route('/user_chat',methods=['get','post'])
def user_chat():
	data={}
	user_id=session['lid']
	data['user_id']=user_id
	lid=request.args['lid']
	name=request.args['name']
	data['name']=name
	data['lid']=lid
	if 'submit' in request.form:
		msg=request.form['msg']
		q="insert into chat values(NULL,'%s','%s','%s',NOW())"%(user_id,lid,msg)
		insert(q)
		return redirect(url_for('user.user_chat',lid=lid,name=name))
	q="select * from chat where (sender_id='%s' and reciever_id='%s')or (sender_id='%s' and reciever_id='%s')"%(lid,user_id,user_id,lid)
	res=select(q)
	print(q)
	print(res)
	data['chat']=res
	return render_template('user_chat.html',data=data)


@user.route('/user_rate',methods=['get','post'])
def institute_make_rate():
	
	data={}
	inslid=session['lid']
	data['inslid']=inslid

	sp_lid=request.args['sp_lid']

	name=request.args['name']
	data['name']=name

	if 'rate' in request.form:
		rates=request.form['rates']
		review=request.form['review']
		q="SELECT * FROM rating  WHERE `ratedby_id`='%s' AND `rated_for_id`='%s'"%(inslid,sp_lid)
		ress=select(q)
		if ress:
			qu="UPDATE `rating` SET `rate`='%s',`review`='%s',`date`=CURDATE() WHERE `ratedby_id`='%s' AND `rated_for_id`='%s'"%(rates,review,inslid,sp_lid)
			print(qu)
			update(qu)
		else:
			q="INSERT INTO `rating` VALUES(NULL,'%s','%s','%s','%s',CURDATE())"%(inslid,sp_lid,rates,review)
			ri=insert(q)

		flash("Successfully Rated")
		return redirect(url_for('user.user_rate',sp_lid=sp_lid,name=name))

	q="SELECT * FROM rating  WHERE `ratedby_id`='%s' AND `rated_for_id`='%s'"%(inslid,sp_lid)
	ress=select(q)
	if ress:
		data['rating']=ress

 

	return render_template('user_rate.html',data=data)
