testcases=int(input())
 #no of students and PGs
 
 
def matching_pairs():
	n= int(input())
	pref_pg={}
	pref_students={}
	for i in range(n):
		pref=list(map(int, input().split()))
		pref_pg[i+1]=pref[1:]

	for i in range(n):
		pref=list(map(int, input().split()))
		pref_students[i+1]=pref[1:]

	# print(pref_pg)
	# print(pref_students)
	# print(pref_pg.keys())

	pg=[]
	students=[]
	for i in range (n+1):
		pg.append(False)
		students.append(False)

	pairs={}
	
	while len(pairs)<n:
		for i in pref_students.keys():
			if(students[i]==False):
				for j in range(len(pref_students[i])):
					pg_preferred=pref_students[i][j]
					if pg[pg_preferred]==False:
						pairs[pg_preferred]=i
						pg[pg_preferred]=True
						students[i]=True
						# print(pairs)
						# print(pg)
						# print(students)
						break
					else:
						if pref_pg[pg_preferred].index(i)<pref_pg[pg_preferred].index(pairs[pg_preferred]):
							students[pairs[pg_preferred]]=False
							pairs[pg_preferred]=i
							students[i]=True
							pg[pg_preferred]=True
							# print(pairs)
							# print(pg)
							# print(students)

							break
						else:
							continue



	for i in range(1,n+1):
		if students[i]==False or pg[i]==False:
			print(-1)


	ans=[0]*(n+1)

	for i in pairs.keys():
		ans[pairs[i]]=i
	# print(ans)

	for i in range(1, n+1):
		print(i, ans[i])


for i in range(testcases):
	matching_pairs()
