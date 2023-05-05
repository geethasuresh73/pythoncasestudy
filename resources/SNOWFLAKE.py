create role DBA;
create warehouse Generic;
grant role DBA to role accountadmin;
grant ownership on warehouse Generic to role DBA;
grant ownership on role DBA to role accountadmin;
use role DBA;
use warehouse Generic;
use role accountadmin;
grant create warehouse, create database, create role on account to role DBA;
grant manage grants, monitor usage, manage user support cases on account to role DBA;
grant create integration on account to role DBA;
use role DBA;
create role readonly;
create role readwrite;
create role fullaccess;
grant ownership on role readonly to role DBA;
grant ownership on role readwrite to role DBA;
grant ownership on role fullaccess to role DBA;
grant role readonly to role readwrite;
grant role readwrite to role fullaccess;
grant role fullaccess to role DBA;
create database DBDEMO;
create schema DBDEMO.raw;
create schema DBDEMO.int;
create schema DBDEMO.prs;
use role readonly;
use warehouse Generic;
select * from dbdemo.information_schema.columns;
use role DBA;
grant usage,monitor on warehouse generic to role readonly;
grant monitor, usage on database dbdemo to role readonly;
grant monitor, usage on schema dbdemo.prs to role readonly;
grant monitor, usage on schema dbdemo.int to role readonly;
grant monitor, usage on schema dbdemo.raw to role readonly;

grant select on all tables in schema DBDEMO.prs to role readonly;
grant select on all views in schema DBDEMO.prs to role readonly;
grant select on all external tables in schema DBDEMO.prs to role readonly;
grant usage on all functions in schema DBDEMO.prs to role readonly;
grant select on future tables in schema DBDEMO.prs to role readonly;
grant select on future views in schema DBDEMO.prs to role readonly;
grant select on future external tables in schema DBDEMO.prs to role readonly;
grant usage on future functions in schema DBDEMO.prs to role readonly;

grant select on all tables in schema DBDEMO.raw to role readonly;
grant select on all views in schema DBDEMO.raw to role readonly;
grant select on all external tables in schema DBDEMO.raw to role readonly;
grant usage on all functions in schema DBDEMO.raw to role readonly;
grant select on future tables in schema DBDEMO.raw to role readonly;
grant select on future views in schema DBDEMO.raw to role readonly;
grant select on future external tables in schema DBDEMO.raw to role readonly;
grant usage on future functions in schema DBDEMO.raw to role readonly;

grant select on all tables in schema DBDEMO.int to role readonly;
grant select on all views in schema DBDEMO.int to role readonly;
grant select on all external tables in schema DBDEMO.int to role readonly;
grant usage on all functions in schema DBDEMO.int to role readonly;
grant select on future tables in schema DBDEMO.int to role readonly;
grant select on future views in schema DBDEMO.int to role readonly;
grant select on future external tables in schema DBDEMO.int to role readonly;
grant usage on future functions in schema DBDEMO.int to role readonly;

grant create table, create view, create temporary table on schema DBDEMO.prs to role readwrite;
grant insert, update, truncate, delete on all tables in schema DBDEMO.prs to role readwrite;
grant insert, update, truncate, delete on future tables in schema DBDEMO.prs to role readwrite;
grant usage on all stages in schema DBDEMO.prs to role readwrite;
grant usage on future stages in schema DBDEMO.prs to role readwrite;
grant read, write on all stages in schema DBDEMO.prs to role readwrite;
grant read, write on future stages in schema DBDEMO.prs to role readwrite;
grant usage on all file formats in schema DBDEMO.prs to role readwrite;
grant usage on future file formats in schema DBDEMO.prs to role readwrite;
grant monitor,operate on all tasks in schema DBDEMO.prs to role readwrite;
grant monitor,operate on future tasks in schema DBDEMO.prs to role readwrite;
grant usage on all sequences in schema DBDEMO.prs to role readwrite;
grant usage on future sequences in schema DBDEMO.prs to role readwrite;

grant create table, create view, create temporary table on schema DBDEMO.raw to role readwrite;
grant insert, update, truncate, delete on all tables in schema DBDEMO.raw to role readwrite;
grant insert, update, truncate, delete on future tables in schema DBDEMO.raw to role readwrite;
grant usage on all stages in schema DBDEMO.raw to role readwrite;
grant usage on future stages in schema DBDEMO.raw to role readwrite;
grant read, write on all stages in schema DBDEMO.raw to role readwrite;
grant read, write on future stages in schema DBDEMO.raw to role readwrite;
grant usage on all file formats in schema DBDEMO.raw to role readwrite;
grant usage on future file formats in schema DBDEMO.raw to role readwrite;
grant monitor,operate on all tasks in schema DBDEMO.raw to role readwrite;
grant monitor,operate on future tasks in schema DBDEMO.raw to role readwrite;
grant usage on all sequences in schema DBDEMO.raw to role readwrite;
grant usage on future sequences in schema DBDEMO.raw to role readwrite;

grant create table, create view, create temporary table on schema DBDEMO.int to role readwrite;
grant insert, update, truncate, delete on all tables in schema DBDEMO.int to role readwrite;
grant insert, update, truncate, delete on future tables in schema DBDEMO.int to role readwrite;
grant usage on all stages in schema DBDEMO.int to role readwrite;
grant usage on future stages in schema DBDEMO.int to role readwrite;
grant read, write on all stages in schema DBDEMO.int to role readwrite;
grant read, write on future stages in schema DBDEMO.int to role readwrite;
grant usage on all file formats in schema DBDEMO.int to role readwrite;
grant usage on future file formats in schema DBDEMO.int to role readwrite;
grant monitor,operate on all tasks in schema DBDEMO.int to role readwrite;
grant monitor,operate on future tasks in schema DBDEMO.int to role readwrite;
grant usage on all sequences in schema DBDEMO.int to role readwrite;
grant usage on future sequences in schema DBDEMO.int to role readwrite;

grant ownership on all tables in schema DBDEMO.prs to role fullaccess;
grant ownership on all views in schema DBDEMO.prs to role fullaccess;
grant ownership on all file formats in schema DBDEMO.prs to role fullaccess;
grant ownership on all sequences in schema DBDEMO.prs to role fullaccess;
grant ownership on all streams in schema DBDEMO.prs to role fullaccess;
grant ownership on all tasks in schema DBDEMO.prs to role fullaccess;
grant ownership on all functions in schema DBDEMO.prs to role fullaccess;
grant ownership on all external tables in schema DBDEMO.prs to role fullaccess;
grant ownership on future tables in schema DBDEMO.prs to role fullaccess;
grant ownership on future views in schema DBDEMO.prs to role fullaccess;
grant ownership on future file formats in schema DBDEMO.prs to role fullaccess;
grant ownership on future sequences in schema DBDEMO.prs to role fullaccess;
grant ownership on future streams in schema DBDEMO.prs to role fullaccess;
grant ownership on future tasks in schema DBDEMO.prs to role fullaccess;
grant ownership on future functions in schema DBDEMO.prs to role fullaccess;
grant ownership on future external tables in schema DBDEMO.prs to role fullaccess;
grant create external table on schema DBDEMO.prs to role fullaccess;
grant create materialized view, create file format, create sequence, create function, create pipe, create stream, create task, create procedure on schema DBDEMO.prs to role fullaccess;
grant references on all tables in schema DBDEMO.prs to role fullaccess;
grant references on future tables in schema DBDEMO.prs to role fullaccess;
grant all privileges on all file formats in schema DBDEMO.prs to role fullaccess;
grant all privileges on future file formats in schema DBDEMO.prs to role fullaccess;
grant select on all streams in schema DBDEMO.prs to role fullaccess;
grant select on future streams in schema DBDEMO.prs to role fullaccess;

grant ownership on all tables in schema DBDEMO.raw to role fullaccess;
grant ownership on all views in schema DBDEMO.raw to role fullaccess;
grant ownership on all file formats in schema DBDEMO.raw to role fullaccess;
grant ownership on all sequences in schema DBDEMO.raw to role fullaccess;
grant ownership on all streams in schema DBDEMO.raw to role fullaccess;
grant ownership on all tasks in schema DBDEMO.raw to role fullaccess;
grant ownership on all functions in schema DBDEMO.raw to role fullaccess;
grant ownership on all external tables in schema DBDEMO.raw to role fullaccess;
grant ownership on future tables in schema DBDEMO.raw to role fullaccess;
grant ownership on future views in schema DBDEMO.raw to role fullaccess;
grant ownership on future file formats in schema DBDEMO.raw to role fullaccess;
grant ownership on future sequences in schema DBDEMO.raw to role fullaccess;
grant ownership on future streams in schema DBDEMO.raw to role fullaccess;
grant ownership on future tasks in schema DBDEMO.raw to role fullaccess;
grant ownership on future functions in schema DBDEMO.raw to role fullaccess;
grant ownership on future external tables in schema DBDEMO.raw to role fullaccess;
grant create external table on schema DBDEMO.raw to role fullaccess;
grant create materialized view, create file format, create sequence, create function, create pipe, create stream, create task, create procedure on schema DBDEMO.raw to role fullaccess;
grant references on all tables in schema DBDEMO.raw to role fullaccess;
grant references on future tables in schema DBDEMO.raw to role fullaccess;
grant all privileges on all file formats in schema DBDEMO.raw to role fullaccess;
grant all privileges on future file formats in schema DBDEMO.raw to role fullaccess;
grant select on all streams in schema DBDEMO.raw to role fullaccess;
grant select on future streams in schema DBDEMO.raw to role fullaccess;

grant ownership on all tables in schema DBDEMO.int to role fullaccess;
grant ownership on all views in schema DBDEMO.int to role fullaccess;
grant ownership on all file formats in schema DBDEMO.int to role fullaccess;
grant ownership on all sequences in schema DBDEMO.int to role fullaccess;
grant ownership on all streams in schema DBDEMO.int to role fullaccess;
grant ownership on all tasks in schema DBDEMO.int to role fullaccess;
grant ownership on all functions in schema DBDEMO.int to role fullaccess;
grant ownership on all external tables in schema DBDEMO.int to role fullaccess;
grant ownership on future tables in schema DBDEMO.int to role fullaccess;
grant ownership on future views in schema DBDEMO.int to role fullaccess;
grant ownership on future file formats in schema DBDEMO.int to role fullaccess;
grant ownership on future sequences in schema DBDEMO.int to role fullaccess;
grant ownership on future streams in schema DBDEMO.int to role fullaccess;
grant ownership on future tasks in schema DBDEMO.int to role fullaccess;
grant ownership on future functions in schema DBDEMO.int to role fullaccess;
grant ownership on future external tables in schema DBDEMO.int to role fullaccess;
grant create external table on schema DBDEMO.int to role fullaccess;
grant create materialized view, create file format, create sequence, create function, create pipe, create stream, create task, create procedure on schema DBDEMO.int to role fullaccess;
grant references on all tables in schema DBDEMO.int to role fullaccess;
grant references on future tables in schema DBDEMO.int to role fullaccess;
grant all privileges on all file formats in schema DBDEMO.int to role fullaccess;
grant all privileges on future file formats in schema DBDEMO.int to role fullaccess;
grant select on all streams in schema DBDEMO.int to role fullaccess;
grant select on future streams in schema DBDEMO.int to role fullaccess;

use role accountadmin;
create resource monitor DEMO_MONITOR with credit_quota=2 frequency=weekly start_timestamp=immediately triggers on 75 percent do notify on 95 percent do suspend_immediate;


show resource monitors;
show warehouses;
alter warehouse Generic set resource_monitor="DEMO_MONITOR";

use role readonly;
use database DBDEMO;
use schema DBDEMO.raw;

create table temp as select * from snowflake.account_usage.roles;
select * from temp;
use role accountadmin;
select * from snowflake.account_usage.query_history;
use schema snowflake.account_usage;
select query_type, sum(credits_used_cloud_services) cs_credits, count(1) num_queries
from query_history
where true
and start_time >= timestampadd(day, -10, current_timestamp)
group by 1
order by 2 desc
limit 10;

-- Find warehouses that consume the most cloud services credits
select warehouse_name,
       sum(credits_used_cloud_services) credits_used_cloud_services,
       sum(credits_used_compute) credits_used_compute,
   sum(credits_used) credits_used
from warehouse_metering_history
where true
  and start_time >= timestampadd(day, -10, current_timestamp)
group by 1
order by 2 desc
limit 10;


