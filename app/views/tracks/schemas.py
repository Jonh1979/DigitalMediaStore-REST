from app.extensions.schema import ma
from app.models.albums import tracks


class AlbumSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = tracks

    id = ma.auto_field(dump_only=True)
