import elasticsearch as es
from datetime import datetime as dt
from qbitkit.error import error as qbitkit_error

def get_support_status(self):
    elasticsearch_support_status = 'experimental'
    qbitkit_error.errors.experimental_feature(feature_state=elasticsearch_support_status,
                                              resource_name='Elasticsearch',
                                              additional_notes='For more information on forthcoming Elasticsearch support, see https://github.com/brianlechthaler/qbitkit/issues/4')
    return elasticsearch_support_status

get_support_status()

class es_connect:
    def using_api_key(api_key=None,
                      api_id=None,
                      elasticsearch_host='127.0.0.1',
                      timeout=60):
        """Connect to Elasticsearch using an elasticsearch API key and API ID. To learn how to generate API keys to authenticate to Elasticsearch, refer to Elastic's documentation regarding using API keys: https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html

        Keyword arguments:
        api_key -- The API key for authenticating to Elasticsearch. (default None)
        api_id -- The API ID for authenticating to Elasticsearch. (default None)
        elasticsearch_host -- The hostname or IP address of the Elasticsearch server you are trying to authenticate to. (default '127.0.0.1')
        timeout -- The timeout in seconds to use when waiting for the Elasticsearch server to respond. (default 60)"""
        es_connection = es.Elasticsearch([elasticsearch_host],
                                        api_key=(api_key,
                                                 api_id),
                                         timeout=timeout)
        return es_connection
    def using_http_auth(username='elastic',
                        password=None,
                        elasticsearch_host='127.0.0.1',
                        timeout=60):
        """Connect to Elasticsearch using an Elasticsearch HTTP username and password. To learn how to generate API keys to authenticate to Elasticsearch, refer to Elastic's documentation regarding using API keys: https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html

        Keyword arguments:
        username -- The username you would like to use when connecting to Elasticsearch with HTTP authentication. (default 'elastic')
        password -- The password you would like to use when connecting to Elasticsearch with HTTP authentication. (default None)
        elasticsearch_host -- The hostname or IP address of the Elasticsearch server you are trying to authenticate to. (default '127.0.0.1')
        timeout -- The timeout in seconds to use when waiting for the Elasticsearch server to respond. (default 60)"""
        es_connection = es.Elasticsearch([elasticsearch_host],
                                         http_auth=(username,
                                                    password),
                                         timeout=timeout)
        return es_connection
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