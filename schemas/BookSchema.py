from main import ma
from models.Book import Book
from schemas.UserSchema import UserSchema
from marshmallow.validate import Length

class BookSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Book

    title = ma.String(required=True, validate=Length(min=1))
    user = ma.Nested(UserSchema)
    
book_schema = BookSchema()
books_schema = BookSchema(many=True)