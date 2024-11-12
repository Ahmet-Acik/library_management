# library_management/borrowable.py

from abc import ABC, abstractmethod


class Borrowable(ABC):
    @abstractmethod
    def borrow_book(self, library, title, is_account_active):
        pass

    @abstractmethod
    def return_book(self, library, title):
        pass
