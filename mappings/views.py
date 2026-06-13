from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import PatientDoctorMapping
from .serializers import MappingSerializer, MappingDetailSerializer
from patients.models import Patient

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def mapping_list_create(request):
    if request.method == 'GET':
        mappings = PatientDoctorMapping.objects.all()
        serializer = MappingDetailSerializer(mappings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            mapping = PatientDoctorMapping.objects.get(pk=serializer.data['id'])
            detail_serializer = MappingDetailSerializer(mapping)
            return Response(detail_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@permission_classes([IsAuthenticated])
def mapping_detail(request, pk):
    if request.method == 'GET':
        # GET /api/mappings/<patient_id>/ - Get all doctors assigned to a specific patient.
        try:
            patient = Patient.objects.get(pk=pk)
        except Patient.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        mappings = PatientDoctorMapping.objects.filter(patient=patient)
        serializer = MappingDetailSerializer(mappings, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        # DELETE /api/mappings/<id>/ - Remove a doctor from a patient.
        try:
            mapping = PatientDoctorMapping.objects.get(pk=pk)
        except PatientDoctorMapping.DoesNotExist:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
