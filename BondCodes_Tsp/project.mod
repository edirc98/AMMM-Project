// PLEASE ONLY CHANGE THIS FILE WHERE INDICATED.

// Length of codes.
int m = ...;

// Number of codes.
int n = ...;

// Codes.
// Input should satisfy the following precondition:
// the 0-th code is n zeroes: 000..000
int S[0..n-1][0..m-1] = ...;

// Range of code indices, including code 000...000.
range N0 = 0..n-1;

// Range of code indices, excluding code 000...000.
range N1 = 1..n-1;

// Define here your decision variables and 
// any other auxiliary program variables you need.

int d[N0][N0];
dvar int+ f;
dvar boolean y[N0][N0];
dvar boolean x[N1][N1];

// You can run an execute block if needed.

//Preprocces block for calculation distances (number of flips) beetween each code
execute {
  for (var x=0;x<=n-1;x++){
    for (var y=0;y<=n-1;y++){
      var flips=0;
		  for (var z=0; z<=m-1; z++){
		    flips+= S[x][z]==S[y][z]?0:1;
		  }
	  d[x][y]=flips;
    }
  }
}


// Write here the objective function.
minimize f;

subject to {
    // Write here the constraints.
    // 1. Minimize constrain. The actual value f to be minimized have its intended meaning
    // as total distance (number of flips) of our solution.
	sum(i,j in N0) d[i][j]*y[i][j] == f;
	  
	// 2. For each step that we do, we only enter one code (constraint c)
	forall (k in N1){
	  sum (j in N1) x[k][j] ==1;
	}
	// 
	forall (j in N1){
	  sum (k in N1) x[k][j] ==1;
	}
	
	// 3. After entering code i code j is entered.
	forall (k in 1..n-2){
	  forall(i,j in N1){
	    x[k][i]+x[k+1][j]-y[i][j]<=1;
	  }
	}
	//4. After the code 0…0, the 1-st code is entered. Making that code 0..0 is the first one. 
	forall (j in N1) y[0][j]==x[1][j];
	 
	//After the last code (n-1)-th, the code 0…0 is entered again. Making that 0..0 is the last code. 
	forall (j in N1) y[j][0]==x[n-1][j];
}


// You can run an execute block if needed.

// Print result of the order in which the codes are entered. 
execute POSTPROCESS {
  var lastDestination=0;
    for (var i in N1)
        for (var j in N1)
            if (x[i][j] > 0){
              write("[",i,"]", " From:",lastDestination," to destination -> ", j, " d:",d[lastDestination][j],"\n");
              lastDestination=j;
            }
    write("[",n,"]", " From:",lastDestination," to destination -> ", "0", " d:",d[lastDestination][0],"\n");
}
