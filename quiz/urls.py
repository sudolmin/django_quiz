from django.urls import path, include

from .views import QuizListView, CategoriesListView, \
    ViewQuizListByCategory, QuizUserProgressView, QuizMarkingList, \
    QuizMarkingDetail, QuizDetailView, QuizTake, AddQuizView

from multichoice import views as mcq_views
from true_false import views as tfq_views
from essay import views as esq_views

urlpatterns = [

    path('',
        view=QuizListView.as_view(),
        name='quiz_index'),

    path('add/mcq', mcq_views.mcq, name="mcq"),
    path('add/esq', esq_views.essay, name="esq"),
    path('add/tfq', tfq_views.tfq, name="tfq"),
    path('add/quiz', AddQuizView, name="add_quiz"),

    path('category/',
        view=CategoriesListView.as_view(),
        name='quiz_category_list_all'),

    path('category/<str:category_name>',
        view=ViewQuizListByCategory.as_view(),
        name='quiz_category_list_matching'),

    path('progress/',
        view=QuizUserProgressView.as_view(),
        name='quiz_progress'),

    path('marking/',
        view=QuizMarkingList.as_view(),
        name='quiz_marking'),

    path('marking/<int:pk>/',
        view=QuizMarkingDetail.as_view(),
        name='quiz_marking_detail'),

    #  passes variable 'quiz_name' to quiz_take view
    path('<slug:slug>/',
        view=QuizDetailView.as_view(),
        name='quiz_start_page'),

    path('<str:quiz_name>/take/',
        view=QuizTake.as_view(),
        name='quiz_question'),
]
