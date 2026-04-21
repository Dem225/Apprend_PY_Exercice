vscode_lsp_terminal_prompt_tracker= {}

def inverse_number(n):
    n=str(n)
    nombre=''
    for elment in n:
        nombre=elment+nombre
    return nombre
print(inverse_number(123))

def inverse_number(n):
    return int(str(n)[: : -1])
print(inverse_number(123))
