cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeep_list = ', '.join(cars['Jeep'])
    return jeep_list


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first = [model[0] for model in cars.values()]
    return first


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    grep_models = []
    for car in cars.values():
        for model in car:
            if grep.lower() in model.lower():
                grep_models.append(model)
    return sorted(grep_models)
    
    # another way
    # flatten the list of lists
    grep = grep.lower()
    models = sum(cars.values(), [])
    # models = list(chain.from_iterable(cars.values()))
    grep_models = [model for model in models if grep in model.lower()]
    return sorted(grep_models)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    sorted_car_dict = {car:sorted(model) for car,model in cars.items()}
    return sorted_car_dict