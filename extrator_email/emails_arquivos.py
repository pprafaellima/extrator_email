"""Módulo responsável por navegar em pastas, extrair os emails e exportar para csv.
"""
import glob
from extrator import extrair_emails, EmailNotFoundError

def print_emails(list_of_emails: list[str]) -> None:
    """
    Imprime uma lista de endereços de e-mail.

    Args:
        list_of_emails (list[str]): Uma lista de endereços de e-mail.

    Returns:
        None
    """
    for email in list_of_emails:
        print(email)

def read_and_export_emails(path: str = "./", exported_file_path: str = "./emails.csv") -> None:
    """
    Lê arquivos de texto em um diretório e extrai endereços de e-mail, exportando-os para um arquivo CSV.

    Args:
        path (str, optional): O caminho para o diretório que contém os arquivos de texto. Padrão é "./".
        exported_file_path (str, optional): O caminho para o arquivo CSV de saída. Padrão é "./emails.csv".

    Returns:
        None

    Raises:
        OSError: Se ocorrer um erro ao abrir ou processar um arquivo.
    """
    for file in glob.glob(f"{path}/**/*.txt", recursive=True):
        try:
            with open(file) as txt_file:
                text = txt_file.read()
                list_of_emails = extrair_emails(text)
                print_emails(list_of_emails)
        except EmailNotFoundError as e:
            print(f"Warning: nenhum email encontrado em: {file}")
        except OSError as e:
            raise e

def main() -> None:
    """
    Função principal que lê arquivos de texto em um diretório e exporta endereços de e-mail para um arquivo CSV.
    
    Returns:
        None
    """
    read_and_export_emails("./arquivos", "emails.csv")

if __name__ == "__main__":
    main()
