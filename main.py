import numpy as np
import pickle

# namefile = 'a_example.in'
# # namefile = 'b_small.in'
# # namefile = 'c_medium.in'
# # namefile = 'd_big.in'
for namefile in ['a_example.in','b_small.in',  'c_medium.in','d_big.in' ]:
	f = open(namefile, 'r')

	l = []
	z = 0

	R = 0
	C = 0
	L = 0
	H = 0
	for line in f:
		if z == 0:
			line = line.split(' ')
			R, C, L, H = int(line[0]), int(line[1]), int(line[2]), int(line[3])
			# print R,C,L,H
		else:
			l.append([1 if i == 'T' else 0 for i in line[:-1]])
		z += 1


	# R = 5
	# C = 5
	# l = [[11,12,13,14,15],[21,22,23,24,25], [31,32,33,34,35], [41,42,43,44,45], [51,52,53,54,55]]
	# H = 6

	l = np.asarray(l)
	# for i in l:
	# 	print(i)

	zero_array = []
	for i in range(R):
		zero_array.append([0 for i in range(C)])


	for ir in range(R):
		print(ir)
		for ic in range(C):
			# print(ir, ic)
			max_column = ic + H - 1
			if max_column >= C:
				max_column = C - 1

			icolumn = max_column
			frst = True
			
			list_answer = []

			while icolumn >= ic:
				max_rows = int(H/(icolumn -ic + 1))
				# print(max_rows, 'max_rows')
				# print(l[ir:max_rows+ir, ic:icolumn+1])
				if frst:
					###one rows
					# print('onerwos')
					zzz = l[ir, :]
					zero = 0
					ones = 0
					# print(ir,ic, icolumn)
					# print(zzz)
					for xx in range(ic,icolumn+1):
						if zzz[xx] == 0:
							zero += 1
						else:
							ones += 1
						if ones >= L and zero >= L:
							x1, x2 = ir, ir
							y1, y2 = ic, xx
							S = (x2-x1+1)*(y2-y1+1)
							# print('::::', x1, y1, x2, y2, '	s', S)
							if S <= H:
								list_answer.append([x1, y1, x2, y2, S])
					# 	print(zzz[xx], end = '')
					# print()
					# print(';-----')
					frst = False
					while icolumn >= ic:
						max_rows = int(H/(icolumn - ic + 1))
						if max_rows > 1:
							break
					
						icolumn -= 1

				else:
					if max_rows >= R:
						max_rows = R - 1
					irows = ir
					zero = 0
					ones = 0
					# print('------')
					ones = 0
					zero = 0
					while irows <= max_rows:
						# print irows, 'irows'
						zzz = l[irows, :]
						# print(zzz)
						for xx in range(ic,icolumn+1):
							if zzz[xx] == 0:
								zero += 1
							else:
								ones += 1
							if ones >= L and zero >= L:
								x1, x2 = ir, irows
								y1, y2 = ic, icolumn
								S = (x2-x1+1)*(y2-y1+1)
								# print('::::', x1, y1, x2, y2, '	s', S)							
								if S <= H:

									list_answer.append([x1, y1, x2, y2, S])
								break
						irows += 1
					# print('------')
					icolumn -= 1
			# print(list_answer)
			zero_array[ir][ic] = list_answer.copy()
			# print(zero_array)
			# exit()

			# input('--')


	check = []
	for i in range(R):
		check.append([0 for i in range(C)])

	# print(zero_array)


	ir = 0
	new_lst = []
	zo = 0

	while ir < R:
		ic = 0
		while ic < C:
			if check[ir][ic] == 0:
				tmp = zero_array[ir][ic]
				minin = -11111111111111111
				have = False
				r1, c1, r2, c2 = 0,0,0,0
				for i_ in tmp:
					if i_[4] > minin:
					# if i_[4] < minin:
						r1, c1, r2, c2 = i_[0], i_[1], i_[2] ,i_[3]
						have = True
						for __ir in range(r1, r2 + 1):
							for __ic in range(c1, c2 + 1):	
								if check[__ir][__ic] == 1:
									have = False
									break
				if have:
					r1, c1, r2, c2 = i_[0], i_[1], i_[2] ,i_[3]
					for __ir in range(r1, r2 + 1):
						for __ic in range(c1, c2 + 1):	
							check[__ir][__ic] = 1
					zo += 1
					new_lst.append([r1, c1, r2, c2])
			ic += 1
		ir += 1

	fp = open('ans_'+namefile+'.txt', 'w')
	# print(zo, type(zo))
	fp.write(str(zo) + '\n')
	for i in new_lst:
		fp.write(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) + ' ' + str(i[3])+ '\n')
