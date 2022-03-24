# CS103a Spring 22

# PA02: tracker.py and the Transaction class

This git repository is for sharing code developed in the course lessons.
Each Lesson will be a different branch with the name L??.
Not all lessons have branches.

``` bash
# Meng-Ku Chen
Script started on Thu Mar 24 15:15:11 2022
[1m[7m%[27m[1m[0m                                                                                                                                    
 

[0m[27m[24m[Jchenmengku@chenmenggudeair pa02 % [K[?2004hexitpython3 tracker.py[18Dcd pa02           [11Dpython3 tracker.py[18Dcd pao2           [11Dpython3 tracker.py[18Dcd pa02           [11Dpython3 tracker.py[18Dexit              [14D    ppylint tracker.py[?2004l

************* Module tracker
tracker.py:65:4: R1705: Unnecessary "elif" after "return" (no-else-return)
tracker.py:63:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
tracker.py:126:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:131:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:134:39: C0103: Argument name "t" doesn't conform to snake_case naming style (invalid-name)
tracker.py:140:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:145:14: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:149:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)
tracker.py:153:10: C0209: Formatting a regular string which could be a f-string (consider-using-f-string)

------------------------------------------------------------------
Your code has been rated at 8.86/10 (previous run: 8.86/10, +0.00)

[1m[7m%[27m[1m[0m                                                                                                                                    
 

[0m[27m[24m[Jchenmengku@chenmenggudeair pa02 % [K[?2004hpylint tracker.py          transactions.py[?2004l

************* Module transactions
transactions.py:17:40: C0103: Argument name "t" doesn't conform to snake_case naming style (invalid-name)
transactions.py:23:46: W0622: Redefining built-in 'type' (redefined-builtin)

------------------------------------------------------------------
Your code has been rated at 9.64/10 (previous run: 9.64/10, +0.00)

[1m[7m%[27m[1m[0m                                                                                                                                    
 

[0m[27m[24m[Jchenmengku@chenmenggudeair pa02 % [K[?2004hppytest test    [?2004l

[1m======================================================== test session starts ========================================================[0m
platform darwin -- Python 3.8.2, pytest-7.1.1, pluggy-1.0.0
rootdir: /Users/chenmengku/Desktop/COSI/COSI-103A/COSI-103A_PA02/pa02, configfile: pytest.ini
[1mcollecting ... [0m[1m
collected 8 items                                                                                                                   [0m

test_category.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                                                                         [ 50%][0m
test_transaction.py [32m.[0m[32m.[0m[32m.[0m[32m.[0m[32m                                                                                                      [100%][0m

[32m========================================================= [32m[1m8 passed[0m[32m in 0.11s[0m[32m =========================================================[0m
[1m[7m%[27m[1m[0m                                                                                                                                    
 

[0m[27m[24m[Jchenmengku@chenmenggudeair pa02 % [K[?2004hppython3 trak cker.py[?2004l


0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> 9
[{'year': '2017', 'amount': 30.0}, {'year': '2020', 'amount': 41.0}]


year       amount    
------------------------------------------------------------
2017       30        
2020       41        
> 10


category   amount    
------------------------------------------------------------
drink      41        
food       30        
> 11

0. quit
1. show categories
2. add category
3. modify category
4. show transactions
5. add transaction
6. delete transaction
7. summarize transactions by date
8. summarize transactions by month
9. summarize transactions by year
10. summarize transactions by category
11. print this menu

> ^Z
zsh: suspended  python3 tracker.py
[1m[7m%[27m[1m[0m                                                                                                                                    
 

[0m[27m[24m[Jchenmengku@chenmenggudeair pa02 % [K[?2004heexit[?2004l

zsh: you have suspended jobs.
[1m[7m%[27m[1m[0m                                                                                                                                    
 

[0m[27m[24m[Jchenmengku@chenmenggudeair pa02 % [K[?2004heexit[?2004l


Script done on Thu Mar 24 15:16:20 2022

```






