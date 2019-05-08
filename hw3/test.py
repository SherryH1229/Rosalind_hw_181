def EulerianCycle_test(Adj):
	r = "stop"
	for i in Adj:
		if len(Adj[i])!=0:
			r = i
			break
	if r == "stop":
		return "stop"
	stack = []
	stack.append(r)
	#print (r,"r")
	result = []
	while len(stack) != 0:
		#print (stack,"stack")
		u = stack[len(stack) - 1]
		#print(u,"u")
		#print(Adj[u],"value of u")
		if len(Adj[u])!=0:
			w = Adj[u][0]
			#print(w,"w")
			stack.append(w)
			del Adj[u][0]
			#print (Adj[u],"value of u after")
		else:
			result.append(stack.pop())
	result = result[::-1]
	return result