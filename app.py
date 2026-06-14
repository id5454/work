from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="hellow"
@app.route('/')
def main():
    posts = cur.execute('SELECT * FROM ads').fetchall()
    return render_template('main.html', posts = posts)


@app.route('/login/')
def login():
    return render_template('login.html')


@app.route('/profile/')
def profile():
    user_email = session['email']
    user_role = cur.execute(f"SELECT role FROM users WHERE email = ?", [user_email]).fetchone()[0]
    return render_template('profile.html', user_role=user_role)





@app.route('/registar/', methods=['GET', 'POST'])
def registar():
    if request.method == 'POST':
        email = request.form.get('email') # input из html у которого id = email
        password = request.form.get('password')
        user = user = cur.execute(f"SELECT * FROM users WHERE email = '{email}'").fetchone()
        checkbox = request.form.get('checkbox')
        if user is None:
            if checkbox:
                cur.execute(f"INSERT INTO users(email, password, role) VALUES('{email}', '{password}','работник')")
            else: 
                cur.execute(f"INSERT INTO users(email, password, role) VALUES('{email}', '{password}','работадатель')")
            conn.commit()
            session['email'] = email 
            return redirect('/')
        else:
            print("Такой пользователь уже есть")
    return render_template('registar.html')




    @app.route('/login/', methods=['GET', 'POST'])
    def login():
     if request.method == 'POST':
        email = request.form.get('email') # input из html у которого id = email
        password = request.form.get('password')
        user = user = cur.execute(f"SELECT * FROM users WHERE email = '{email}'").fetchone()
        checkbox = request.form.get('checkbox')
        if user is None:
            if checkbox:
                cur.execute(f"INSERT INTO users(email, password) VALUES('{email}', '{password}')")
            else: 
                cur.execute(f"INSERT INTO users(email, password) VALUES('{email}', '{password}')")
            conn.commit()
            session['email'] = email 
            return redirect('/')       
    return render_template('login.html')






import sqlite3
conn = sqlite3.connect('USERS.db', check_same_thread=False)
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            password TEXT,
            date_of_brirth DATE,
            location TEXT,
            role TEXT,
            id_resume INTEGER,
            FOREIGN KEY (id_resume) REFERENCES resume(id)
            )
''')
conn.commit()



cur.execute('''
CREATE TABLE IF NOT EXISTS resume(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            surname TEXT,
            patronymic TEXT,
            date_of_brirth DATE,
            number_on_phone INTEGER,
            email TEXT,
            work_experience INTEGER,
            your_profession TEXT,
            photo TEXT,
            additional_ingormation TEXT
            )
''')
conn.commit()





cur.execute('''
CREATE TABLE IF NOT EXISTS ads(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT,  
            photo TEXT,
            id_employer INTEGER,
            heading TEXT,
            title_content TEXT,
            salary INTEGER,
            FOREIGN KEY (id_employer) REFERENCES users(id)
            )
''')
conn.commit()




if __name__ == '__main__':
    app.run()
