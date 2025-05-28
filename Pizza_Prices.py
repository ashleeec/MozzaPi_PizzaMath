# Prices of each ingredient (in USD)
ingredient_prices = { #this can easily be made a csv/ airtable, or we can keep it as a dict
    'cheese': 0.50,
    'pepperoni': 0.75,
    'dough': 0.30,
    'sauce': 0.25
}

# Ingredient list for each pizza
pizza_recipes = {
    'Cheese': ['dough', 'sauce', 'cheese'],
    'Pepperoni': ['dough', 'sauce', 'cheese', 'pepperoni']
}

# Client order (Connect to Airtable using Airtable API function get record)
client_order = {
    'Pizza Type': ['Cheese', 'Pepperoni'],
    'Quantity': [10, 15]
}

# Compute cost
total_ingredient_cost = 0
per_pizza_type_prices = {}

for i, pizza_type in enumerate(client_order['Pizza Type']):
    quantity = client_order['Quantity'][i]
    ingredients = pizza_recipes[pizza_type]
    
    # Calculate cost per pizza
    cost_per_pizza = sum(ingredient_prices[ingredient] for ingredient in ingredients)
    
    # Total price for that pizza type
    per_pizza_type_prices[pizza_type] = cost_per_pizza * quantity
    total_ingredient_cost += per_pizza_type_prices[pizza_type]

# Output (Connect to Airtable using Airtable API function to update record)
print("Breakdown per pizza type:", per_pizza_type_prices)
print("Total ingredient cost", total_ingredient_cost)
