def make_car(manufacturer, model, **car_info):
    car_info['Manufacturer'] = manufacturer
    car_info['Model'] = model
    return car_info