from app.extensions.schema import ma
from app.models.albums import Track


class AlbumSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Track

    id = ma.auto_field(dump_only=True)
