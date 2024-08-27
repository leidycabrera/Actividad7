from flask import render_template, request, redirect, url_for, flash, session
from app import app
from app.models.persona import Persona
from werkzeug.security import check_password_hash

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = Persona.find_by_username(username)

        if user and check_password_hash(user['password'], password):
            session['id_persona'] = user['idpersona']
            return redirect(url_for('index'))
        else:
            flash('Credenciales inválidas', 'danger')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('id_persona', None)
    flash('Se ha cerrado la sesión.', 'success')
    return redirect(url_for('login'))
