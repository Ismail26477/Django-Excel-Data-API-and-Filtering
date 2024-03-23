import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ExcelDataSerializer
from django.shortcuts import render
from .models import ExcelData

@api_view(['GET'])
def get_excel_data(request):
    try:
        excel_file = 'C:\DjangoProject\Excel_API\excel_api\path_to_your_excel_file.xlsx'
        df = pd.read_excel(excel_file, engine='openpyxl')
        
        for index, row in df.iterrows():
            name = row['name']
            age = row['age']
            
            # Check if a record with the same name and age already exists in the database
            if not ExcelData.objects.filter(name=name, age=age).exists():
                serializer = ExcelDataSerializer(data={'name': name, 'age': age})
                if serializer.is_valid():
                    serializer.save()
                else:
                    return Response({
                        'error': 'Invalid data',
                        'details': serializer.errors
                    }, status=400)
        
        return Response({'message': 'Excel data imported successfully'})
    
    except Exception as e:
        return Response({
            'error': 'An error occurred',
            'details': str(e)
        }, status=500)

def display_excel_data(request):
    age_filter = request.GET.get('age', None)
    excel_data = ExcelData.objects.all()
    
    if age_filter:
        excel_data = excel_data.filter(age=age_filter)
    return render(request, 'index.html', {'excel_data': excel_data})

