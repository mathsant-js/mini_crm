from stages import model_lead
import repo

def add_lead():
    name = input("Nome: ")
    email = input("Email: ")
    status = input("Etapa no funil de vendas: ")
    
    print(model_lead(name, email, status))
    
    repo.create_leads(model_lead(name, email, status))
    
    print("Lead adicionado (func)")
    
def list_leads():
    leads = repo.read_leads()
    
    print(f"## | {"Nome":<15} | E-mail")

    for i, lead in enumerate(leads):
        print(f"{i:02d} | {lead["name"]:<15} | {lead["email"]}")

def search_leads():
    query = input("Buscar por: ").strip().lower()

    # CONTROL!!
    # comparação entre a query digitada e o leads.json
    search_results = repo.read_leads_search(query)

    print(f"## | {"Nome":<15} | E-mail")

    for i, lead in search_results:
        print(f"{i:02d} | {lead["name"]:<15} | {lead["email"]}")

def export_leads():
    path_csv = repo.export_csv()

    if path_csv is None:
        print("Não foi possível exportar para CSV")
    else:
        print(f"Exportado para {path_csv}")

def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] - Adicionar Lead")
        print("[2] - Listar Leads")
        print("[3] - Buscar (nome/e-mail)")
        print("[4] - Exportar para CSV")
        print("[0] - Sair do Programa")
        
        opt = input("\nDigite uma opção: ")
        
        if opt == "1":
            add_lead()
        
        elif opt == "2":
            list_leads()
        
        elif opt == "3":
            search_leads()

        elif opt == "4":
            export_leads()

        elif opt == "0":
            print("\nPrograma Encerrado!")
            break
        
        else:
            print("Opção Inválida!")

if __name__ == '__main__':
    main()