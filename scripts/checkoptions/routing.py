from modulos.processes.routing_module import routing


clave = 'database'
tree = routing(clave)
print(tree[1])