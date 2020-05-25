from app import db


class Curedb(db.Model):
    __tablename__ = 'curedb'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),unique=True)
    description = db.Column(db.String(100))
    a = db.Column(db.Float())
    b = db.Column(db.Float())
    

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                        nullable=False)

    def __repr__(self):
        return '<Id: {}, name: {}>'.format(self.id, self.name)
