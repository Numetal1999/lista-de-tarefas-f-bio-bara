import urllib.request
import json
import ipaddress

ips = [
    "8.8.8.8",
    "1.1.1.1",
    "185.220.101.1",
    "208.67.222.222",
    "91.240.118.172",
]

def is_internal(ip):
    try:
        return ipaddress.ip_address(ip).is_private
    except ValueError:
        return False

def consultar_ip(ip):
    url = f"https://ipinfo.io/{ip}/json"
    try:
        with urllib.request.urlopen(url, timeout=5) as response:
            data = json.loads(response.read().decode())

        if "error" in data:
            erro = data["error"]
            return {
                "status": "erro",
                "codigo": data.get("status", "?"),
                "titulo": erro.get("title", "Erro desconhecido"),
                "mensagem": erro.get("message", ""),
            }

        return {
            "status": "ok",
            "cidade": data.get("city", "N/A"),
            "regiao": data.get("region", "N/A"),
            "pais": data.get("country", "N/A"),
            "org": data.get("org", "N/A"),
            "privacy": data.get("privacy", {}),
        }

    except Exception as e:
        return {
            "status": "erro",
            "codigo": 500,
            "titulo": "Falha na requisição",
            "mensagem": str(e),
        }

def exibir_resultado(ip, dados):
    tipo = "INTERNO" if is_internal(ip) else "EXTERNO"

    print(f"IP: {ip}")

    if dados["status"] == "erro":
        print(f"  [ERRO {dados['codigo']}] {dados['titulo']}: {dados['mensagem']}")
        print(f"  Tipo: {tipo}")
        return False

    privacy = dados.get("privacy", {})
    flags = []
    if privacy.get("vpn"):
        flags.append("VPN")
    if privacy.get("proxy"):
        flags.append("Proxy")
    if privacy.get("tor"):
        flags.append("Tor")
    if privacy.get("relay"):
        flags.append("Relay")

    print(f"  Cidade: {dados['cidade']}")
    print(f"  Região: {dados['regiao']}")
    print(f"  País:   {dados['pais']}")
    print(f"  Org:    {dados['org']}")
    if flags:
        print(f"  Flags:  {', '.join(flags)}")
    print(f"  Tipo:   {tipo}")
    return True

def main():
    print("=" * 35)
    print("      Relatório de IPs")
    print("=" * 35)

    externos = 0
    internos = 0
    erros = 0

    for ip in ips:
        print()
        dados = consultar_ip(ip)
        sucesso = exibir_resultado(ip, dados)

        if not sucesso:
            erros += 1
        elif is_internal(ip):
            internos += 1
        else:
            externos += 1

    print()
    print("=" * 35)
    print("         Resumo")
    print("=" * 35)
    print(f"Total de IPs consultados: {len(ips)}")
    print(f"Externos: {externos}")
    print(f"Internos: {internos}")
    print(f"Erros de consulta: {erros}")

main()

#################################################################################

import urllib.request
import urllib.error
import json
import time
import os
from datetime import datetime

sites = [
    {"nome": "Google",      "url": "https://www.google.com"},
    {"nome": "GitHub",      "url": "https://api.github.com"},
    {"nome": "HTTPBin",     "url": "https://httpbin.org/get"},
    {"nome": "Inexistente", "url": "https://site-que-nao-existe-xyz.com"},
    {"nome": "Lento",       "url": "https://httpbin.org/delay/5"},
]

TIMEOUT = 3
INTERVALO = 30
ARQUIVO_HISTORICO = "historico.json"


def carregar_historico():
    if os.path.exists(ARQUIVO_HISTORICO):
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_historico(historico):
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=2)


def verificar_site(site):
    inicio = time.time()
    horario = datetime.now().strftime("%H:%M:%S")

    try:
        req = urllib.request.Request(site["url"], headers={"User-Agent": "Monitor/1.0"})
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            status = resp.status
        tempo_ms = int((time.time() - inicio) * 1000)
        return {
            "nome": site["nome"],
            "url": site["url"],
            "horario": horario,
            "timestamp": time.time(),
            "status_code": status,
            "tempo_ms": tempo_ms,
            "online": True,
            "erro": None,
        }

    except urllib.error.HTTPError as e:
        tempo_ms = int((time.time() - inicio) * 1000)
        return {
            "nome": site["nome"],
            "url": site["url"],
            "horario": horario,
            "timestamp": time.time(),
            "status_code": e.code,
            "tempo_ms": tempo_ms,
            "online": False,
            "erro": f"HTTPError {e.code}",
        }

    except urllib.error.URLError as e:
        motivo = str(e.reason)
        if "timed out" in motivo.lower():
            erro = f"Timeout: {TIMEOUT}s"
        else:
            erro = "ConnectionError"
        return {
            "nome": site["nome"],
            "url": site["url"],
            "horario": horario,
            "timestamp": time.time(),
            "status_code": None,
            "tempo_ms": None,
            "online": False,
            "erro": erro,
        }

    except Exception as e:
        return {
            "nome": site["nome"],
            "url": site["url"],
            "horario": horario,
            "timestamp": time.time(),
            "status_code": None,
            "tempo_ms": None,
            "online": False,
            "erro": str(e),
        }


def exibir(resultado):
    nome = resultado["nome"].ljust(12)
    horario = resultado["horario"]

    if resultado["online"]:
        status = str(resultado["status_code"]).rjust(3)
        tempo = f"{resultado['tempo_ms']}ms".rjust(6)
        print(f"[{horario}] {nome} {status}  {tempo}  ONLINE")
    else:
        erro = resultado["erro"] or "Erro desconhecido"
        print(f"[{horario}] {nome} ---     ---  OFFLINE ({erro})")


def ciclo(historico):
    print(f"\n{'─' * 55}")
    print(f"  Verificação: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"{'─' * 55}")

    for site in sites:
        resultado = verificar_site(site)
        historico.append(resultado)
        exibir(resultado)

        if not resultado["online"]:
            print(f"   ALERTA: {resultado['nome']} está OFFLINE!")

    salvar_historico(historico)
    print(f"\n  Histórico salvo em '{ARQUIVO_HISTORICO}' ({len(historico)} registros)")


def main():
    print("=" * 55)
    print("         Monitor de Websites")
    print(f"  Timeout: {TIMEOUT}s  |  Intervalo: {INTERVALO}s")
    print("  Ctrl+C para encerrar")
    print("=" * 55)

    historico = carregar_historico()

    while True:
        try:
            ciclo(historico)
            print(f"\n  Próxima verificação em {INTERVALO}s...")
            time.sleep(INTERVALO)
        except KeyboardInterrupt:
            print("\n\nMonitor encerrado pelo usuário.")
            print(f"Total de registros salvos: {len(historico)}")
            break


main()  

####################################################################################

import urllib.request
import urllib.error
import json
import time
import os
from datetime import datetime

BASE_URL = "https://api.github.com"
TIMEOUT = 10
ARQUIVO_RESULTADOS = "github_resultados.json"

usuarios_teste = ["octocat", "torvalds", "guido"]

resultados_sessao = []


def requisitar(endpoint):
    url = f"{BASE_URL}{endpoint}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "GithubExplorer/1.0",
        "Accept": "application/vnd.github+json",
    })

    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode()), resp.status

    except urllib.error.HTTPError as e:
        corpo = {}
        try:
            corpo = json.loads(e.read().decode())
        except Exception:
            pass

        if e.code == 403:
            reset = e.headers.get("X-RateLimit-Reset", "")
            if reset:
                espera = int(reset) - int(time.time())
                print(f"\n   Rate limit atingido. Tente novamente em {max(espera, 0)}s.")
            else:
                print("\n   Acesso negado (403):", corpo.get("message", ""))
        elif e.code == 404:
            print(f"\n  X  Não encontrado (404): {corpo.get('message', url)}")
        else:
            print(f"\n  X  Erro HTTP {e.code}: {corpo.get('message', '')}")
        return None, e.code

    except urllib.error.URLError as e:
        if "timed out" in str(e.reason).lower():
            print(f"\n  X  Timeout após {TIMEOUT}s.")
        else:
            print(f"\n  X  Erro de conexão: {e.reason}")
        return None, None

    except Exception as e:
        print(f"\n  X  Erro inesperado: {e}")
        return None, None


def salvar(dados, tipo, identificador):
    entrada = {
        "tipo": tipo,
        "identificador": identificador,
        "consultado_em": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "dados": dados,
    }
    resultados_sessao.append(entrada)

    with open(ARQUIVO_RESULTADOS, "w", encoding="utf-8") as f:
        json.dump(resultados_sessao, f, ensure_ascii=False, indent=2)

    print(f"\n  S  Salvo em '{ARQUIVO_RESULTADOS}'")


def ver_perfil(username):
    print(f"\n{'─' * 45}")
    print(f"  Perfil: {username}")
    print(f"{'─' * 45}")

    dados, status = requisitar(f"/users/{username}")
    if not dados:
        return

    print(f"  Nome:         {dados.get('name') or 'N/A'}")
    print(f"  Bio:          {dados.get('bio') or 'N/A'}")
    print(f"  Empresa:      {dados.get('company') or 'N/A'}")
    print(f"  Localização:  {dados.get('location') or 'N/A'}")
    print(f"  Repos públicos: {dados.get('public_repos', 0)}")
    print(f"  Seguidores:   {dados.get('followers', 0):,}")
    print(f"  Seguindo:     {dados.get('following', 0):,}")
    print(f"  Criado em:    {dados.get('created_at', 'N/A')[:10]}")
    print(f"  URL:          {dados.get('html_url', '')}")

    salvar(dados, "perfil", username)


def listar_repos(username):
    print(f"\n{'─' * 45}")
    print(f"  Repositórios de: {username}")
    print(f"{'─' * 45}")

    dados, status = requisitar(f"/users/{username}/repos?per_page=30&sort=stars")
    if not dados:
        return

    if not dados:
        print("  Nenhum repositório público encontrado.")
        return

    for i, repo in enumerate(dados, 1):
        nome = repo.get("name", "")
        stars = repo.get("stargazers_count", 0)
        lingua = repo.get("language") or "—"
        forks = repo.get("forks_count", 0)
        desc = repo.get("description") or ""
        desc_curta = desc[:40] + "..." if len(desc) > 40 else desc

        print(f"  {i:>2}. {nome:<25} ★ {stars:<7,} 🍴{forks:<5} ({lingua})")
        if desc_curta:
            print(f"       {desc_curta}")

    salvar(dados, "repos", username)


def ver_repositorio(owner, repo):
    print(f"\n{'─' * 45}")
    print(f"  Repositório: {owner}/{repo}")
    print(f"{'─' * 45}")

    dados, status = requisitar(f"/repos/{owner}/{repo}")
    if not dados:
        return

    print(f"  Nome:        {dados.get('full_name', '')}")
    print(f"  Descrição:   {dados.get('description') or 'N/A'}")
    print(f"  Linguagem:   {dados.get('language') or 'N/A'}")
    print(f"  Stars:       {dados.get('stargazers_count', 0):,}")
    print(f"  Forks:       {dados.get('forks_count', 0):,}")
    print(f"  Watchers:    {dados.get('watchers_count', 0):,}")
    print(f"  Issues:      {dados.get('open_issues_count', 0):,}")
    print(f"  Licença:     {(dados.get('license') or {}).get('name', 'N/A')}")
    print(f"  Criado em:   {dados.get('created_at', '')[:10]}")
    print(f"  Atualizado:  {dados.get('updated_at', '')[:10]}")
    print(f"  Clone URL:   {dados.get('clone_url', '')}")

    salvar(dados, "repositorio", f"{owner}/{repo}")


def ver_rate_limit():
    print(f"\n{'─' * 45}")
    print("  Status do Rate Limit")
    print(f"{'─' * 45}")

    dados, _ = requisitar("/rate_limit")
    if not dados:
        return

    core = dados.get("resources", {}).get("core", {})
    limite = core.get("limit", 0)
    restante = core.get("remaining", 0)
    reset_ts = core.get("reset", 0)
    reset_hora = datetime.fromtimestamp(reset_ts).strftime("%H:%M:%S")

    print(f"  Limite total:   {limite}")
    print(f"  Restante:       {restante}")
    print(f"  Reset em:       {reset_hora}")
    print(f"  Usado:          {limite - restante}/{limite}")


def menu_principal():
    print("\n" + "=" * 45)
    print("       GitHub Explorer")
    print("=" * 45)
    print("  1. Buscar perfil de usuário")
    print("  2. Listar repositórios de usuário")
    print("  3. Detalhes de um repositório")
    print("  4. Testar com usuários de exemplo")
    print("  5. Ver rate limit")
    print("  0. Sair")
    print("─" * 45)
    return input("  Escolha: ").strip()


def opcao_perfil():
    usuario = input("\n  Nome do usuário: ").strip()
    if usuario:
        ver_perfil(usuario)


def opcao_repos():
    usuario = input("\n  Nome do usuário: ").strip()
    if usuario:
        listar_repos(usuario)


def opcao_repositorio():
    owner = input("\n  Dono do repositório (owner): ").strip()
    repo = input("  Nome do repositório: ").strip()
    if owner and repo:
        ver_repositorio(owner, repo)


def opcao_exemplos():
    print("\n  Usuários de teste:", ", ".join(usuarios_teste))
    print("  1. octocat")
    print("  2. torvalds")
    print("  3. guido")
    escolha = input("  Escolha (1-3): ").strip()

    mapa = {"1": "octocat", "2": "torvalds", "3": "guido"}
    usuario = mapa.get(escolha)

    if not usuario:
        print("  Opção inválida.")
        return

    print("\n  O que deseja ver?")
    print("  1. Perfil")
    print("  2. Repositórios")
    acao = input("  Escolha (1-2): ").strip()

    if acao == "1":
        ver_perfil(usuario)
    elif acao == "2":
        listar_repos(usuario)
    else:
        print("  Opção inválida.")


def main():
    print("\n  Carregando histórico...")
    global resultados_sessao

    if os.path.exists(ARQUIVO_RESULTADOS):
        with open(ARQUIVO_RESULTADOS, "r", encoding="utf-8") as f:
            resultados_sessao = json.load(f)
        print(f"  {len(resultados_sessao)} registro(s) carregado(s) de sessões anteriores.")
    else:
        print("  Nenhum histórico encontrado. Iniciando novo.")

    acoes = {
        "1": opcao_perfil,
        "2": opcao_repos,
        "3": opcao_repositorio,
        "4": opcao_exemplos,
        "5": ver_rate_limit,
    }

    while True:
        escolha = menu_principal()

        if escolha == "0":
            print(f"\n  Sessão encerrada. {len(resultados_sessao)} registro(s) salvos.\n")
            break
        elif escolha in acoes:
            acoes[escolha]()
        else:
            print("\n  Opção inválida.")

        input("\n  [Enter para continuar]")


main()
