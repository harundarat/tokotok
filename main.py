from flask import Flask,render_template,request,redirect,url_for,flash,session
from flask_mysqldb import MySQL
from werkzeug.security import check_password_hash,generate_password_hash

app = Flask (__name__)
app.secret_key = "projectakhir"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'tokotok'
mysql = MySQL(app)

@app.route('/')
def index():
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
    gambar = request.form['gambarproduk']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO produk(id_produk,nama_produk,merek,stok_produk,harga,deskripsi,gambar) VALUES(%s,%s,%s,%s,%s,%s,%s)',(id_produk,nama_produk,merek,stok_produk,harga,deskripsi,gambar))
    mysql.connection.commit()
    cur.close()
    return redirect(url_for('dataproduk'))
    

@app.route('/hapusproduk', methods=['GET','POST'])
def hapusproduk():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM produk WHERE id_produk=%s")
    produk = cur.fetchall()
    cur.close()
    return render_template('hapusproduk.html',menu = 'master',submenu = 'formproduk', hapus=produk)

@app.route('/datapengguna')
def datapengguna():
    return render_template('datapengguna.html',menu = 'master',submenu = 'pengguna')
    
@app.route('/datatransaksi')
def datatransaksi():
    return render_template('datatransaksi.html',menu = 'master',submenu = 'transaksi')

@app.route('/about')
def about():
    return render_template('about.html',menu = 'about',submenu = 'tentang')


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
