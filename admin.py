from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/adminhome')
def adminhome():
	return render_template('adminhome.html')


@admin.route('/view_speaker',methods=['get','post'])
def view_speaker():
	data={}
	q="select * from speaker"
	res=select(q)
	data['speak']=res

	if 'action' in request.args:
		action=request.args['action']
		id=request.args['id']
	else:
		action=None

	if action=="accept":
		q="update login set usertype='speaker' where login_id='%s'" %(id)
		update(q)
		return redirect(url_for('admin.view_speaker'))

	if action=="reject":
		q="delete from login where login_id='%s'" %(id)
		delete(q)
		q="delete from speaker where login_id='%s'" %(id)
		delete(q)
		return redirect(url_for('admin.view_speaker'))
	return render_template('admin_viewspeaker.html',data=data)

@admin.route('/view_institute',methods=['get','post'])
def view_institute():
	data={}
	q="select * from institution"
	res=select(q)
	data['institute']=res
	return render_template('admin_viewinstitution.html',data=data)
 
@admin.route('/view_user',methods=['get','post'])
def view_user():
	data={}
	q="select * from user"
	res=select(q)
	data['user']=res
	return render_template('admin_viewuser.html',data=data)

@admin.route('/complaint',methods=['get','post'])
def complaint():
	data={}
	q="select * from complaint"
	res=select(q)
	data['comp']=res
	return render_template('admin_viewcomplaint.html',data=data)
@admin.route('/admin_sendreply',methods=['get','post'])
def sendreply():
	if 'submit' in request.form:
		replay=request.form['reply']
		id=request.args['id']
		q="update complaint set reply='%s' where complaint_id='%s'"%(replay,id)
		update(q)
		return redirect(url_for('admin.complaint'))
	return render_template('admin_sendreply.html')


 	