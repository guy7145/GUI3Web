# The data for your website

data = {
    # Example of a collection
    "dogs": [
        {
            "index": '0',
            'txt': "Pikatchu Breakfast",
            'small_txt': "Only 3.90$",
            'imageUrl': '/shared/images/pika_omlet.png'
        },
        {
            "index": '1',
            'txt': "strong food",
            'small_txt': "ask the waitress",
            'imageUrl': '/shared/images/db_food.png'
        },
        {
            "index": '2',
            'txt': "new beer special this summer!",
            'small_txt': "5.50$ for a glass",
            'imageUrl': '/shared/images/beers.png'
        },
        {
            "index": '3',
            'txt': "hear about our new home-brew beers",
            'small_txt': "Eeasy & Greasy Brewry",
            'imageUrl': '/shared/images/beer.png'
        },

    ],
}


def get_data(params):
    index = int(params.pop('_index', 0))
    length = int(params.pop('_length', 0))
    collection = params.pop('_collection')

    filtered_data = filter(lambda element: set(params.items()).issubset(set(element.items())),
                           data[collection])

    return filtered_data[index:index + length] if length > 0 else filtered_data[index:]
