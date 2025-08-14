{{ config(
    materialized='table'
) }}

with source as(
     select*
     from {{ source('dev', 'data') }}
)

select 
  id,
  city,
  temperature,
  wind_speed,
  pressure

from source


