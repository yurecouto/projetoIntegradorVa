from django.contrib import admin
from .models import Aluno, Professor, Curso, Turma, DetalheCurso, DetalheTurma, Disciplina, DetalheDisciplina

admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(DetalheCurso)
admin.site.register(DetalheTurma)
admin.site.register(Disciplina)
admin.site.register(DetalheDisciplina)