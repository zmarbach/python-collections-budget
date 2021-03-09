from . import Expense
import collections
import matplotlib.pyplot as plt

expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')
spending_categories = []

for expense in expenses.list:
    spending_categories.append(expense.category)

spending_counter = collections.Counter(spending_categories)
print(spending_counter)
top5 = spending_counter.most_common(5)
categories, count = zip(*top5)
print(categories, count)

# initialize 'fig' as the Figure, or top level container for our graph.
# And 'ax' as the Axes, which contains the actual figure elements.
fig, ax = plt.subplots()
# sets the x and y axis of graph
ax.bar(categories, count)
ax.set_title('# of Purchases by Category')
plt.show()