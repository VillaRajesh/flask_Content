from flask import Flask,redirect,url_for,render_template,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from project_database import Register,Base

engine=create_engine('sqlite:///bvc.db',connect_args={'check_same_thread':False},echo=True)
Base.metadata.bind=engine

DBSession=sessionmaker(bind=engine)
session=DBSession()





app = Flask('__name__') 

@app.route("/home")
def hello():
	return "<h1>RAJESH.</h1> "



@app.route("/about")
def about():
	return "<h1>about page</h1>"



@app.route("/data/<name>/<number>")
def data(name,number):
	name="sai prasad"
	number="580"
	return "<h1>my name is : {} and<p>my number is: {} </p></h1>".format(name,number)



@app.route("/bio/<name>/<number>/<no>")
def bio(name,number,no):
	name="Rajesh"
	number="5B3"
	no="9381393834"
	return"My name is: <font color='red'>{}<p><font color='black'>and my roll number is : <font color='blue'>{}</p><p><font color='black'>my mobile no is: <font color='pink'>{}</p>".format(name,number,no)



@app.route("/admin")
def admin():
	return render_template("sample.html")


@app.route("/student")
def student():
	return "<font color='pink'>hello to welcome student page"


@app.route("/faculty")
def faculty():
	return "Welcome to faculty data"




@app.route("/person/<uname>")
def person(unname):
	return render_template("sample1.html",name=uname)




@app.route("/user/<name>")
def user(name):
	if name=='sir':
		return redirect(url_for('sir'))
	elif name=='student':
		return redirect(url_for('student'))
	elif name=='admin':
		return redirect(url_for('admin'))
	else:
		return'search another url'


dummy_data=[{'name':'prasad','org':'Bvc','DOB':'28 jun 2000'},{'name':'rajesh','org':'BVCE','DOB':'20 jun 2000'}]
@app.route("/show")
def data_show():
	return render_template("show_data.html",d=dummy_data)





@app.route("/sir")
def sir():
	return "hi this is python sir"

@app.route("/table/<int:num>")
def table(num):
	return render_template("table.html",n=num)

@app.route("/factor/<int:num>")
def factor(num):
	fact=1
	return render_template("sample2.html",fact)

@app.route("/register")
def reg():
	return render_template('register.html')






@app.route("/file")
def file_upload():
	return render_template("file_upload.html")




@app.route("/success",methods=["POST"])
def success():
	if request.method=='POST':
		f = request.files["files"]
		f.save(f.filename)
		return render_template("display.html",name=f.filename)


@app.route("/show_data")
def showData():
	register=session.query(Register).all()
	return render_template('show.html',register=register)



@app.route("/add",methods=["POST","GET"])
def addData():
	if request.method=='POST':
		newData=Register(name=request.form['name'],surname=request.form['surname'],roll_no=request.form['roll_no'],mobile=request.form['mobile'],branch=request.form['branch'])
		session.add(newData)
		session.commit()
		return redirect(url_for('showData'))
	else:
			return render_template('new.html')




@app.route("/<int:register_id>/edit",methods=["POST","GET"])
def editData(register_id):
	editedData=session.query(Register).filter_by(id=register_id).one()
	if request.method=="POST":
		editedData.name=request.form['name']
		editedData.surname=request.form['surname']
		editedData.roll_no=request.form['roll_no']
		editedData.mobile=request.form['mobile']
		editedData.branch=request.form['branch']

		session.add(editedData)
		session.commit()
		return redirect(url_for('showData'))
	else:
		return render_template('edit.html',register=editedData)

@app.route("/<int:register_id>/delete",methods=["POST","GET"])
def deleteData(register_id):
	deletedData=session.query(Register).filter_by(id=register_id).one()


	if request.method=="POST":
		session.delete(deletedData)
		session.commit()
		return redirect(url_for('showData',register_id=register_id))

	else:
		return render_template('delete.html',register=deletedData)




















if __name__=='__main__':
	app.run(debug=True)


