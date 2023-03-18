from modulos.processes.routing_module import routing


key = 'database'
mode = False
tree = routing(mode)[key]
print(tree)