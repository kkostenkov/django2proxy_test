
def parse_filters(message):
    arguments = message.split("|")
    parsed_message = { "subject":arguments[0],
                       "filters":["|" + filter for filter in arguments[1:]],
                       }
    return parsed_message
