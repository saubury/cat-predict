{{ config(materialized='table') }}

with source_data as (
    select date_trunc('hour', s.created) as created_local_hr
    , s.created as created_local
    , s.created 
    , s.entity_id
    , s.state
    , CASE WHEN state~E'^[0-9\.]*$' THEN to_number(state, '999.9')  ELSE null END as state_numeric
    from hass_schema.states s
    where s.state != 'unavailable'
)
select *
from source_data

