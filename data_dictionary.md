# Mutual Fund Analytics Data Dictionary


# 07_scheme_performance table

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | Integer | Unique AMFI fund code |
| scheme_name | Text | Name of mutual fund scheme |
| fund_house | Text | Fund management company |
| category | Text | Fund category |
| plan | Text | Regular or Direct plan |
| return_1yr_pct | Decimal | 1 year return (%) |
| return_3yr_pct | Decimal | 3 year return (%) |
| return_5yr_pct | Decimal | 5 year return (%) |
| benchmark_3yr_pct | Decimal | Benchmark return (%) |
| alpha | Decimal | Alpha performance measure |
| beta | Decimal | Beta risk measure |
| sharpe_ratio | Decimal | Risk-adjusted return |
| sortino_ratio | Decimal | Downside risk-adjusted return |
| std_dev_ann_pct | Decimal | Annual volatility |
| max_drawdown_pct | Decimal | Maximum loss from peak |
| aum_crore | Decimal | Assets Under Management |
| expense_ratio_pct | Decimal | Expense ratio (%) |
| morningstar_rating | Integer | Morningstar rating |
| risk_grade | Text | Risk category |

# 08_investor_transactions table

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| investor_id | Integer | Unique investor ID |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Fund AMFI code |
| transaction_type | Text | SIP, Lumpsum, Redemption |
| amount_inr | Decimal | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| city_tier | Text | Tier 1, Tier 2, Tier 3 city |
| age_group | Text | Investor age group |
| gender | Text | Male/Female |
| annual_income_lakh | Decimal | Annual income |
| payment_mode | Text | UPI, Net Banking, Card etc |
| kyc_status | Text | Verified/Pending/Rejected |

# nav_history

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | Integer | Fund code |
| date | Date | NAV date |
| nav | Decimal | Net Asset Value |
