sandwich_orders = ['sandwich1', 'sandwich2', 'sandwich3', 'sandwich4', 'sandwich5',
                   'pastrami', 'pastrami', 'pastrami']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    
    print(f'Making sandwich: {current_sandwiches}')
    finished_sandwiches.append(current_sandwiches)
    

for finish_sandwiches in finished_sandwiches:
    print(f'Finished sandwiches: {finish_sandwiches}')