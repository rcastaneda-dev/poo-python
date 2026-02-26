class BookStoreError(Exception):
    """ Base class for all exceptions in the bookstore"""
    pass

class InvalidTitleError(BookStoreError):
    """ Invalid title error"""
    pass

class BookNotAvailableError(BookStoreError):
    """ Book not available in the bookstore"""
    pass

class UserNotFoundError(BookStoreError):
    """ User not found in the bookstore"""
    pass

class BookNotFoundError(BookStoreError):
    """ Book not found in the bookstore"""
    pass
