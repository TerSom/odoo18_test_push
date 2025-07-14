from odoo import models, fields,api
from odoo.exceptions import ValidationError
import re

class DataSiswa(models.Model):
    _name = "data.siswa"
    _description = "Data Siswa"

    nama = fields.Char(string='Nama', required=True)
    nis = fields.Integer(string='NIS', required=True)
    nisn = fields.Integer(string='NISN', required=True)
    email = fields.Char(string='email', required=True)
    tanggal_lahir = fields.Date(string='Tanggal Lahir', required=True)
    jenis_kelamin = fields.Selection(
        selection=[('l', 'Laki-laki'), ('p', 'Perempuan')],
        string='Jenis Kelamin',
        required=True
    )
    wali_kelas_id = fields.Many2one(
        comodel_name="data.guru",
        string="wali kelas"
    )
    
    _sql_constraints = [
        ('inique_nis','UNIQUE(nis)', 'kode unik')
    ]
    
    @api.constrains("email")
    def check_email(self):
        emailRegex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        for record in self:
            if record.email and not re.match(emailRegex,record.email):
                raise ValidationError("masukan email yang benar")
    
    _sql_constraints = [
        ('unique_email','UNIQUE(email)', 'email sudah ada') 
    ]
    
    @api.constrains("nama")
    def check_unique_nama(self):
        for record in self:
            exciting = self.env['data.siswa'].search([('nama','=',record.nama), ('id','!=', record.id)])
            if exciting:
                raise ValidationError("nama sudah ada")
        
            
    
    
    
class DataGuru(models.Model):
    _name="data.guru"
    _description = "Data Guru"
    
    nama = fields.Char(string='Nama', required=True)
    nip = fields.Integer(string='NIP', required=True)
    tanggal_lahir = fields.Date(string='Tanggal Lahir', required=True)
    jenis_kelamin = fields.Selection(
        selection=[('l', 'Laki-laki'), ('p', 'Perempuan')],
        string='Jenis Kelamin',
        required=True
    )

    murid_kelas_id = fields.One2many(
        comodel_name="data.siswa",
        inverse_name="wali_kelas_id",
        string="Daftar siswa"
    )


class Ekstrakulikuler(models.Model):
    _name ="exktrakulikuler.sekolah"
    _description="Extrakulikuler Sekolah"
    
    nama = fields.Char(string="Nama Extrakulikuler", required=True)
    umur = fields.Integer(string="Buat umur berapa", required=True)
    Peseta = fields.Integer(string="peserta", required=True)
    bayarMasuk = fields.Float(string="harga masuk ekstrakulikuler" , required=True)
    totalHarga = fields.Float(compute='_compute_totalHarga', store=True)
    active = fields.Boolean(default=True)
    siswa_ids = fields.Many2many(
        comodel_name="data.siswa",
        string="peserta"
    )
    
    @api.depends('bayarMasuk','Peseta')
    def _compute_totalHarga(self):
        for record in self:
            record.totalHarga = record.bayarMasuk * record.Peseta 
    
    @api.constrains("umur")
    def chek_umur(self):
        for record in self:
            if record.umur < 18:
                raise ValidationError("terlalu muda")
            elif record.umur > 20:
                raise ValidationError("terlalu tua")
    

   