
def remove_from_list(list0,value):
	if value in list0:
		list0.remove(value)
		return True
	return False

def set_grid_limit(data,row_limit,col_limit,squ_limit,grid_limit):
	for i,row in enumerate(data):
		for j,col in enumerate(row):
			if col==0:
				grid_limit[i][j]=list(set(row_limit[i]) & set(col_limit[j]) & set(squ_limit[i//3*3+j//3]))
				if grid_limit[i][j]==[]:
					return False
	return True

def fill_next(total,data,row_limit,col_limit,squ_limit,grid_limit):
	min=10;x,y=0,0
	for i,row in enumerate(grid_limit):
		for j,col in enumerate(row):
			if 0 < len(col) < min:
				min=len(col)
				x,y=i,j
	
	i,j=x,y
	grid_limit_t=grid_limit[i][j]
	for value in grid_limit[i][j]:
		data[i][j]=value
		grid_limit[i][j]=[]
		c_row=remove_from_list(row_limit[i],value)
		c_col=remove_from_list(col_limit[j],value)
		c_squ=remove_from_list(squ_limit[i//3*3+j//3],value)
		
		if total==1:
			return True
			
		if set_grid_limit(data,row_limit,col_limit,squ_limit,grid_limit):
			if fill_next(total-1,data,row_limit,col_limit,squ_limit,grid_limit):
				return True
		
		if c_row:row_limit[i].append(value)
		if c_col:col_limit[j].append(value)
		if c_squ:squ_limit[i//3*3+j//3].append(value)
	data[i][j]=0
	grid_limit[i][j]=grid_limit_t
		
	return False

def main():		
	row_limit=[range(1,10) for i in range(9)]
	col_limit=[range(1,10) for i in range(9)]
	squ_limit=[range(1,10) for i in range(9)]
	grid_limit=[[[] for i in range(9)] for j in range(9)]
	
	filename='case1.txt'
	data=[map(int,row_t.rstrip().split()) for i,row_t in enumerate(open(filename))]
	
	total=0
	for i in range(9):
		for j in range(9):
			tdata=data[i][j]
			if tdata>0:
				remove_from_list(row_limit[i],tdata)
				remove_from_list(col_limit[j],tdata)
				remove_from_list(squ_limit[i//3*3+j//3],tdata)
			else:
				total+=1
	
	set_grid_limit(data,row_limit,col_limit,squ_limit,grid_limit)
				
	fill_next(total,data,row_limit,col_limit,squ_limit,grid_limit)
	
	for row in data:
		print row
		
if __name__=="__main__":
	main()
	

