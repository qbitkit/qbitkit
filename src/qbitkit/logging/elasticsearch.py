import elasticsearch as es
from datetime import datetime as dt
class es_connect:
    def get_connection(api_key=None,
                       api_id=None,
                       elasticsearch_host='127.0.0.1',
                       timeout=None, http_user='elastic',
                       http_password=None):
        es_connection = es.Elasticsearch([elasticsearch_host],
                                         api_key=(api_key,
                                                  api_id),
                                         timeout=timeout,
                                         http_auth=(http_user,
                                                    http_password)
                                         )
        return es_connection
class es_read:
    def read(connection=es_connect.get_connection(),
             index='qbitkit-*',
             query={"query": {"match_all": {}}}
             ):
        return None
class es_doc:
    def doc(qpu_sampling_time=None,
            qpu_access_times=None,
            qpu_programming_times=None,
            qpu_anneal_time_per_samples=None,
            results=None):
        {
            'timestamp': str(dt.now()),
            'qpu_access_times' : qpu_access_times,
            'qpu_programming_times' : qpu_programming_times,
            'qpu_anneal_time_per_samples' : qpu_anneal_time_per_samples,
            'results' : results,
        }
class es_write:
    def write(connection=es_connect.get_connection(),
             index='qbitkit-*',
             doc=None):
        result = {'timestamp' : str(dt.now()),
               }
        print(result)
        return result