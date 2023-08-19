# Faça um programa em python que leiam em uma pasta arquivos pdfs diversos, procurando uma palavara especifica. 
# NO final mostre em que arquicos estão estas palavras e monte uma lista na tela."
# - Desafios - o número de arquivos pdf não importam
# - Eu tenho que digitar a palavra que eu quero procurar

import os
import fitz

def obter_arquivos_pdf_da_pasta(caminho_pasta):
    arquivos_pdf = [arquivo for arquivo in os.listdir(caminho_pasta) if arquivo.lower().endswith('.pdf')]
    return arquivos_pdf

def buscar_palavra_chave_no_pdf(caminho_arquivo, palavra_chave):
    documento_pdf = fitz.open(caminho_arquivo)
    for num_pagina in range(documento_pdf.page_count):
        pagina = documento_pdf.load_page(num_pagina)
        texto = pagina.get_text()
        if palavra_chave.lower() in texto.lower():
            documento_pdf.close()
            return True
    documento_pdf.close()
    return False

def main():
    caminho_pasta = input("Digite o caminho da pasta para listar os arquivos PDF: ")
    palavra_chave = input("Digite a palavra-chave a ser procurada: ")
    
    if not os.path.exists(caminho_pasta):
        print("Caminho da pasta inválido.")
        return

    arquivos_pdf = obter_arquivos_pdf_da_pasta(caminho_pasta)

    if arquivos_pdf:
        arquivos_com_palavra_chave = []
        for nome_arquivo in arquivos_pdf:
            caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)

            if buscar_palavra_chave_no_pdf(caminho_arquivo, palavra_chave):
                arquivos_com_palavra_chave.append(nome_arquivo)

        if arquivos_com_palavra_chave:
            print("Arquivos PDF contendo a palavra-chave:")
            for nome_arquivo in arquivos_com_palavra_chave:
                print(nome_arquivo)

            nome_arquivo_resultado = f"resultados_{palavra_chave}.txt"
            with open(nome_arquivo_resultado, "w") as arquivo_txt:
                arquivo_txt.write("Arquivos PDF contendo a palavra-chave:\n")
                for nome_arquivo in arquivos_com_palavra_chave:
                    arquivo_txt.write(nome_arquivo + "\n")

            print(f"Resultados gravados no arquivo '{nome_arquivo_resultado}'.")
        else:
            print("Nenhum arquivo PDF encontrado com a palavra-chave.")
    else:
        print("Nenhum arquivo PDF encontrado na pasta.")

if __name__ == "__main__":
    main()