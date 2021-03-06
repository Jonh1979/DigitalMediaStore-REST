from app.extensions.database import BaseModelMixin, db
<<<<<<< HEAD
from app.models import track
=======
>>>>>>> 57f56e3d5f7d52559a4c03941eaa61180cf49c01


class Track(db.Model, BaseModelMixin):
    __tablename__ = "Track"

    id = db.Column(name="TrackId", type_=db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(name="Name", type_=db.Unicode(200), nullable=False)
    media_type_id = db.Column(name="MediaTypeId", type_=db.Integer, nullable=False, default=1)
    name = db.Column(name="Composer", type_=db.Unicode(220), nullable=False)
    id = db.Column(name="Miliseconds", type_=db.Integer, nullable=False)
    id = db.Column(name="Bytes", type_=db.Integer, default=None)
    unit_price = db.Column(name="UnitPrice", type_=db.Numeric(10, 2))

    def __repr__(self):
        return f"<Tracks {self.name}>"

    def __str__(self):
        return self.name

    # def save(self):
    #     BaseModelMixin.save(self)
    #     self.id

    @classmethod
    def find_track_by_name(cls, name):
        return cls.simple_filter(name=name).first()
