from Book import Book
from LiteModel import BusinessKey
'''
# simple key
bookBU = BusinessKey()
bookBU.addKeyValue('id', 1)


# compound key
bookBU2 = BusinessKey()
bookBU2.addKeyValue('book_title','IT')
bookBU2.addKeyValue('book_author','Stephen King')
book2 = Book(bookBU2)
book2.print()

print('')
print('')
'''

''' returns the book with given id, or None '''
'''
book = Book(bookBU)
book.print()



'''
'''creation cycle test OK'''
'''
book = Book()
book.entityValues['book_title'] = 'Nightmares And Dreamscapes'
book.entityValues['book_author'] = 'Stephen King'
book.entityValues['stack_id'] = 1
book.entityValues['position'] = 4
book.entityValues['reading_state'] = 2
book.save()
'''

'''search '''
bu = BusinessKey()
# bu.addKeyValue('book_title', 'Follia')
bu.addKeyValue('book_author', 'Patrick McGrath')
book = Book()
data = book.search(bu)
if data is not None:
    for d in data:
        d.print()
        print('')
else:
    print('nothing found!')







