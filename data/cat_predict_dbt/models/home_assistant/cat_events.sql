{{ config(materialized='view') }}

with cte AS 
(
	select created_local_hr
	, state
	, count(*)
	, ROW_NUMBER() OVER (PARTITION BY created_local_hr ORDER BY COUNT(*) DESC) rn
	from {{ ref('state_clean') }}
	where entity_id = 'sensor.snowy_tile'
	group by created_local_hr, state
)
--
select created_local_hr, state as cat_location
from cte
where rn=1

