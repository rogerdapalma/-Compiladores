import re

def remove_comments(input_file, comments_file):
    with open(input_file, 'r') as file:
        code = file.read()

    # Busca todos os comentários do tipo // até o final da linha
    single_line_comments = re.findall(r'//.*$', code, flags=re.MULTILINE)
    block_comments = re.findall(r'/\*.*?\*/', code, flags=re.DOTALL)

    with open(comments_file, 'w') as file:
        for comment in single_line_comments:
            file.write(comment.strip() + '\n')
        for comment in block_comments:
            file.write(comment.strip() + '\n')

    # Remove comentários do tipo // até o final da linha
    code = re.sub(r'//.*$', '', code, flags=re.MULTILINE)

    # Remove comentários do tipo /* comentário */
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)

    with open(input_file, 'w') as file:
        file.write(code)

    if '//' in code or '/*' in code:
        print("Os comentários não foram removidos completamente.")
    else:
        print("Os comentários foram removidos com sucesso.")

if __name__ == "__main__":
    input_file = "arquivo_remover_comentario.c"   # arquivo para ler
    comments_file = "comentarios_excluidos.sco"  # comentario salvo
    remove_comments(input_file, comments_file)

# Lê e imprime o conteúdo do arquivo de comentários removidos
comments_file = "comentarios_excluidos.sco" # arquivo de comentários removidos
with open(comments_file, 'r') as file:
    content = file.read()
print(content)
