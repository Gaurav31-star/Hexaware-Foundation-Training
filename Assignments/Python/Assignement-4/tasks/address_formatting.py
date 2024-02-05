def format_address(street, city, state, zip_code):
    formatted_address = f"{street.title()}, {city.title()}, {state.title()} {zip_code}"
    return formatted_address


# Example usage
street = "123 main st"
city = "example city"
state = "ny"
zip_code = "12345"

formatted_address = format_address(street, city, state, zip_code)
print("Formatted Address:", formatted_address)