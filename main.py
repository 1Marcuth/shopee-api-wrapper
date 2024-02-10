from shopee_api import Shopee

def main():
    shopee = Shopee(origin_url = "https://shopee.com.br")

    data = shopee.fetch_product(url = "https://shopee.com.br/Kit-de-2-T%C3%AAnis-casual-masculino-confort%C3%A1vel-dia-a-dia-i.785541033.22892399435")

    print(data)

if __name__ == "__main__":
    main()