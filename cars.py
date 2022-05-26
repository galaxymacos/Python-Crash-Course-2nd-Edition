def car_profile(manufacturer, model, **kwargs):
    kwargs["manufacturer"] = manufacturer
    kwargs["model"] = model
    return kwargs


print(car_profile("Telsa", "Model S", color="red", year="2022"))


