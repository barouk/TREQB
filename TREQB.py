from elasticsearch import Elasticsearch




es = Elasticsearch(hosts="192.168.13.244", timeout=3000)


start_date = "2021-06-01"
end_date = "2022-12-25"

start_time = "00:00:00"
end_time = "23:59:59"

DateField="@timestamp"

query = {
    'query': {
        'bool': {
            'must': [
                {
                    'bool': {
                        'should': [
                            {
                                'bool': {
                                    'must': [
                                        {'range': {DateField: {
                                            'gte': start_date,
                                            'lte': end_date
                                        }
                                        }
                                        },
                                        {
                                            "bool": {
                                                "filter": {
                                                    "script": {
                                                        "script": """
                                                      ZonedDateTime logdatetime = doc['my_time'].value;
                                                      long log_hour = logdatetime.getHour();
                                                      long log_minute = logdatetime.getMinute();
                                                      long log_second = logdatetime.getSecond();

                                                    String log_time = String.valueOf(log_hour) +":" + String.valueOf(log_minute) + ":" + String.valueOf(log_second);
                                                       DateFormat formatter1 = new SimpleDateFormat("hh:mm:ss");
                                                       Date log_time_obj = formatter1.parse(log_time);
                                                    String str1 = "mystarttime";
                                                    DateFormat formatter2 = new SimpleDateFormat("hh:mm:ss");
                                                    Date date1 = formatter2.parse(str1);

                                                   String str2 = "myendtime";
                                                   DateFormat formatter3 = new SimpleDateFormat("hh:mm:ss");
                                                   Date date2 = formatter3.parse(str2);


                                                       if ( log_time_obj.compareTo(date1) >= 0 && log_time_obj.compareTo(date2) <= 0 ) {
                                                         return true;
                                                       }
                                                       return false;
                                                       """.replace("mystarttime", start_time).
                                                            replace("myendtime", end_time).
                                                            replace('my_time', DateField)
                                                    }
                                                }
                                            }
                                        }

                                    ]
                                }
                            }
                        ],
                        'minimum_should_match': '1'
                    }
                }
            ]
        }
    }
}
import json
print(json.dumps(query))
res=es.search(index="*-raw-*",body=query)['hits']['hits']

print(len(res))
