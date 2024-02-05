def find_similar_addresses(address, address_list):
    similar_addresses = [similar for similar in address_list if similar.lower() in address.lower()]
    return similar_addresses

# Example usage
address_to_check = "123 Main St, Example City, NY 12345"
address_list = ["123 Main St", "456 Side St", "789 Up St"]

similar_addresses = find_similar_addresses(address_to_check, address_list)
print("Similar Addresses:", similar_addresses)