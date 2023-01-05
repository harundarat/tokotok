-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 05 Jan 2023 pada 12.45
-- Versi server: 10.4.25-MariaDB
-- Versi PHP: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tokotok`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('admin', 'admin');

-- --------------------------------------------------------

--
-- Struktur dari tabel `pelanggan`
--

CREATE TABLE `pelanggan` (
  `nama` varchar(50) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `alamat` varchar(50) NOT NULL,
  `notelp` int(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `produk`
--

CREATE TABLE `produk` (
  `id_produk` int(50) NOT NULL,
  `nama_produk` varchar(100) NOT NULL,
  `merek` varchar(100) NOT NULL,
  `stok_produk` int(50) NOT NULL,
  `harga` int(100) NOT NULL,
  `deskripsi` text NOT NULL,
  `gambar` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- Kesalahan membaca data untuk tabel tokotok.produk: #2006 - MySQL server has gone away
<div class="alert alert-danger" role="alert"><h1>Galat</h1><p><strong>Query SQL:</strong>  <a href="#" class="copyQueryBtn" data-text="SET SQL_QUOTE_SHOW_CREATE = 1">Salin</a>
<a href="index.php?route=/database/sql&sql_query=SET+SQL_QUOTE_SHOW_CREATE+%3D+1&show_query=1&db=tokotok"><span class="text-nowrap"><img src="themes/dot.gif" title="Ubah" alt="Ubah" class="icon ic_b_edit">&nbsp;Ubah</span></a>    </p>
<p>
<code class="sql"><pre>
SET SQL_QUOTE_SHOW_CREATE = 1
</pre></code>
</p>
<p>
    <strong>MySQL menyatakan: </strong><a href="./url.php?url=https%3A%2F%2Fdev.mysql.com%2Fdoc%2Frefman%2F8.0%2Fen%2Fserver-error-reference.html" target="mysql_doc"><img src="themes/dot.gif" title="Dokumentasi" alt="Dokumentasi" class="icon ic_b_help"></a>
</p>
<code>#2006 - MySQL server has gone away</code><br></div>