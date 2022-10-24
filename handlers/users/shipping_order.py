from telebot.types import ShippingQuery, PreCheckoutQuery
from data.loader import bot, db
from shipping_data.shipping_detail import *


@bot.shipping_query_handler(func=lambda query: True)
def choose_shipping(query: ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        bot.answer_shipping_query(shipping_query_id=query.id, ok=True,
                                  error_message="Yetkazib berish faqat O'zbekeston bo'ylab mavjud")

    elif query.shipping_address.city.lower() in ["toshkent", "tashkent", "тошкент", "ташкент"]:
        bot.answer_shipping_query(shipping_query_id=query.id, ok=True,
                                  shipping_options=[EXPRESS_SHIPPING, REGULAR_SHIPPING, PICUP_SHIPPING])

    elif query.shipping_address.city.lower() not in ["toshkent", "tashkent", "тошкент", "ташкент"]:
        bot.answer_shipping_query(shipping_query_id=query.id, ok=True,
                                  shipping_options=[REGION_SHIPPING])



@bot.pre_checkout_query_handler(func=lambda pre_checkout_query_handler: True)
def checkout(pre_checkout_query_handler: PreCheckoutQuery):
    user_id = pre_checkout_query_handler.from_user.id
    bot.answer_pre_checkout_query(pre_checkout_query_handler.id, ok=True, error_message="Test")
    bot.send_message(user_id, text="Xaridingiz uchun raxmat!")
    with bot.retrieve_data(user_id, user_id) as data:
        customer_full_name = db.check_user_for_registration(user_id)[0]
        customer_order = db.insert_order(customer_full_name)
        order_id = customer_order[0]
        for item in data["card"]:
            product_name = item
            product_quantity = data['card'][item]["quantity"]
            product_price = data["card"][item]['price']
            total_price = int(product_quantity) * int(product_price) * 100

            db.insert_product_item(product_name, product_quantity, total_price, order_id)

    bot.delete_state(user_id, user_id)