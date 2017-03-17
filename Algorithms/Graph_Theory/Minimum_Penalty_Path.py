from operator import ior

(n,m) = [int(i) for i in raw_input().strip().split()]

paths = []

node_paths = {}

while True:
	line = raw_input().strip().split()
	if len(line) == 3:
		(node_u, node_v, c) = line

		if node_u not in node_paths:
			node_paths[node_u] = []

		if node_v not in node_paths:
			node_paths[node_v] = []

		node_paths[node_u].append((node_v, int(c)))
		node_paths[node_v].append((node_u, int(c)))
		paths.append(line)
	else:
		(start_node, end_node) = line
		break

def get_cost(l):
	if len(l) == 0:
		return 0

	return reduce(ior, l)

node_costs = {
	start_node: {0 : []},
}

node_eval_dict = {
	start_node: [0]
}

while True:
	next_eval_dict = {}
	if not node_eval_dict:
		break

	#print "batch size", len(node_eval_dict)
	for curr_node in node_eval_dict.keys():
		#print "node eval paths", curr_node, len(node_paths.get(curr_node, []))
		node_cost_list = []
		for x in node_eval_dict[curr_node]:
			if node_costs[curr_node] and x > 5 * min(node_costs[curr_node].keys()):
				# skip branches by heuristic
				continue
			node_cost_list.append((x, node_costs[curr_node][x]))

		#print "node eval costs on path", x, len(node_cost_list)
		for path in node_paths.get(curr_node, []):
			(dnode, cost) = path
			if dnode not in node_costs:
				node_costs[dnode] = {}
				# print "Found new node %s" % (dnode,)

			for curr_cost, curr_path in node_cost_list:
				dcost = get_cost([cost, curr_cost])
				if dcost not in node_costs[dnode]:
					node_costs[dnode][dcost] = curr_path + [curr_node]
					#print "Found new cost %s for node %s" % (dcost, dnode,)
					if dnode in next_eval_dict:
						if dcost not in next_eval_dict[dnode]:
							next_eval_dict[dnode].append(dcost)
					else:
						next_eval_dict[dnode] = [dcost]

	# switch to the next list
	node_eval_dict = next_eval_dict

#print node_costs.get(end_node)
if end_node in node_costs:
	print min(node_costs[end_node].keys())
else:
	print "-1"
