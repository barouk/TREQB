# TREQB
Time range query builder for Elasticsearch

## Description

Time range query is a challenging issue in the Elasticsearch. More specially, when you want filtering the documents that their ```@timestamp``` in a specific range in all day or specific time. 

Unfortunatly, Discover tools of the Kibana does not have this feature. To this end, you need scripting into the query. 

This sample code represents the procedure of this work by using Java code embedded in the query script. 
