from jogoteca import db

# Classe jogos
class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)
    
    # __repr__ -> Mostra uma versão em string para a pessoa programadora
    # quando a classe é acessada em modo interativo
    def __repr__(self):
        return '<Name %r>' % self.name

# Classe usuários
class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    
    # __repr__ -> Mostra uma versão em string para a pessoa programadora
    # quando a classe é acessada em modo interativo
    def __repr__(self):
        return '<Name %r>' % self.name