# api_python

http://127.0.0.1:5000/professores
{
    "nome": "Marcos",
    "idade": 25,
    "materia": "História",
    "observacoes": "banana"
}


http://127.0.0.1:5000/turmas
{
    "descricao": "Truma do professro Marcos",
    "ativo": true,
    "professor_id": 1
}   


http://127.0.0.1:5000/alunos
{
    "nome": "Bruno",
    "idade": 16,
    "data_nascimento": "2008-03-12",
    "nota_primeiro_semestre": 7.0,
    "nota_segundo_semestre": 8.0,
    "media_final": 7.5,
    "turma_id": 1
}


http://127.0.0.1:5000/atividades
{
    "id_disciplina": 2,
    "enunciado": "Explique a Revolução Francesa",
    "respostas": [{"id_aluno": 1, "resposta": "Resposta exemplo", "nota": 8}]
}
