"""2291. Maximum Profit From Trading Stocks
You are given two O-indexed integer arrays of the same length present and future where present[i] is the current price of the ith stock 
and future[i] is the price of the ith stock a year in the future, You may buy each stock at most once. you're also given an integer budget 
representing the amount of money you currently have.
Return the maximum amount of profit you can make.
present = [5,4,6,2,3], future = [8,5,4,3,5], budget = 10                output = 6
Explaination : One possible way to maximise your profit is to : buy the 0th, 3rd, 4th stock for the total of 5+2+3=10
next year sell all the three stocks for a total of 8+3+5=16, the profit you made is 16-10=6
present = [2,2,5], future = [3,4,10], budget = 6                        output = 5
present = [3,3,12], future = [0,3,15], budget = 10                      output = 0
"""

