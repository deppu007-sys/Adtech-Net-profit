# AdTech Net Profit Margin Calculator

def calculate_net_profit(revenue, cost, expenses):
    return revenue - cost - expenses

def calculate_net_margin(revenue, net_profit):
    if revenue == 0:
        return 0
    return (net_profit / revenue) * 100

# Sample Ad Campaign Data
ads = [
    {"Ad": "Campaign_A", "Revenue": 5000, "Cost": 3000, "Expenses": 500},
    {"Ad": "Campaign_B", "Revenue": 7000, "Cost": 4000, "Expenses": 800},
    {"Ad": "Campaign_C", "Revenue": 6000, "Cost": 2500, "Expenses": 700},
]

print("📊 AdTech Net Profit Report\n")

for ad in ads:
    revenue = ad["Revenue"]
    cost = ad["Cost"]
    expenses = ad["Expenses"]

    net_profit = calculate_net_profit(revenue, cost, expenses)
    net_margin = calculate_net_margin(revenue, net_profit)

    print(f"Ad: {ad['Ad']}")
    print(f"Revenue: {revenue}")
    print(f"Cost: {cost}")
    print(f"Expenses: {expenses}")
    print(f"Net Profit: {net_profit}")
    print(f"Net Margin: {round(net_margin, 2)}%")
    print("-" * 30)
