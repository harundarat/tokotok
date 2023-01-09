import os
from flask import Flask,render_template,request,redirect,url_for,flash,session
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash,generate_password_hash
from werkzeug.utils import secure_filename

app = Flask (__name__)
app.secret_key = "projectakhir"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tokotok'
mysql = MySQL(app)

@app.route('/')
@app.route('/index')
def index():
    if 'loggedin' in session:
        flash('Hallo Selamat Datang Admin Silahkan Lengkapi Data Anda')
    return render_template('index.html')

@app.route('/loginadmin',methods=('GET','POST'))
def loginadmin():
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['password']

    # cek username 
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM admin WHERE username=%s And password=%s',(username,password,))
        akun = cursor.fetchone()
        if akun is None :
            flash('Login gagal, Silahkan cek Username / Password anda!!!')
        else:
            return redirect(url_for('admin'))
    return render_template('loginadmin.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/dataproduk', methods=['GET','POST'])
def dataproduk():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produk")
    produk = cur.fetchall()
    cur.close()
    return render_template('dataproduk.html',menu = 'master',submenu = 'barang',data=produk)

@app.route('/formproduk')
def formproduk():
    return render_template('formproduk.html',menu = 'master',submenu = 'barang')

@app.route('/saveproduk',methods=['GET','POST'])
def saveproduk():
    id_produk = request.form['idproduk']
    nama_produk = request.form['namaproduk']
    merek = request.form['merekproduk']
    stok_produk = request.form['stokproduk']
    harga = request.form['hargaproduk']
    deskripsi = request.form['deskripsiproduk']
    gambar = request.files['file']
    filename = secure_filename(gambar.filename)
    gambar.save(os.path.join('static/dist/img/produk', filename))
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO produk(id_produk,nama_produk,merek,stok_produk,harga,deskripsi) VALUES(%s,%s,%s,%s,%s,%s)',(id_produk,nama_produk,merek,stok_produk,harga,deskripsi))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dataproduk'))
    

@app.route('/hapusproduk', methods=['GET','POST'])
def hapusproduk():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM produk")
    produk = cur.fetchall()
    cur.close()
    return render_template('hapusproduk.html',menu = 'master',submenu = 'formproduk', data=produk )

@app.route('/hapus', methods=['GET','POST'])
def hapus():
    cur = mysql.connection.cursor()
    produk = cur.fetchall()
    cur.execute("DELETE FROM produk WHERE id_produk")
    mysql.connection.commit()
    return redirect('hapusproduk.html',data=produk )
    

@app.route('/datapengguna')
def datapengguna():
    return render_template('datapengguna.html',menu = 'master',submenu = 'pengguna')
    
@app.route('/datatransaksi')
def datatransaksi():
    return render_template('datatransaksi.html',menu = 'master',submenu = 'transaksi')

@app.route('/about')
def about():
    return render_template('about.html',menu = 'about',submenu = 'tentang')


#           HALAMAN USER       
@app.route('/loginuser',methods=['GET','POST'])
def loginuser():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

    # cek username 
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM pelanggan WHERE username=%s',(username,))
        akun = cursor.fetchone()
        if akun is None :
            flash('Login gagal, Silahkan cek Username / Password anda!!!')
        else:
            session['loggedin'] = True
            session['email'] = akun[2]
            session['alamat'] = akun[3]
            session['notelp'] = akun[4]
            return redirect(url_for('index'))
    return render_template('loginuser.html')
    
@app.route('/daftaruser', methods=['GET','POST'])
def daftaruser():
    if request.method=='POST':
        nama = request.form['nama']
        username = request.form['username']
        email = request.form['email']
        alamat = request.form['alamat']
        notelp = request.form['nomor']
        password = request.form['password']
        
        # cek username / email
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM pelanggan WHERE username=%s OR email=%s',(username,email,))
        akun = cursor.fetchone()
        if akun is None:
            cursor.execute('INSERT INTO pelanggan VALUES (%s,%s,%s,%s,%s,%s)',(nama,username,email,alamat,notelp,generate_password_hash(password)))
            mysql.connection.commit()
            flash('Daftar Telah Berhasil,Silahkan untuk Login')
        else :
            flash('Username atau email sudah ada')
    return render_template('daftaruser.html')
    
@app.route('/detailproduk')
def detailproduk():
    return render_template('detailproduk.html')

@app.route('/produk/apple/')    
def apple():
    return render_template("produk/apple.html", judul = "Beli Handphone Apple")

@app.route("/produk/oppo/")
def oppo():
    return render_template("produk/oppo.html", judul = "Beli Handphone Oppo")

@app.route("/produk/samsung/")
def samsung():
    return render_template("produk/samsung.html", judul = "Beli Handphone Samsung")

@app.route("/produk/vivo/")
def vivo():
    return render_template("produk/vivo.html", judul = "Beli Handphone Vivo")

@app.route("/produk/xiaomi/")
def xiaomi():
    return render_template("produk/xiaomi.html", judul = "Beli Handphone Xiaomi")






if __name__ == '__main__':
    app.run(debug=True)
