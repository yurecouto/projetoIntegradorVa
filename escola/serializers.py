from rest_framework import serializers
from .models import Aluno, Professor, Curso, Turma, DetalheCurso, DetalheTurma, Disciplina, DetalheDisciplina, NotasAluno, FaltasAluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class TurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class DetalheCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheCurso
        fields = '__all__'

class DetalheTurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheTurma
        fields = '__all__'

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class DetalheDisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalheDisciplina
        fields = '__all__'

class NotasAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotasAluno
        fields = '__all__'

class FaltasAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaltasAluno
        fields = '__all__'