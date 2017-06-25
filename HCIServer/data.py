# The data for your website

data = {
    # Example of a collection
    "dogs": [
        {
            "size": 'small',
            "name": 'Welsh Corgi',
            'snippet': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                       "Duis sed ultricies lectus, et porttitor diam. Vivamus viverra tincidunt sagittis. "
                       "Fusce pellentesque nibh a convallis eleifend. Ut malesuada, justo a sodales accumsan, "
                       "magna purus vehicula lorem, a tincidunt justo odio vitae leo. Nulla a enim at metus ultrices "
                       "mollis. Donec scelerisque, metus non volutpat finibus, ligula justo sollicitudin nisl, "
                       "sit amet rutrum lorem felis eu orci. Sed dictum dignissim sapien, quis sodales dolor vehicula "
                       "sit amet. Etiam tempus felis turpis, sit amet vehicula ante tincidunt at. Integer ligula mi, "
                       "lobortis a hendrerit et, posuere id elit. Donec pellentesque nisl id vestibulum porttitor."
                       "Phasellus vel felis rhoncus, vehicula nisl in, eleifend orci. Cras tellus nibh, semper nec mi "
                       "eget, interdum vehicula ante. In sed ultrices erat, vitae dictum magna. Mauris id porttitor "
                       "diam. Curabitur ut vehicula mi. Sed tempor felis nec est semper facilisis. Nunc a enim a "
                       "lectus placerat feugiat. Maecenas ante risus, sollicitudin nec ligula eget, luctus mollis "
                       "lorem."
                       "Curabitur aliquam, leo id venenatis posuere, leo ex condimentum augue, quis iaculis "
                       "elit nunc non sapien. Mauris id nunc aliquam, imperdiet diam ac, viverra ante. Praesent "
                       "hendrerit neque et nisi tincidunt, mattis ultrices eros mollis. Etiam auctor facilisis felis, "
                       "et commodo.",
            'imageUrl': '/shared/images/corgi.jpg'
        },
        {
            "size": 'small',
            "name": 'Cavalier King Charles Spaniel',
            'snippet': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                       "Duis sed ultricies lectus, et porttitor diam. Vivamus viverra tincidunt sagittis. "
                       "Fusce pellentesque nibh a convallis eleifend. Ut malesuada, justo a sodales accumsan, "
                       "magna purus vehicula lorem, a tincidunt justo odio vitae leo. Nulla a enim at metus ultrices "
                       "mollis. Donec scelerisque, metus non volutpat finibus, ligula justo sollicitudin nisl, "
                       "sit amet rutrum lorem felis eu orci. Sed dictum dignissim sapien, quis sodales dolor vehicula "
                       "sit amet. Etiam tempus felis turpis, sit amet vehicula ante tincidunt at. Integer ligula mi, "
                       "lobortis a hendrerit et, posuere id elit. Donec pellentesque nisl id vestibulum porttitor."
                       "Phasellus vel felis rhoncus, vehicula nisl in, eleifend orci. Cras tellus nibh, semper nec mi "
                       "eget, interdum vehicula ante. In sed ultrices erat, vitae dictum magna. Mauris id porttitor "
                       "diam. Curabitur ut vehicula mi. Sed tempor felis nec est semper facilisis. Nunc a enim a "
                       "lectus placerat feugiat. Maecenas ante risus, sollicitudin nec ligula eget, luctus mollis "
                       "lorem."
                       "Curabitur aliquam, leo id venenatis posuere, leo ex condimentum augue, quis iaculis "
                       "elit nunc non sapien. Mauris id nunc aliquam, imperdiet diam ac, viverra ante. Praesent "
                       "hendrerit neque et nisi tincidunt, mattis ultrices eros mollis. Etiam auctor facilisis felis, "
                       "et commodo.",
            'imageUrl': '/shared/images/cavalier.jpg'
        },
        {
            "size": 'medium',
            "name": 'Australian Shepherd',
            'snippet': "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                       "Duis sed ultricies lectus, et porttitor diam. Vivamus viverra tincidunt sagittis. "
                       "Fusce pellentesque nibh a convallis eleifend. Ut malesuada, justo a sodales accumsan, "
                       "magna purus vehicula lorem, a tincidunt justo odio vitae leo. Nulla a enim at metus ultrices "
                       "mollis. Donec scelerisque, metus non volutpat finibus, ligula justo sollicitudin nisl, "
                       "sit amet rutrum lorem felis eu orci. Sed dictum dignissim sapien, quis sodales dolor vehicula "
                       "sit amet. Etiam tempus felis turpis, sit amet vehicula ante tincidunt at. Integer ligula mi, "
                       "lobortis a hendrerit et, posuere id elit. Donec pellentesque nisl id vestibulum porttitor."
                       "Phasellus vel felis rhoncus, vehicula nisl in, eleifend orci. Cras tellus nibh, semper nec mi "
                       "eget, interdum vehicula ante. In sed ultrices erat, vitae dictum magna. Mauris id porttitor "
                       "diam. Curabitur ut vehicula mi. Sed tempor felis nec est semper facilisis. Nunc a enim a "
                       "lectus placerat feugiat. Maecenas ante risus, sollicitudin nec ligula eget, luctus mollis "
                       "lorem."
                       "Curabitur aliquam, leo id venenatis posuere, leo ex condimentum augue, quis iaculis "
                       "elit nunc non sapien. Mauris id nunc aliquam, imperdiet diam ac, viverra ante. Praesent "
                       "hendrerit neque et nisi tincidunt, mattis ultrices eros mollis. Etiam auctor facilisis felis, "
                       "et commodo.",
            'imageUrl': '/shared/images/aussi.jpg'
        },

    ]
}


def get_data(params):
    index = int(params.pop('_index', 0))
    length = int(params.pop('_length', 0))
    collection = params.pop('_collection')

    filtered_data = filter(lambda element: set(params.items()).issubset(set(element.items())),
                           data[collection])

    return filtered_data[index:index + length] if length > 0 else filtered_data[index:]
