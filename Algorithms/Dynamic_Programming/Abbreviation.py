#!/bin/python

import sys

def test_input(a, b, eval_tuples_dict, b_curr_pos, b_rem_pos_list):
	if len(b_rem_pos_list) == 0:
		gap_text = a[b_curr_pos+1:len(a)]
		if any(a_char.isupper() for a_char in gap_text):
			#print "eval (can't drop trailing): text: %s curr: %s" % (gap_text, b_curr_pos)
			return False
		return True

	b_rem_pos_list[0] = [ x for x in b_rem_pos_list[0] if x > b_curr_pos ]
	b_rem_pos_entry = b_rem_pos_list[0]
	for b_rem_pos_val in b_rem_pos_entry:
		if b_curr_pos == None:
			if any(a_char.isupper() for a_char in a[0:b_rem_pos_val]):
				#print "eval (header): curr: %s rem_val: %s" % (b_curr_pos, b_rem_pos_val)
				return False

		a_rem_len = len(a) - b_rem_pos_val
		b_rem_len = len(b_rem_pos_list)
		if a_rem_len < b_rem_len:
			#print "eval (shortcut-length): a_rem_len:%s b_rem:%s" % (a_rem_len, b_rem_len)
			return False

		if b_curr_pos != None:
			tup_check = (b_curr_pos, b_rem_pos_val, "len")
			tup_check_result = eval_tuples_dict.get(tup_check)
			if tup_check_result == False:
				#print "tuple %s already failed" % (tup_check,)
				continue

			elif tup_check_result == None:
				if b_rem_pos_val <= b_curr_pos:
					#print "eval (behind): curr: %s rem_val: %s" % (b_curr_pos, b_rem_pos_val)
					continue

				#print "evaluating: pos: %s next: %s a_rem: %s b_rem: %s" % (b_curr_pos, b_rem_pos_val, a_rem_len, b_rem_len)
				gap_text = a[b_curr_pos+1:b_rem_pos_val]
				if any(a_char.isupper() for a_char in gap_text):
					#print "eval (can't drop gap): text: %s curr: %s rem_val: %s" % (gap_text, b_curr_pos, b_rem_pos_val)
					eval_tuples_dict[tup_check] = False
					return False

				eval_tuples_dict[tup_check] = True

		tup_check = (b_rem_pos_val, len(b_rem_pos_list[1:]), "tree")
		tup_check_result = eval_tuples_dict.get(tup_check)
		if tup_check_result != None:
			#print "subtree %s already checked" % (tup_check,)
			return tup_check_result

		ret = test_input(a, b, eval_tuples_dict, b_rem_pos_val, b_rem_pos_list[1:])
		eval_tuples_dict[tup_check] = ret
		if not ret:
			continue
		else:
			return ret

		

	return False

q = int(raw_input().strip())
for x in xrange(0,q):
	a = list(raw_input().strip())
	b = list(raw_input().strip())

	b_pos_list = []
	for b_idx in xrange(0, len(b)):
		b_char = b[b_idx]
		b_pos_list_entry = []
		for a_idx in xrange(0, len(a)):
			a_char = a[a_idx]
			if a_char.upper() == b_char:
				b_pos_list_entry.append(a_idx)

		b_pos_list.append(b_pos_list_entry)

	outcome = None
	for b_idx in xrange(0, len(b_pos_list)):
		entry = b_pos_list[b_idx]
		#print b_idx, b[b_idx], entry
		if len(entry) == 0:
			outcome = "NO"

	eval_tuples_dict = {}
	if not outcome:
		if test_input(a, b, eval_tuples_dict, None, b_pos_list):
			outcome = "YES"
		else:
			outcome = "NO"

	print outcome
