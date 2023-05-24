from django.urls import path, include
from rest_framework import routers
from .views import listar_alunos_turma, listar_turmas_professor, AlunoViewSet, ProfessorViewSet, CursoViewSet, TurmaViewSet, DetalheCursoViewSet, DetalheTurmaViewSet, DisciplinaViewSet, DetalheDisciplinaViewSet, DisciplinaCreateView, NotasAlunoViewSet, FaltasAlunoViewSet

router = routers.DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'turmas', TurmaViewSet)
router.register(r'disciplinas', DisciplinaViewSet)

router.register(r'faltasaluno', FaltasAlunoViewSet)
router.register(r'notasaluno', NotasAlunoViewSet)
router.register(r'detalhecurso', DetalheCursoViewSet)
router.register(r'detalhedisciplina', DetalheDisciplinaViewSet)
router.register(r'detalheturma', DetalheTurmaViewSet)

urlpatterns = [
    path('turmas/<int:turma_id>/alunos/', listar_alunos_turma, name='listar_alunos_turma'),
    path('professor/<int:codigo_professor>/turmas/', listar_turmas_professor, name='listar_turmas_professor'),
    path('', include(router.urls)),
]