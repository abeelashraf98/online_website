from flask import *
from database import *

institute=Blueprint('institute',__name__)


@institute.route('/institute_home',methods=['get','post'])
def institute_home():
	data={}

	

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
		search1=request.form['searchs1']
		search2=request.form['searchs2']
		print(search)
		q="SELECT * FROM speaker WHERE  `place`='%s' OR `subject`='%s' OR `designation`='%s'"%(search,search1,search2)
		print(q)
		res1=select(q)
		data['sp']=res1


		
	return render_template('institute_home.html',data=data)


@institute.route('/institute_view_speaker')
def institute_view_speaker():
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
			return redirect(url_for('institute.institute_viewdetail',id=id))
	return render_template('institute_viewspeaker.html',data=data,val=val)

@institute.route('/institute_viewdetail')
def institute_viewdetail():
	data={}
	id=request.args['id']
	q="select * from speaker where speaker_id='%s'"%(id)
	res=select(q)
	data['speak']=res
	print(res)

	q="SELECT *,AVG(`rate`) AS avrate FROM `rating` WHERE `rated_for_id`=(SELECT `login_id` FROM `speaker` WHERE `speaker_id`='%s')"%(id)
	ress=select(q)
	data['star_rate']=ress[0]['avrate']
	print(data['star_rate'])
	q="SELECT * FROM `education` WHERE `speaker_id`='%s'"%(id)
	res=select(q)
	data['edu']=res
	q2="SELECT * FROM `experience` WHERE `speaker_id`='%s'"%(id)
	res1=select(q2)
	data['exp']=res1

	q3="SELECT * FROM `interest` WHERE `speaker_id`='%s'"%(id)
	res2=select(q3)
	data['interest']=res2


	return render_template('institute_viewdetail.html',data=data)

@institute.route('/institute_complaint',methods=['get','post'])
def institute_complaint():
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
	return render_template('institute_complaint.html',data=data)

@institute.route('/search')
def search():
	d=request.args['data']
	print(d)
	print(d['search'])

	return render_template('institute_search.html',data=d)

@institute.route('/institute_chat',methods=['get','post'])
def institute_chat():
	
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
		return redirect(url_for('institute.institute_chat',lid=lid,name=name))
	q="select * from chat where (sender_id='%s' and reciever_id='%s')or (sender_id='%s' and reciever_id='%s')"%(lid,inslid,inslid,lid)
	res=select(q)
	print(q)
	print(res)
	data['chat']=res
	return render_template('institute_chat.html',data=data)





@institute.route('/institute_make_rate',methods=['get','post'])
def institute_make_rate():
	
	data={}
	inslid=session['lid']
	data['inslid']=inslid

	sp_lid=request.args['sp_lid']

	name=request.args['name']
	data['name']=name

	if 'rate' in request.form:
		rates=request.form['rates']
		# review=request.form['review']
		q="SELECT * FROM rating  WHERE `ratedby_id`='%s' AND `rated_for_id`='%s'"%(inslid,sp_lid)
		ress=select(q)
		if ress:
			qu="UPDATE `rating` SET `rate`='%s',`date`=CURDATE() WHERE `ratedby_id`='%s' AND `rated_for_id`='%s'"%(rates,inslid,sp_lid)
			print(qu)
			update(qu)
		else:
			q="INSERT INTO `rating` VALUES(NULL,'%s','%s','%s',CURDATE())"%(inslid,sp_lid,rates)
			ri=insert(q)

		flash("Successfully Rated")
		return redirect(url_for('institute.institute_make_rate',sp_lid=sp_lid,name=name))

	q="SELECT * FROM rating  WHERE `ratedby_id`='%s' AND `rated_for_id`='%s'"%(inslid,sp_lid)
	ress=select(q)
	if ress:
		data['rating']=ress

 

	return render_template('institute_make_rate.html',data=data)
