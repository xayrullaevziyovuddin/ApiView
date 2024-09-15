from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Faculty, Group, Kafedra, Subject, Teacher, Student
from .serializers import FacultySerializer, GroupSerializer, KafedraSerializer, SubjectSerializer, TeacherSerializer, \
    StudentSerializer


class StudentListCreateAPIView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacultyListCreateAPIView(APIView):
    def get(self, request):
        faculties = Faculty.objects.all()
        serializer = FacultySerializer(faculties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FacultyDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Faculty.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            return None

    def get(self, request, pk):
        faculty = self.get_object(pk)
        if faculty is not None:
            serializer = FacultySerializer(faculty)
            return Response(serializer.data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        faculty = self.get_object(pk)
        if faculty is not None:
            serializer = FacultySerializer(faculty, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        faculty = self.get_object(pk)
        if faculty is not None:
            faculty.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)




class GroupListCreateAPIView(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            return None

    def get(self, request, pk):
        group = self.get_object(pk)
        if group is not None:
            serializer = GroupSerializer(group)
            return Response(serializer.data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        group = self.get_object(pk)
        if group is not None:
            serializer = GroupSerializer(group, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        group = self.get_object(pk)
        if group is not None:
            group.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)



class KafedraListCreateAPIView(APIView):
    def get(self, request):
        kafedras = Kafedra.objects.all()
        serializer = KafedraSerializer(kafedras, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KafedraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KafedraDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Kafedra.objects.get(pk=pk)
        except Kafedra.DoesNotExist:
            return None

    def get(self, request, pk):
        kafedra = self.get_object(pk)
        if kafedra is not None:
            serializer = KafedraSerializer(kafedra)
            return Response(serializer.data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        kafedra = self.get_object(pk)
        if kafedra is not None:
            serializer = KafedraSerializer(kafedra, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        kafedra = self.get_object(pk)
        if kafedra is not None:
            kafedra.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


class SubjectListCreateAPIView(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            return None

    def get(self, request, pk):
        subject = self.get_object(pk)
        if subject is not None:
            serializer = SubjectSerializer(subject)
            return Response(serializer.data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        subject = self.get_object(pk)
        if subject is not None:
            serializer = SubjectSerializer(subject, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        subject = self.get_object(pk)
        if subject is not None:
            subject.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


class TeacherListCreateAPIView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            return None

    def get(self, request, pk):
        teacher = self.get_object(pk)
        if teacher is not None:
            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        teacher = self.get_object(pk)
        if teacher is not None:
            serializer = TeacherSerializer(teacher, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        teacher = self.get_object(pk)
        if teacher is not None:
            teacher.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)



class StudentDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return None

    def get(self, request, pk):
        student = self.get_object(pk)
        if student is not None:
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        student = self.get_object(pk)
        if student is not None:
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        student = self.get_object(pk)
        if student is not None:
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
