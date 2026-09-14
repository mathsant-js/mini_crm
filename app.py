def main():
    while True:
        print("\nMini CRM de leads")
        print("[1] - Adicionar Lead")
        print("[2] - Listar Leads")
        print("[0] - Sair do Programa")
        
        opt = input("\nDigite uma opção: ")
        
        if opt == "1":
            # Adicionar lead
            pass
        
        elif opt == "2":
            # Listar leads
            pass
        
        elif opt == "0":
            print("\nPrograma Encerrado!")
            break
        
        else:
            print("Opção Inválida!")

if __name__ == '__main__':
    main()