import sqlite3

# Função para criar o banco de dados e a tabela de medicamentos
def create_database():
    conn = sqlite3.connect('medicamentos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicamentos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            dosagem TEXT NOT NULL,
            frequencia TEXT NOT NULL,
            observacoes TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

# Função para adicionar um medicamento
def add_medicamento(nome, dosagem, frequencia, observacoes=''):
    conn = sqlite3.connect('medicamentos.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO medicamentos (nome, dosagem, frequencia, observacoes)
        VALUES (?, ?, ?, ?)
    ''', (nome, dosagem, frequencia, observacoes))
    
    conn.commit()
    conn.close()

# Função para visualizar todos os medicamentos
def view_medicamentos():
    conn = sqlite3.connect('medicamentos.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM medicamentos')
    medicamentos = cursor.fetchall()
    
    conn.close()
    return medicamentos

# Função para atualizar um medicamento
def update_medicamento(id, nome=None, dosagem=None, frequencia=None, observacoes=None):
    conn = sqlite3.connect('medicamentos.db')
    cursor = conn.cursor()
    
    if nome:
        cursor.execute('UPDATE medicamentos SET nome = ? WHERE id = ?', (nome, id))
    if dosagem:
        cursor.execute('UPDATE medicamentos SET dosagem = ? WHERE id = ?', (dosagem, id))
    if frequencia:
        cursor.execute('UPDATE medicamentos SET frequencia = ? WHERE id = ?', (frequencia, id))
    if observacoes:
        cursor.execute('UPDATE medicamentos SET observacoes = ? WHERE id = ?', (observacoes, id))
    
    conn.commit()
    conn.close()

# Função principal para interagir com o usuário
def main():
    create_database()
    
    while True:
        print("\nSistema de Gestão de Medicamentos")
        print("1. Adicionar Medicamento")
        print("2. Visualizar Medicamentos")
        print("3. Atualizar Medicamento")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome do medicamento: ")
            dosagem = input("Dosagem: ")
            frequencia = input("Frequência: ")
            observacoes = input("Observações (opcional): ")
            add_medicamento(nome, dosagem, frequencia, observacoes)
            print("Medicamento adicionado com sucesso!")
        
        elif escolha == '2':
            medicamentos = view_medicamentos()
            for medicamento in medicamentos:
                print(f"ID: {medicamento[0]}, Nome: {medicamento[1]}, Dosagem: {medicamento[2]}, Frequência: {medicamento[3]}, Observações: {medicamento[4]}")
        
        elif escolha == '3':
            id = int(input("ID do medicamento a ser atualizado: "))
            print("Deixe em branco se não deseja atualizar um campo.")
            nome = input("Novo nome (deixe em branco para não alterar): ")
            dosagem = input("Nova dosagem (deixe em branco para não alterar): ")
            frequencia = input("Nova frequência (deixe em branco para não alterar): ")
            observacoes = input("Novas observações (deixe em branco para não alterar): ")
            update_medicamento(id, nome if nome else None, dosagem if dosagem else None, frequencia if frequencia else None, observacoes if observacoes else None)
            print("Medicamento atualizado com sucesso!")
        
        elif escolha == '4':
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
