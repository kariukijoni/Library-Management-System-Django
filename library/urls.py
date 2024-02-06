from django.urls import path

from .views import (
    AddBookView,
    AddMemberView,
    BooksListView,
    DeleteBookView,
    DeleteBorrowedBookView,
    DeleteMemberView,
    HomeView,
    IssueBookView,
    IssuedBooksListView,
    IssueMemberBookView,
    MembersListView,
    ReturnBookFineView,
    ReturnBookView,
    UpdateBookDetailsView,
    UpdateBorrowedBookView,
    UpdateMemberDetailsView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("add-member/", AddMemberView.as_view(), name="add-member"),
    path("members/", MembersListView.as_view(), name="members"),
    path("edit-member-details/<str:pk>/", UpdateMemberDetailsView.as_view(), name="update-member"),
    path("delete-member/<str:pk>/", DeleteMemberView.as_view(), name="delete-member"),
    path("add-book/", AddBookView.as_view(), name="add-book"),
    path("books/", BooksListView.as_view(), name="books"),
    path("edit-book-details/<str:pk>/", UpdateBookDetailsView.as_view(), name="update-book"),
    path("delete-book/<str:pk>/", DeleteBookView.as_view(), name="delete-book"),
    path("issue-book/", IssueBookView.as_view(), name="issue-book"),
    path("issue-book/<str:pk>/", IssueMemberBookView.as_view(), name="issue-member-book"),
    path("issued-books/", IssuedBooksListView.as_view(), name="issued-books"),
    path("edit-borrowed-book/<str:pk>/", UpdateBorrowedBookView.as_view(), name="edit-borrowed-book"),
    path("delete-borrowed-book/<str:pk>/", DeleteBorrowedBookView.as_view(), name="delete-borrowed-book"),
    path("return-book/<str:pk>/", ReturnBookView.as_view(), name="return-book"),
    path("return-book-fine/<str:pk>/", ReturnBookFineView.as_view(), name="return-book-fine"),
]
