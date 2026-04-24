# Exercício 1 — Contador de Vogais e Consoantes #

def exercicio_01():
    print("\n" + "="*50)
    print("Exercício 1 — Contador de Vogais e Consoantes")
    print("="*50)

    testes = [
        "Python para Seguranca",
        "Hello World 123!",
        "aeiou",
        "",
    ]

    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

    for frase in testes:
        total_vogais = 0
        total_consoantes = 0

        for char in frase:
            if char in vogais:
                total_vogais += 1
            elif char in consoantes:
                total_consoantes += 1

        print(f'\nFrase: "{frase}"')
        print(f"Vogais: {total_vogais}")
        print(f"Consoantes: {total_consoantes}")


# Exercício 2 — Validador de Senha com Regras #

def exercicio_02():
    print("\n" + "="*50)
    print("Exercício 2 — Validador de Senha com Regras")
    print("="*50)

    testes = [
        "abc",
        "abcdefgh",
        "Abcdefgh",
        "Abcdefg1",
        "Cyber@2024",
    ]

    especiais = "!@#$%&*"

    for senha in testes:
        print(f"\nTestando senha: '{senha}'")

        while True:
            problemas = []

            if len(senha) < 8:
                problemas.append("Falta mínimo de 8 caracteres")
            if not any(c.isupper() for c in senha):
                problemas.append("Falta pelo menos 1 letra maiúscula")
            if not any(c.islower() for c in senha):
                problemas.append("Falta pelo menos 1 letra minúscula")
            if not any(c.isdigit() for c in senha):
                problemas.append("Falta pelo menos 1 número")
            if not any(c in especiais for c in senha):
                problemas.append(f"Falta pelo menos 1 caractere especial ({especiais})")

            if not problemas:
                print("Senha válida!")
                break
            else:
                print("Senha inválida! Problemas encontrados:")
                for p in problemas:
                    print(f"  - {p}")
                break  


# Exercício 3 — Gerenciador de Lista de IPs #

def exercicio_03():
    print("\n" + "="*50)
    print("Exercício 3 — Gerenciador de Lista de IPs")
    print("="*50)

    ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3"]

    acoes = [
        ("adicionar", "192.168.1.10"),
        ("adicionar", "10.0.0.5"),
        ("buscar",    "172.16.0.3"),
        ("buscar",    "8.8.8.8"),
        ("remover",   "10.0.0.5"),
        ("listar",    None),
        ("sair",      None),
    ]

    for acao, valor in acoes:
        if acao == "sair":
            print("\nEncerrando...")
            break

        elif acao == "listar":
            print("\n Lista de IPs:")
            for i, ip in enumerate(ips, 1):
                print(f"  {i}. {ip}")

        elif acao == "adicionar":
            if valor in ips:
                print(f"\n  IP já existe na lista: {valor}")
            else:
                ips.append(valor)
                print(f"\n IP adicionado: {valor}")

        elif acao == "remover":
            if valor in ips:
                ips.remove(valor)
                print(f"\n  IP removido: {valor}")
            else:
                print(f"\n IP não encontrado: {valor}")

        elif acao == "buscar":
            if valor in ips:
                pos = ips.index(valor) + 1
                print(f"\n IP encontrado na posição {pos}: {valor}")
            else:
                print(f"\n IP não encontrado: {valor}")


# Exercício 4 — Análise de Notas com Tuplas #

def exercicio_04():
    print("\n" + "="*50)
    print("Exercício 4 — Análise de Notas com Tuplas")
    print("="*50)

    alunos = [
        ("Carlos",  8.5),
        ("Ana",     9.2),
        ("Bruno",   6.0),
        ("Diana",   7.8),
        ("Eduardo", 4.5),
    ]

    maior_nome, maior_nota = alunos[0]
    menor_nome, menor_nota = alunos[0]
    soma = 0.0

    for nome, nota in alunos:
        soma += nota
        if nota > maior_nota:
            maior_nota, maior_nome = nota, nome
        if nota < menor_nota:
            menor_nota, menor_nome = nota, nome

    media = soma / len(alunos)

    print("\n=== Relatório de Notas ===")
    print(f"Maior nota: {maior_nome} - {maior_nota}")
    print(f"Menor nota: {menor_nome} - {menor_nota}")
    print(f"Média da turma: {media:.1f}")
    print("\nAlunos acima da média:")
    for nome, nota in alunos:
        if nota > media:
            print(f"  - {nome}: {nota}")


# Exercício 5 — Contador de Palavras com Dicionário #

def exercicio_05():
    print("\n" + "="*50)
    print("Exercício 5 — Contador de Palavras com Dicionário")
    print("="*50)

    texto = "o gato viu o rato e o rato viu o gato e o gato correu"

    contagem = {}
    for palavra in texto.lower().split():
        contagem[palavra] = contagem.get(palavra, 0) + 1

    ordenado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    print("\n=== Contagem de Palavras ===")
    for palavra, qtd in ordenado:
        vez = "vez" if qtd == 1 else "vezes"
        print(f'  "{palavra}"{"":6} → {qtd} {vez}')

    mais_frequente, max_count = ordenado[0]
    print(f'\nPalavra mais frequente: "{mais_frequente}" ({max_count} vezes)')
    print(f"Total de palavras únicas: {len(contagem)}")


# Exercício 6 — Blacklist de IPs com Sets #


def exercicio_06():
    print("\n" + "="*50)
    print("Exercício 6 — Blacklist de IPs com Sets")
    print("="*50)

    acessos = {
        "192.168.1.10", "10.0.0.5", "185.220.101.1", "172.16.0.3",
        "192.168.1.20", "91.240.118.172", "10.0.0.12", "45.33.32.156"
    }

    blacklist = {
        "185.220.101.1", "45.33.32.156", "91.240.118.172",
        "23.94.5.100", "104.244.72.115"
    }

    maliciosos      = acessos & blacklist          # interseção
    seguros         = acessos - blacklist           # diferença
    nao_detectados  = blacklist - acessos           # diferença inversa
    todos           = acessos | blacklist           # união

    print("\n=== Relatório de Segurança ===")

    print(f"\n IPs maliciosos detectados ({len(maliciosos)}):")
    for ip in sorted(maliciosos):
        print(f"   - {ip}")

    print(f"\n IPs seguros ({len(seguros)}):")
    for ip in sorted(seguros):
        print(f"   - {ip}")

    print(f"\n IPs da blacklist não detectados ({len(nao_detectados)}):")
    for ip in sorted(nao_detectados):
        print(f"   - {ip}")

    print(f"\n Total de IPs únicos: {len(todos)}")


# Exercício 7 — Calculadora Segura com Exceções #

def exercicio_07():
    print("\n" + "="*50)
    print("Exercício 7 — Calculadora Segura com Exceções")
    print("="*50)

    operacoes_validas = {"+", "-", "*", "/"}

    sequencia = [
        ("abc", "0",  "/"),
        ("10",  "0",  "/"),
        ("10",  "3",  "/"),
        ("5",   "3",  "%"),
        ("sair","",   ""),
    ]

    for entrada1, entrada2, op in sequencia:
        print()
        try:
            if entrada1.lower() == "sair":
                print("Encerrando calculadora.")
                break

            num1 = float(entrada1)
            num2 = float(entrada2)

            if op not in operacoes_validas:
                raise ValueError(f"Operação '{op}' não suportada. Use +, -, * ou /")

            if op == "+":
                resultado = num1 + num2
            elif op == "-":
                resultado = num1 - num2
            elif op == "*":
                resultado = num1 * num2
            elif op == "/":
                resultado = num1 / num2

        except ValueError as e:
            if "not supported" in str(e) or "não suportada" in str(e):
                print(f"Erro: {e}")
            elif "could not convert" in str(e) or not entrada1.replace('.','',1).lstrip('-').isdigit():
                print("Erro: Digite apenas números!")
            else:
                print(f"Erro: {e}")
        except ZeroDivisionError:
            print("Erro: Divisão por zero!")
        else:
            print(f"Resultado: {resultado:.2f}")
        finally:
            print("Operação processada.")


# Exercício 8 — Inventário de Ativos com CRUD #

def exercicio_08():
    print("\n" + "="*50)
    print("Exercício 8 — Inventário de Ativos com CRUD")
    print("="*50)

    ativos = [
        {"nome": "SRV-WEB01", "tipo": "servidor", "ip": "192.168.1.10", "status": "ativo"},
        {"nome": "PC-RH03",   "tipo": "estacao",  "ip": "192.168.1.45", "status": "ativo"},
        {"nome": "SW-CORE01", "tipo": "switch",   "ip": "192.168.1.1",  "status": "inativo"},
    ]

    def buscar_por_ip(ip):
        for a in ativos:
            if a["ip"] == ip:
                return a
        return None

    # Simulação de sequência de teste
    acoes = [
        ("cadastrar", {"nome": "SRV-DB01", "tipo": "servidor", "ip": "192.168.1.20", "status": "ativo"}),
        ("cadastrar", {"nome": "DUPLICADO", "tipo": "servidor", "ip": "192.168.1.10", "status": "ativo"}),
        ("buscar",    "192.168.1.45"),
        ("buscar",    "8.8.8.8"),
        ("alterar",   ("192.168.1.1", "ativo")),
        ("remover",   "192.168.1.45"),
        ("listar",    None),
        ("sair",      None),
    ]

    for acao, dados in acoes:
        print()
        if acao == "sair":
            print("Encerrando sistema.")
            break

        elif acao == "cadastrar":
            if buscar_por_ip(dados["ip"]):
                print(f" Erro: IP já cadastrado! ({dados['ip']})")
            else:
                ativos.append(dados)
                print(f" Ativo '{dados['nome']}' cadastrado com sucesso!")

        elif acao == "listar":
            print(" Inventário de Ativos:")
            print(f"  {'NOME':<12} {'TIPO':<10} {'IP':<16} {'STATUS'}")
            print("  " + "-"*50)
            for a in ativos:
                print(f"  {a['nome']:<12} {a['tipo']:<10} {a['ip']:<16} {a['status']}")

        elif acao == "buscar":
            ativo = buscar_por_ip(dados)
            if ativo:
                print(f" Ativo encontrado:")
                for k, v in ativo.items():
                    print(f"   {k}: {v}")
            else:
                print(f" Ativo não encontrado: {dados}")

        elif acao == "alterar":
            ip, novo_status = dados
            ativo = buscar_por_ip(ip)
            if ativo:
                ativo["status"] = novo_status
                print(f" Status de '{ativo['nome']}' atualizado para '{novo_status}'")
            else:
                print(f" IP não encontrado: {ip}")

        elif acao == "remover":
            ativo = buscar_por_ip(dados)
            if ativo:
                ativos.remove(ativo)
                print(f"🗑️  Ativo '{ativo['nome']}' removido!")
            else:
                print(f" IP não encontrado: {dados}")


# Exercício 9 — Analisador de Logs de Segurança #

def exercicio_09():
    print("\n" + "="*50)
    print("Exercício 9 — Analisador de Logs de Segurança")
    print("="*50)

    logs = [
        "[2025-02-20 08:15:01] [INFO] Login ok - IP: 192.168.1.10",
        "[2025-02-20 08:15:03] [WARNING] Area restrita - IP: 10.0.0.5",
        "[2025-02-20 08:15:10] [ERROR] Falha auth - IP: 185.220.101.1",
        "[2025-02-20 08:15:15] [INFO] Arquivo acessado - IP: 192.168.1.10",
        "[2025-02-20 08:15:22] [ERROR] Conexao recusada - IP: 185.220.101.1",
        "[2025-02-20 08:15:30] [WARNING] Certificado SSL - IP: 172.16.0.3",
        "[2025-02-20 08:15:35] [ERROR] Falha auth - IP: 10.0.0.5",
        "log malformado sem formato correto",
        "[2025-02-20 08:15:45] [ERROR] Timeout - IP: 185.220.101.1",
        "[2025-02-20 08:15:50] [WARNING] CPU alta - IP: 192.168.1.20",
        "[2025-02-20 08:16:01] [ERROR] Falha auth - IP: 185.220.101.1",
        "[2025-02-20 08:16:05] [INFO] Firewall ok - IP: 192.168.1.10",
    ]

    contagem_nivel = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    erros_por_ip   = {}
    malformados    = 0

    for log in logs:
        try:
           
            nivel_inicio = log.index("[", log.index("]") + 1) + 1
            nivel_fim    = log.index("]", nivel_inicio)
            nivel        = log[nivel_inicio:nivel_fim]

            if nivel not in contagem_nivel:
                raise ValueError("Nível inválido")

            ip = log.split("IP: ")[1].strip()

            contagem_nivel[nivel] += 1

            if nivel == "ERROR":
                erros_por_ip[ip] = erros_por_ip.get(ip, 0) + 1

        except (ValueError, IndexError):
            malformados += 1

    print("\n=== Relatório de Logs ===")
    for nivel, qtd in contagem_nivel.items():
        print(f"  {nivel:<8}: {qtd} eventos")
    print(f"  Logs malformados: {malformados}")

    if erros_por_ip:
        ip_max = max(erros_por_ip, key=erros_por_ip.get)
        print(f"\n🚨 IP com mais erros: {ip_max} ({erros_por_ip[ip_max]} erros)")

        print("\nDetalhamento de erros:")
        for ip, qtd in sorted(erros_por_ip.items(), key=lambda x: x[1], reverse=True):
            erro = "erro" if qtd == 1 else "erros"
            print(f"   {ip:<18} → {qtd} {erro}")


# Exercício 10 — Sistema Completo de Gerenciamento de Senhas #

import random

def exercicio_10():
    print("\n" + "="*50)
    print("Exercício 10 — Sistema de Gerenciamento de Senhas")
    print("="*50)

    senhas = {
        "gmail":       "MinhaS3nha!",
        "github":      "Dev@2024Seguro",
        "banco_dados": "db123",
    }

    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
    especiais  = "!@#$%&*"

    def avaliar_forca(senha):
        if len(senha) < 8:
            return "Fraca"
        tem_maiuscula  = any(c.isupper() for c in senha)
        tem_minuscula  = any(c.islower() for c in senha)
        tem_numero     = any(c.isdigit() for c in senha)
        tem_especial   = any(c in especiais for c in senha)
        if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
            return "Forte"
        return "Média"

    def gerar_senha(tamanho):
        return "".join(random.choice(caracteres) for _ in range(tamanho))

    acoes = [
        ("cadastrar", ("linkedin", "Minha@Senha1")),
        ("cadastrar", ("gmail",    "outra")),
        ("gerar",     16),
        ("avaliar",   None),
        ("exportar",  None),
        ("sair",      None),
    ]

    for acao, dados in acoes:
        print()
        if acao == "sair":
            print("Encerrando...")
            break

        elif acao == "cadastrar":
            servico, senha = dados
            try:
                if servico in senhas:
                    raise ValueError(f"Serviço '{servico}' já cadastrado!")
                senhas[servico] = senha
                forca = avaliar_forca(senha)
                print(f" Cadastrado! Serviço: {servico} | Força: {forca}")
            except ValueError as e:
                print(f" Erro: {e}")

        elif acao == "gerar":
            nova = gerar_senha(dados)
            print(f" Senha aleatória gerada ({dados} chars): {nova}")

        elif acao == "avaliar":
            print("=== Avaliação de Força das Senhas ===")
            for servico, senha in senhas.items():
                forca = avaliar_forca(senha)
                emoji = "[-]" if forca == "Forte" else "[+]" if forca == "Média" else "[~]"
                print(f"  {emoji} {servico:<15}: {forca}")

        elif acao == "exportar":
            nome_arquivo = "senhas_relatorio.txt"
            try:
                with open(nome_arquivo, "w", encoding="utf-8") as f:
                    f.write("=== Relatório de Senhas ===\n\n")
                    for servico, senha in senhas.items():
                        forca = avaliar_forca(senha)
                        f.write(f"Serviço: {servico:<15} | Força: {forca}\n")
                print(f"📄 Relatório exportado com sucesso! → {nome_arquivo}")
            except IOError as e:
                print(f" Erro ao exportar: {e}")
