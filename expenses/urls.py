from django.urls import path
from .views import ExpenseListCreate, ExpenseDetail, ExpenseByDateRange, CategorySummary

urlpatterns = [
    path('v1/expenses/', ExpenseListCreate.as_view(), name='expense-list-create'),
    path('v1/expenses/<int:pk>/', ExpenseDetail.as_view(), name='expense-detail'),
    path('v1/expenses/user/<int:user_id>/date-range/<str:start_date>/<str:end_date>/', ExpenseByDateRange.as_view(), name='expense-by-date-range'),
    path('v1/expenses/user/<int:user_id>/summary/<int:year>/<int:month>/', CategorySummary.as_view(), name='category-summary'),
]