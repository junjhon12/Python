sandwich_orders = ['sandwich1', 'sandwich2', 'sandwich3', 'sandwich4', 'sandwich5']
finished_sandwiches = []

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    
    print(f'Making sandwich: {current_sandwiches}')
    finished_sandwiches.append(current_sandwiches)
    
print(f'Finished sandwiches:')
for finish_sandwiches in finished_sandwiches:
    print(finish_sandwiches)