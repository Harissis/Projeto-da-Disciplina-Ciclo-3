from PIL import Image
import numpy as np

# Área total do Brasil em hectares (fonte IBGE)
AREA_BRASIL_HA = 850_000_000

# Função principal
def analisar_imagem(caminho_imagem):
    # Carregar a imagem
    img = Image.open(caminho_imagem)
    img_array = np.array(img)

    # Total de pixels
    total_pixels = img_array.size

    # Contagem de pixels para cada classe
    pixels_sem_dados = np.sum(img_array == 0)
    pixels_soja = np.sum(img_array == 39)
    pixels_pastagem = np.sum(img_array == 15)

    # Pixels úteis (excluindo sem dados)
    pixels_uteis = total_pixels - pixels_sem_dados

    # Percentuais de cobertura
    percentual_soja = (pixels_soja / pixels_uteis) * 100
    percentual_pastagem = (pixels_pastagem / pixels_uteis) * 100

    # Cálculo das áreas em hectares
    area_soja_ha = (percentual_soja / 100) * AREA_BRASIL_HA
    area_pastagem_ha = (percentual_pastagem / 100) * AREA_BRASIL_HA

    # Exibir os resultados
    resultados = {
        "Total de Pixels": total_pixels,
        "Pixels Sem Dados": pixels_sem_dados,
        "Pixels Soja": pixels_soja,
        "Pixels Pastagem": pixels_pastagem,
        "Área Soja (ha)": area_soja_ha,
        "Área Pastagem (ha)": area_pastagem_ha,
    }

    return resultados

# Caminho para a imagem
caminho_imagem = "brasil.png"
resultados = analisar_imagem(caminho_imagem)

# Imprimir resultados
for chave, valor in resultados.items():
    print(f"{chave}: {valor}")
