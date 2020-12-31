import elasticsearch as es
from datetime import datetime as dt

class es_connect:
    def get_connection(api_key=None,
                       api_id=None,
                       elasticsearch_host='127.0.0.1',
                       timeout=None, http_user='elastic',
                       http_password=None):
        """Create a new connection to an Elasticsearch host to use for interacting with Elasticsearch.

        Keyword arguments:
        api_key -- the Elasticsearch API key you wish to use to authenticate to Elasticsearch. (default None)
        api_id -- the Elasticsearch API ID you wish to use to authenticate to Elasticsearch. (default None)
        elasticsearch_host -- the Elasticsearch host you wish to connect to. make sure to specify the hostname or IP of your Elasticsearch host here. (default '127.0.0.1')
        timeout -- set a timeout, in case you need to run queries that exceed the default timeout. (default None)
        http_user -- set the username to use when authenticating to Elasticsearch over HTTP. (default 'elastic')
        http_password -- set the password to use with authenticating to Elasticsearch over HTTP. (default None)"""
        es_connection = es.Elasticsearch([elasticsearch_host],
                                         api_key=(api_key,
                                                  api_id),
                                         timeout=timeout,
                                         http_auth=(http_user,
                                                    http_password)
                                         )
        return es_connection
class es_read:
    class classic:

        def read(connection=None,
                 index='qbitkit-*',
                 query={"query": {"match_all": {}}}
                 ):
            """Read a document from the specified index using the specified query against the specified Elasticsearch host.

            Keyword arguments:
            index -- set the index template for which to use to read data from. (default 'qbitkit-*')
            query -- set the query to run against the specified Elasticsearch host. (default {"query": {"match_all": {}}})"""
            return None
class es_write:
    class classic:

        def write(connection=None,
                 index='qbitkit-*',
                 doc=None):
            """Add a timestamp field with the current time and date to a new query containing specified data, sends the query to the specified Elasticsearch host, and returns the result of the indexing query.

            Keyword arguments:
            connection -- specify a connection to use when communicating with the Elasticsearch host. (default es_connect.get_connection())
            index -- specify the index template to use when writing to Elasticsearch. (defaul"""
            result = {'timestamp' : str(dt.now()),
                   }
            print(result)
            return result