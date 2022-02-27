from app.extensions.database import BaseModelMixin, db
from app.models import genre


class track(db.Model, BaseModelMixin):
    __tablename__ = "Track"
    id = db.Column(name="GenreId", type_=db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(name="Name", type_=db.Unicode(120), nullable=False, unique=True)

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
