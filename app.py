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
    print(leads)

def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] - Adicionar Lead")
        print("[2] - Listar Leads")
        print("[0] - Sair do Programa")
        
        opt = input("\nDigite uma opção: ")
        
        if opt == "1":
            add_lead()
            pass
        
        elif opt == "2":
            list_leads()
            pass
        
        elif opt == "0":
            print("\nPrograma Encerrado!")
            break
        
        else:
            print("Opção Inválida!")

if __name__ == '__main__':
    main()