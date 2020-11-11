from app import app, db 
from flask import render_template, request, redirect, url_for

#Import for Forms
from app.forms import PhoneForm

#Import for Models
from app.models import User




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registerphone', methods=['GET', 'POST'])
def registerphone():

    form = PhoneForm()

    context = {
        'form': form 

    }

  
    
    if request.method == 'POST' and form.validate():
            #Get Information
        
        phonenumber = form.phonenumber.data
        username = form.username.data
       
        #Create new instance of User
        new_user = User(username, phonenumber)
        #Add user to db
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('registerphone.html', **context)

