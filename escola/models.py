from django.db import models

class Aluno(models.Model):
    class Meta:
        db_table = 'aluno'

    nome = models.CharField(max_length=200)
    sexo = models.CharField(max_length=200)
    matricula = models.CharField(max_length=200, unique=True)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.title


class Professor(models.Model):
    class Meta:
        db_table = 'professor'

    nome = models.CharField(max_length=100)
    sexo = models.CharField(max_length=1)
    registro = models.CharField(max_length=8, unique=True)


class Curso(models.Model):
    class Meta:
        db_table = 'curso'

    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=8, unique=True)


class Turma(models.Model):
    class Meta:
        db_table = 'turma'

    codigo = models.CharField(max_length=20, unique=True)
    codigo_curso = models.ForeignKey(Curso, to_field='codigo', on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo


class DetalheCurso(models.Model):
    class Meta:
        db_table = 'detalhecurso'

    codigo_curso = models.ForeignKey(Curso, to_field='id', on_delete=models.CASCADE)
    codigo_turma = models.ForeignKey(Turma, to_field='codigo', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.codigo_curso} - {self.codigo_turma}"


class DetalheTurma(models.Model):
    class Meta:
        db_table = 'detalhe_turma'

    codigo_aluno = models.ForeignKey(Aluno, to_field='matricula', on_delete=models.CASCADE)
    codigo_professor = models.ForeignKey(Professor, to_field='registro', on_delete=models.CASCADE)
    codigo_turma = models.ForeignKey(Turma, to_field='codigo', on_delete=models.CASCADE)


class Disciplina(models.Model):
    class Meta:
        db_table = 'disciplina'

    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=8)


class DetalheDisciplina(models.Model):
    class Meta:
        db_table = 'detalhedisciplina'

    codigo_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    codigo_disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.codigo_curso} - {self.codigo_disciplina}"


class NotasAluno(models.Model):
    class Meta:
        db_table = 'notasaluno'

    codigo_aluno = models.ForeignKey(Aluno, to_field='matricula', on_delete=models.CASCADE)
    nota = models.IntegerField()
    disciplina = models.ForeignKey(Disciplina, to_field='id', on_delete=models.CASCADE)
    avaliacao = models.CharField(max_length=4)
    data = models.DateField()


class FaltasAluno(models.Model):
    class Meta:
        db_table = 'faltasaluno'

    codigo_aluno = models.ForeignKey(Aluno, to_field='matricula', on_delete=models.CASCADE)
    codigo_professor = models.ForeignKey(Professor, to_field='registro', on_delete=models.CASCADE)
    codigo_turma = models.ForeignKey(Turma, to_field='codigo', on_delete=models.CASCADE)
    data = models.DateField()

