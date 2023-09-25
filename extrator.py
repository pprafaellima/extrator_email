import re

class EmailNotFoundError(Exception):
    """
    Exceção personalizada para indicar que nenhum endereço de e-mail foi encontrado no texto.
    """
    pass

def extrair_emails(texto: str) -> list[str]:
    """
    Extrai endereços de e-mail de um texto usando uma expressão regular.

    Args:
        texto (str): O texto do qual os endereços de e-mail serão extraídos.

    Returns:
        list[str]: Uma lista de endereços de e-mail encontrados no texto.

    Raises:
        EmailNotFoundError: Se nenhum endereço de e-mail for encontrado no texto.
    """
    # Usando uma expressão regular para encontrar endereços de e-mail
    padrao_email = r'([A-Za-z0-9_]+@[A-Za-z0-9_]+\.[a-z]{2,3}(\.[a-z]{2})?)'
    emails_encontrados = re.findall(padrao_email, texto)
    
    if len(emails_encontrados) == 0:
        raise EmailNotFoundError("Não encontrei email no texto passado.")
    
    return [email[0] for email in emails_encontrados]
