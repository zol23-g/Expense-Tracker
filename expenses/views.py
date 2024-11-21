from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Sum
from .models import Expense
from .serializers import ExpenseSerializer
from datetime import datetime

# Create your views here.

from rest_framework import generics
from .models import Expense
from .serializers import ExpenseSerializer

class ExpenseListCreate(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer



# views for listing expenses by date range and category summary

class ExpenseByDateRange(APIView):
    def get(self, request, user_id, start_date, end_date):
        expenses = Expense.objects.filter(user_id=user_id, date__range=[start_date, end_date])
        serializer = ExpenseSerializer(expenses, many=True)
        return Response(serializer.data)

class CategorySummary(APIView):
    def get(self, request, user_id, year, month):
        expenses = Expense.objects.filter(user_id=user_id, date__year=year, date__month=month)
        summary = expenses.values('category').annotate(total=Sum('amount'))
        return Response(summary)