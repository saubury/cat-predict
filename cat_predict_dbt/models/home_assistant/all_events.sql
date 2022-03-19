{{ config(materialized='view') }}

with source_data as (
    select cevt.created_local_hr 
    , cevt.cat_location
    , hevt.indoor_temp, hevt.outside_temp, hevt.outside_humidity
    from {{ ref('cat_events') }} cevt 
    inner join {{ ref('house_events') }} hevt on cevt.created_local_hr = hevt.created_local_hr 
)
select *
from source_data


