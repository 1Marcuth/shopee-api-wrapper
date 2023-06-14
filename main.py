from shopee_api import Shopee

def main():
    shopee = Shopee(origin_url = "https://shopee.com.br")

    data = shopee.fetch_product(url = "https://shopee.com.br/Videogame-Stick-10mil-2-Controles-Sem-Fio-Console-Original-Portatil-Jogos-Retro-Antigo-Marisa-i.400311012.18265078100")

    print(data)

if __name__ == "__main__":
    main()