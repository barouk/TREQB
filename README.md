# TREQB
Time range query builder for Elasticsearch

## Description

Time range query is a challenging issue in Elasticsearch. More specially, when you want to filter documents that their ```@timestamp``` in a specific range in all day or a specific time. 

Unfortunately, Discover tools of the Kibana do not have this feature. To this end, you need scripting into the query. 

This sample code represents the procedure of this work by using Java code embedded in the query script. 
