
from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self._available = True

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, value):
        if value in [True, False]:
            self._available = value

    def displayDetails(self):
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)
        print("Status  :", "Available" if self.available else "Issued")

    def issueBook(self):
        if self.available:
            self.available = False
            return True
        return False

    def returnBook(self):
        self.available = True

    @abstractmethod
    def calculateFine(self, days):
        pass


class AcademicBook(Book):
    def calculateFine(self, days):
        return days * 2


class NovelBook(Book):
    def calculateFine(self, days):
        return days * 5


class Magazine(Book):
    def calculateFine(self, days):
        return days * 1


class Member:
    total_members = 0

    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.issued_books = []
        Member.total_members += 1

    def issueBook(self, book_id):
        self.issued_books.append(book_id)

    def returnBook(self, book_id):
        if book_id in self.issued_books:
            self.issued_books.remove(book_id)

    def displayMember(self):
        print("Member ID :", self.member_id)
        print("Name :", self.name)
        print("Issued Books :", self.issued_books)



class Library:
    total_books = 0

    def __init__(self):
        self.books = {}
        self.members = {}

    @staticmethod
    def validateBookID(book_id):
        return len(book_id) > 1 and book_id[0] == "B" and book_id[1:].isdigit()

    def addBook(self):
        bid = input("Book ID : ")
        if not Library.validateBookID(bid):
            print("Invalid Book ID")
            return
        title = input("Title : ")
        author = input("Author : ")

        print("1.Academic")
        print("2.Novel")
        print("3.Magazine")
        ch = input("Category : ")

        if ch == "1":
            book = AcademicBook(bid, title, author)
        elif ch == "2":
            book = NovelBook(bid, title, author)
        else:
            book = Magazine(bid, title, author)

        self.books[bid] = book
        Library.total_books += 1
        print("Book Added Successfully")

    def registerMember(self):
        mid = input("Member ID : ")
        name = input("Name : ")
        self.members[mid] = Member(mid, name)
        print("Member Registered Successfully")

    def displayBooks(self):
        for book in self.books.values():
            book.displayDetails()
            print("----------------")

    def displayMembers(self):
        for member in self.members.values():
            member.displayMember()
            print("----------------")

    def searchBook(self):
        bid = input("Enter Book ID : ")
        if bid in self.books:
            print("Book Found")
            self.books[bid].displayDetails()
        else:
            print("Book Not Found")

    def issueBook(self):
        mid = input("Member ID : ")
        bid = input("Book ID : ")

        if mid in self.members and bid in self.books:
            if self.books[bid].issueBook():
                self.members[mid].issueBook(bid)
                print("Book Issued Successfully")
            else:
                print("Book Already Issued")
        else:
            print("Invalid Member ID or Book ID")

    def returnBook(self):
        mid = input("Member ID : ")
        bid = input("Book ID : ")

        if mid in self.members and bid in self.books:
            days = int(input("Days Late : "))
            self.books[bid].returnBook()
            self.members[mid].returnBook(bid)
            fine = self.books[bid].calculateFine(days)
            print("Book Returned Successfully")
            print("Fine = ₹", fine)
        else:
            print("Invalid Member ID or Book ID")

    def libraryReport(self):
        issued = 0
        for book in self.books.values():
            if not book.available:
                issued += 1

        print("\n------ LIBRARY REPORT ------")
        print("Total Books :", Library.total_books)
        print("Issued Books :", issued)
        print("Available Books :", Library.total_books - issued)
        print("Total Members :", Member.total_members)


library = Library()

while True:
    print("\n===== LIBRARY MANAGEMENT =====")
    print("1. Add Book")
    print("2. Register Member")
    print("3. Display Books")
    print("4. Display Members")
    print("5. Issue Book")
    print("6. Return Book")
    print("7. Search Book")
    print("8. Library Report")
    print("9. Exit")

    choice = input("Enter Choice : ")

    if choice == "1":
        library.addBook()
    elif choice == "2":
        library.registerMember()
    elif choice == "3":
        library.displayBooks()
    elif choice == "4":
        library.displayMembers()
    elif choice == "5":
        library.issueBook()
    elif choice == "6":
        library.returnBook()
    elif choice == "7":
        library.searchBook()
    elif choice == "8":
        library.libraryReport()
    elif choice == "9":
        print("Thank You!")
        break
    else:
        print("Invalid Choice")