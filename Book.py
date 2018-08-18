from LiteModel import LiteModel
from LiteModel import BusinessKey


class Book (LiteModel):

    def __init__(self, key=None):
        self.table = 'book'
        self.columns = ['id', 'book_title', 'book_author', 'stack_id', 'position', 'reading_state']
        self.protectedColumns = ['id']
        LiteModel.__init__(self, key)


