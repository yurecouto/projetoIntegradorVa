from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView
from .models import Aluno, Professor, Curso, Turma, DetalheCurso, DetalheTurma, Disciplina, DetalheDisciplina, NotasAluno, FaltasAluno
from .serializers import AlunoSerializer, ProfessorSerializer, CursoSerializer, TurmaSerializer, DetalheCursoSerializer, DetalheTurmaSerializer, DisciplinaSerializer, DetalheDisciplinaSerializer, NotasAlunoSerializer, FaltasAlunoSerializer

@api_view(['GET'])
def listar_turmas_professor(self, request, codigo_professor):
    detalhes_turma = DetalheTurma.objects.filter(codigo_professor=codigo_professor)
    serializer = DetalheTurmaSerializer(detalhes_turma, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def listar_alunos_turma(request, turma_id):
    detalhes_turma = DetalheTurma.objects.filter(id=turma_id)
    alunos_turma = [detalhe.codigo_aluno for detalhe in detalhes_turma]
    serializer = AlunoSerializer(alunos_turma, many=True)
    return Response(serializer.data)

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class DetalheCursoViewSet(viewsets.ModelViewSet):
    queryset = DetalheCurso.objects.all()
    serializer_class = DetalheCursoSerializer

class DetalheTurmaViewSet(viewsets.ModelViewSet):
    queryset = DetalheTurma.objects.all()
    serializer_class = DetalheTurmaSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class DisciplinaCreateView(CreateAPIView):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DetalheDisciplinaViewSet(viewsets.ModelViewSet):
    queryset =  DetalheDisciplina.objects.all()
    serializer_class =  DetalheDisciplinaSerializer

class NotasAlunoViewSet(viewsets.ModelViewSet):
    queryset =  NotasAluno.objects.all()
    serializer_class =  NotasAlunoSerializer

class FaltasAlunoViewSet(viewsets.ModelViewSet):
    queryset =  FaltasAluno.objects.all()
    serializer_class =  FaltasAlunoSerializer