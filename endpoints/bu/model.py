from app import db


class BU(db.Model):
    __tablename__ = 'bu'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20),unique=True)
    description = db.Column(db.String(100))


    def __repr__(self):
        return 'Id: {}, name: {}'.format(self.id, self.name)
