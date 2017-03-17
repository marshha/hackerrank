from operator import ior
import bisect

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

node_costs_only = {
	start_node: [0]
}

node_costs_set = {}
node_costs_set[start_node] = set([0])

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
			if x in node_costs_set[curr_node]:
				node_cost_list.append(x)

		#print "node eval costs on path", x, len(node_cost_list)
		for path in node_paths.get(curr_node, []):
			(dnode, cost) = path
			if dnode not in node_costs_only:
				node_costs_only[dnode] = []
				node_costs_set[dnode] = set()
				# print "Found new node %s" % (dnode,)

			for curr_cost in node_cost_list:
				dcost = get_cost([cost, curr_cost])
				if dcost not in node_costs_set[dnode]:
					matched = False
					for keys in list(node_costs_only[dnode]):
						if (dcost & keys) == keys:
							#print "matched %s to %s, skipping" % (dcost, keys)
							matched = True
							break

						#if (dcost > keys):
						#	# hit the maximum cover range
						#	break

						if (dcost & keys) == dcost:
							del node_costs_only[dnode][bisect.bisect_left(node_costs_only[dnode], keys)]
							node_costs_set[dnode].remove(keys)

					if matched:
						continue

					bisect.insort(node_costs_only[dnode], dcost)
					node_costs_set[dnode].add(dcost)
					#print "Found new cost %s for node %s" % (dcost, dnode,)
					if dnode in next_eval_dict:
						if dcost not in next_eval_dict[dnode]:
							bisect.insort(next_eval_dict[dnode], dcost)
					else:
						next_eval_dict[dnode] = [dcost]

	# switch to the next list
	node_eval_dict = next_eval_dict

if end_node in node_costs_only:
	print node_costs_only[end_node][0]
else:
	print "-1"

