import pyinputplus as pyip

prices = {
  'bread': {'Wheat': 1.00, 'White': 0.90, 'Sourdough': 1.20},
  'protein': {'Chicken': 2.50, 'Turkey': 2.75, 'Ham': 2.25, 'Tofu': 2.00},
  'cheese': {'Cheddar': 0.75, 'Swiss': 0.80, 'Mozzarella': 0.70},
  'lettuce_tomato_onion': 0.50,
  'sauce': {'Mayo': 0.15, 'Mustard': 0.10, 'Ketchup': 0.10, 'None': 0.00}
}

def make_sandwich():
  print("Sandwich Making Maker")
  
  bread_type = pyip.inputMenu(
    ['Wheat', 'White', 'Sourdough'],
    numbered=True,
    prompt='Choose your bread type: '
  )
  
  protein = pyip.inputMenu(
    ['Chicken', 'Turkey', 'Ham', 'Tofu'],
    numbered=True,
    prompt='Choose your protein: '
  )
  
  cheese = pyip.inputYesNo(prompt='Would you like cheese? (yes/no): ')
  cheese_type = None
  if cheese:
    cheese_type = pyip.inputMenu(
        ['Cheddar', 'Swiss', 'Mozzarella'],
        numbered=True,
        prompt='Choose your cheese type: '
    )
  
  lettuce_tomato_onion = pyip.inputYesNo(
    prompt='Would you like lettuce, tomato, and onion? (yes/no): '
  )

  sauce = pyip.inputMenu(
    ['Mayo', 'Mustard', 'Ketchup', 'None'],
    numbered=True,
    prompt='Choose your sauce: '
  )
  
  print_order(
    bread=bread_type,
    protein=protein,
    cheese=cheese,
    cheese_type=cheese_type,
    lettuce_tomato_onion=lettuce_tomato_onion,
    sauce=sauce
  )

def print_order(bread, protein, cheese, cheese_type, lettuce_tomato_onion, sauce):
  total_price = 0.0
  total_price += prices['bread'][bread]
  total_price += prices['protein'][protein]
  total_price += prices['cheese'][cheese_type]
  if lettuce_tomato_onion:
    total_price += prices['lettuce_tomato_onion']
  total_price += prices['sauce'][sauce]
  
  print("\nYour sandwich order:")

  print(f"Bread: {bread} (${prices['bread'][bread]:.2f})")

  print(f"Protein: {protein} (${prices['protein'][protein]:.2f})")

  if cheese:
    print(f"Cheese: {cheese_type} (${prices['cheese'][cheese_type]:.2f})")
  else:
    print("Cheese: None")
  
  if lettuce_tomato_onion:
    print("Lettuce, Tomato, Onion: Yes ($0.50)")
  else:
    print("Lettuce, Tomato, Onion: No")
  
  print(f"Sauce: {sauce} (${prices['sauce'][sauce]:.2f})")
  
  print(f"\nTotal Price: ${total_price:.2f}")


make_sandwich()