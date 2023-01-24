# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def price_check(products, product_prices, product_sold, sold_price):
    # Assumption : products.size = product_prices , product_sold = sold_price
    products_with_price = make_products_with_prices(products, product_prices)
    incorrect_sale = 0

    for i in range(len(product_sold)):
        product = product_sold[i]
        product_price = products_with_price[product]
        if product_price != sold_price[i]:
            incorrect_sale += 1

    return incorrect_sale

def make_products_with_prices(products, product_prices):
    products_with_prices= {}
    for i in range(len(products)):
        products_with_prices[products[i]] = product_prices[i]

    return products_with_prices

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    products = ['eggs', 'milk', 'cheese']
    productPrices = [2.89, 3.29, 5.79]
    productSold = ['eggs', 'eggs', 'cheese', 'milk']
    soldPrice = [2.89, 2.99, 5.97, 3.29]
    print(price_check(products, productPrices, productSold, soldPrice))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
