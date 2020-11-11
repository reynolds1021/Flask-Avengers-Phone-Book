from app import app, db 
from flask import render_template, request, redirect, url_for

#Import for Forms
from app.forms import PhoneForm

#Import for Models
from app.models import Phone




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
        first_name = form.first_name.data
        last_name = form.last_name.data
        hero_name = form.hero_name.data
        phone_number = form.phone_number.data
        address = form.address.data
        print(first_name, last_name, hero_name, phone_number, address)        
       
        #Create new instance of Phone
        #new_phone = Phone(first_name, last_name, hero_name, phone_number, address)
        #Add user to db
       # db.session.add(new_phone)
        #db.session.commit()

        return redirect(url_for('index'))
    return render_template('registerphone.html', **context)

