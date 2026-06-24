-- 1 Top 10 Funds by AUM
SELECT scheme_name,
       aum_crore
FROM 07_scheme_performance
ORDER BY aum_crore DESC
LIMIT 10;

-- 2 Average Expense Ratio by Category
SELECT category,
       AVG(expense_ratio_pct) AS avg_expense_ratio
FROM 07_scheme_performance
GROUP BY category
ORDER BY avg_expense_ratio DESC;

-- 3 Top 10 Funds by 5-Year Return
SELECT scheme_name,
       return_5yr_pct
FROM 07_scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 4 Funds with Lowest Expense Ratio
SELECT scheme_name,
       expense_ratio_pct
FROM 07_scheme_performance
ORDER BY expense_ratio_pct ASC
LIMIT 10;

-- 5 Transaction Count by Type
SELECT transaction_type,
       COUNT(*) AS total_transactions
FROM 08_investor_transactions
GROUP BY transaction_type;

-- 6 Total Investment Amount by State
SELECT state,
       SUM(amount_inr) AS total_investment
FROM 08_investor_transactions
GROUP BY state
ORDER BY total_investment DESC;

-- 7 Investment Amount by Gender
SELECT gender,
       SUM(amount_inr) AS total_amount
FROM 08_investor_transactions
GROUP BY gender;

-- 8 Average Investment by City Tier
SELECT city_tier,
       AVG(amount_inr) AS avg_investment
FROM 08_investor_transactions
GROUP BY city_tier;

-- 9 Funds with Highest Sharpe Ratio
SELECT scheme_name,
       sharpe_ratio
FROM 07_scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 10;

-- 10 Risk Grade Distribution
SELECT risk_grade,
       COUNT(*) AS total_funds
FROM 07_scheme_performance
GROUP BY risk_grade
ORDER BY total_funds DESC;
