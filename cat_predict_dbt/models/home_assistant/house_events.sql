{{ config(materialized='view') }}

with source_data as (
    select created_local_hr
    , round(avg(case when entity_id = 'sensor.study_temperature' then state_numeric end)) as indoor_temp
    , round(avg(case when entity_id = 'sensor.lumi_lumi_weather_b8190707_temperature' then state_numeric end)) as outside_temp
    , round(avg(case when entity_id = 'sensor.lumi_lumi_weather_b8190707_humidity' then state_numeric end)) as outside_humidity
    from {{ ref('state_clean') }}
    where entity_id in ( 'sensor.study_temperature', 'sensor.lumi_lumi_weather_b8190707_humidity', 'sensor.lumi_lumi_weather_b8190707_temperature')
    group by created_local_hr
)
select *
from source_data

