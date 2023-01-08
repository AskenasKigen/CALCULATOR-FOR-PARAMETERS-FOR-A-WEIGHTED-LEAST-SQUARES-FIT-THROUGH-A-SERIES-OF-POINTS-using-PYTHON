# PROGRAM-THAT-CALCULATES-THE-PARAMETERS-FOR-A-WEIGHTED-LEAST-SQUARES-FIT-THROUGH-A-SERIES-OF-POINTS-using PYTHON
In this project I developed a program that calculated the parameters for a weighted least squares fit through a series of points.
Background – Least squares fit to data points with errors
Given a set of N data points (xi, yi), i = 1, 2 ...N, with associated errors ei, the aim was to find the values of a and b such that
• y = a + bx
was the “best” line through the data points. The “best” line was achieved by weighting points with small errors more highly, and vice-versa. This was accomplished by minimising the sum of the squares of the differences between the data points and this line, weighting the data such that those with a smaller error contribute more to the least-squares sum we were trying to minimise.
Task
I wrote a program to calculate a weighted least-squares fit to a set of data. I used the number part of my student ID to generate a unique set of errors on the data so my fit could be unique. The x and y values for the 5 data points to be used in my fit were noted in the table provided.
1. Generated a set of random errors. Used my student ID as a seed in the random number generator in this code and ran it to create personalised errors ei on each of the data points in the table above. The errors ranged between the limits ±0.5.
2. Created a file with 3 columns of data. From left to right the columns stored values for x, y and e. There were 5 rows corresponding to each of the data points and their errors on y.
3. Wrote a program that:
• Reads in your data file and places values for x, y and e into 3 1- dimensional numpy arrays.
• Using these values of x, y and e, calculates values for p, q, r, s, t and Δ.
• Calculates the least squares parameters a and b.
• Calculates the uncertainty estimates for a and b (i.e. ∑a and ∑b ).
• Outputs to screen the values of the best fit parameters and their uncertainties.
• Incorporates an error checking code in the program to guard against possible problems such as only one
data point being entered from the file, a zero weight being entered, the data file not being found or syntax
errors in the data file.
• Draws a suitable graph of the data and the fit. Uses the matplotlib package to do this. The graph contains
the data, axis labels, and appropriately-sized error bars on the data. It also contains a line of best fit through the data (NOTE: this is not the same as using a line to join up individual points!). The easiest way to do this is to use your values of a and b to generate y-values for a set of corresponding x-values and then to plot these (in addition to plotting the data). Add the fit results and the error estimates to a small panel appropriately positioned within the graph.
• Creates a flowchart describing the program.
