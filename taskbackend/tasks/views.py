from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Task
from .serializers import TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
import openpyxl

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def export(self, request):
        tasks = self.get_queryset()
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['Title', 'Description', 'Effort Days', 'Due Date'])

        for task in tasks:
            ws.append([task.title, task.description, task.effort_days, task.due_date])

        response = HttpResponse(
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=tasks.xlsx'
        wb.save(response)
        return response
