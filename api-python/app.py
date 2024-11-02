from flask import Flask, request, jsonify
from config import app, db
from models import Professor, Turma, Aluno

@app.route('/professores', methods=['POST'])
def create_professor():
    data = request.get_json()
    professor = Professor(
        nome=data['nome'],
        idade=data['idade'],
        materia=data['materia'],
        observacoes=data.get('observacoes', '')
    )
    db.session.add(professor)
    db.session.commit()
    return jsonify({"message": "Professor criado com sucesso"}), 201

@app.route('/turmas', methods=['POST'])
def create_turma():
    data = request.get_json()
    turma = Turma(
        descricao=data['descricao'],
        ativo=data.get('ativo', True),
        professor_id=data['professor_id']
    )
    db.session.add(turma)
    db.session.commit()
    return jsonify({"message": "Turma criada com sucesso"}), 201

@app.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.get_json()
    aluno = Aluno(
        nome=data['nome'],
        idade=data['idade'],
        data_nascimento=data['data_nascimento'],
        nota_primeiro_semestre=data['nota_primeiro_semestre'],
        nota_segundo_semestre=data['nota_segundo_semestre'],
        media_final=(data['nota_primeiro_semestre'] + data['nota_segundo_semestre']) / 2,
        turma_id=data['turma_id']
    )
    db.session.add(aluno)
    db.session.commit()
    return jsonify({"message": "Aluno criado com sucesso"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
