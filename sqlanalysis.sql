--1. this query mimics the first table in the loops case study, showing a naive analysis of treatment effect

with kpitab as (select treat,
round(avg(kpi)*100,2) as kpi_rate from combined0802 group by treat)
select treat,kpi_rate,
round((kpi_rate-lag(kpi_rate) over(order by treat))/lag(kpi_rate) over(order by treat)*100,2) as kpi_lift
from kpitab order by treat;

--2. this query shows the creation of bias, since intent groups with different kpi rates are distributed differently in control and treatment

select treat,intent, count(*) as cnt,
cast(round((count(*)*1.0)/sum(count(*)) over(partition by treat),2) as decimal(10,1)) as pct_of_treatment_group,
round(avg(kpi)*100,2) as kpi_rate
from combined0802 group by treat,intent
order by treat,intent;

--3. this query is same as last but from the new table, with the correct split in control and treatment of intent
select treat,intent, count(*) as cnt,
cast(round((count(*)*1.0)/sum(count(*)) over(partition by treat),2) as decimal(10,1)) as pct_of_treatment_group
from combined0505 group by treat,intent
order by treat,intent;

--4. this query shows the real kpi lift, showing a positive effect of treatment

with kpitab_05 as (select treat,round(avg(kpi)*100,2) as kpi_rate from combined0505 group by treat)
select treat,kpi_rate,
round((kpi_rate-lag(kpi_rate) over(order by treat))/lag(kpi_rate) over(order by treat)*100,2) as kpi_lift
from kpitab_05 order by treat;

--5. this query compares between the two tables, showing the biad that occured in the original table 

with kpitab as (select treat,
round(avg(kpi)*100,2) as kpi_rate from combined0802 group by treat),
kpitab_05 as (select treat,round(avg(kpi)*100,2) as kpi_rate from combined0505 group by treat)
select
k.treat, k.kpi_rate as kpi_original, k5.kpi_rate as kpi_new
from kpitab k join kpitab_05 k5 on k.treat=k5.treat
order by treat;

--6. this query shows that bias is created when subgroups affect both treatment (incorrect split to control and treatment) and outcome (kpi).
-- in this setup we have two tables (like in the case study) but different intent groups have same effect on kpi, so a different randomization scheme for control and treatment does not produce different results.

select
'original' as test,
cast((sum(case when treat=0 and intent='high' then 1 else 0 end))*1.0/(sum(case when treat=0 then 1 else 0 end)) as decimal(4,2)) as pct_highintent_of_control,
cast((sum(case when treat=1 and intent='high' then 1 else 0 end))*1.0/(sum(case when treat=1 then 1 else 0 end)) as decimal(4,2)) as pct_highintent_of_treat,
cast((sum(case when treat=0 and kpi=1 then 1 else 0 end))*1.0/(sum(case when treat=0 then 1 else 0 end)) as decimal(5,4)) as kpi_control,
cast((sum(case when treat=1 and kpi=1 then 1 else 0 end))*1.0/(sum(case when treat=1 then 1 else 0 end)) as decimal(5,4)) as kpi_treat
from combined_same0802
union
select
'fixed' as test,
cast((sum(case when treat=0 and intent='high' then 1 else 0 end))*1.0/(sum(case when treat=0 then 1 else 0 end)) as decimal(4,2)) as pct_highintent_of_control,
cast((sum(case when treat=1 and intent='high' then 1 else 0 end))*1.0/(sum(case when treat=1 then 1 else 0 end)) as decimal(4,2)) as pct_highintent_of_treat,
cast((sum(case when treat=0 and kpi=1 then 1 else 0 end))*1.0/(sum(case when treat=0 then 1 else 0 end)) as decimal(5,4)) as kpi_control,
cast((sum(case when treat=1 and kpi=1 then 1 else 0 end))*1.0/(sum(case when treat=1 then 1 else 0 end)) as decimal(5,4)) as kpi_treat
from combined_same0505