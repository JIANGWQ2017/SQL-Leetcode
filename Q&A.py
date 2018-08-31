'''
QUESTION 1 : 
	output the distinct second highest salary if there is no second highest 
	out null instead 
	
points: output null not empty []	
ANSWER 1 :
	select(
	select distinct salary from employee 
	order by salary desc
	limit 1 offset 1
	) as SecondHighestSalary


	
	
QUESTION 2:
	output employee name whos salary is greater than his/her manager
	
points: correlated subquery 
ANSWER: 
	select name as Employee from employee as e1
	where salary > (
	select salary from employee as e2 
    where e1.managerid = e2.id
	)
	



	
QUESTION 3:
	REPORT EMAIL ADDRESS THAT ARE DUPLICATED
	
POINTS: GROUP BY AND HAVING CLAUSE
ANSWER: 
	SELECT EMAIL FROM PERSON 
	GROUP BY EMAIL HAVING COUNT(EMAIL)>1





QUESTION 4:
	FIND THE DATE WHOSE TEMPERATURE IS HIGHER THAN IT IS YESTERDAY 
POINTS : (DATE) DATATYPE, AND DATEDIFF FUNCTION 
ANSWER : 
	select w1.id from weather as w1,weather as w2
	where datediff(w1.recorddate,w2.recorddate)=1
	and w1.temperature> w2.temperature 





QUESTION 5:
	SWAP F(FEMALE) TO M(MALE) AND VICE VISA
POINTS:  SIMPLE CASE FUNCTION 
ANSWER: 
	update salary
	set sex = case sex when 'f' then 'm' else 'f' end 




QUESTION 6:
	DEFINE A FUNCTION TO FIND OUT THE Nth HIGHEST SALARY OF THE EMPLOYEES IF THERE IS NO Nth Highest slary 
	it should return null
points :    self_defined function ; the use of having 
ANSWER: 
	create function getNthHighestSalary(N int)
	begin
		return (
	select min(t.salary) from (
	select distinct salary from employee 
	order by salary desc 
	limit N 
	)as t
	having count(*) =N               # having clause filter the situation where N> num of distinct salary 
	)
	end





QUESTION 7:
	GIVEN SEVERAL SCORES IN A TABLE, SOME SCORES ARE DUPLICATED , RETURN THE TABLE CONTAINS SCORES AND IT CORRESPONSE RANK, IF MULTIPLE SCORES ARE THE SAME 
	THEM HAVE THE SAME RANK AND THE NEXT SCORE RANK THE CONSECUTIVE NUM
POINTS: HOW TO GET RANK £¨using count() function£© a score rank first if and only if count( other scores > target score)=0 . some sort of correlated subquery
ANSWER: 
	select score , 1+(select count(*) from (select distinct scores from scores order by score desc)as s2 where s2.score>s1.score)
	from scores as s1
	order by score desc

	
	
	
QUESTION 8:
	FIND THE NUMBER THAT OCCUR CONSECUTIVELY FOR MORE THAN 3 TIMES 
POINTS :  SELF JOIN TWICE TIMES/ write 
ANSWER: 
	answer 1 : 
		select distinct l3.num from `logs` as l1
		inner join `logs` as l2 
		where l1.id = l2.id+1 and l1.num = l2.num
		inner join `logs` as l3
		where l1.id = l3.id+2 and l1.num = l3.num
		
	answer 2:
		select distinct l3.num as consecutivenums from `logs` as l1,`logs`as l2, `logs` as l3
		where l1.id = l2.id+1 and l2.num = l1.num and l3.id +2= l1.id and l3.num = l1.num
		
'''
