import elasticsearch as es
from datetime import datetime as dt

class util:
    def auto_ilm(index='qbitkit',
                 strftime='%Y-%m-%d'):
        """Automatically generates an index name for Elasticsearch to use when logging data to Elasticsearch. Doing this allows users to set up Index Lifecycle Management within Elasticsearch to define what happens to data past pre-defined retention periods.

        Args:
            index (str): an Elasticsearch index to append formatted timestamp to (default 'qbitkit')
            strftime (str): strftime formatting to use when representing timestamp in index name
        Returns:
            str: index template formatted for ILM"""
        date = dt.now().strftime(strftime)
        ilm_index=f"{index}-{date}"
        return ilm_index


class es_connect:
    def using_api_key(api_key=None,
                      api_id=None,
                      elasticsearch_host='127.0.0.1',
                      timeout=60):
        """Connect to Elasticsearch using an elasticsearch API key and API ID. To learn how to generate API keys to authenticate to Elasticsearch, refer to Elastic's documentation regarding using API keys: https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-create-api-key.html

        Args:
            api_key (str): The API key for authenticating to Elasticsearch. (default None)
            api_id (str): The API ID for authenticating to Elasticsearch. (default None)
            elasticsearch_host (str): The hostname or IP address of the Elasticsearch server you are trying to authenticate to. (default '127.0.0.1')
            timeout (int): The timeout in seconds to use when waiting for the Elasticsearch server to respond. (default 60)"""
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

        Args:
            username (str): The username you would like to use when connecting to Elasticsearch with HTTP authentication. (default 'elastic')
            password (str): The password you would like to use when connecting to Elasticsearch with HTTP authentication. (default None)
            elasticsearch_host (str) The hostname or IP address of the Elasticsearch server you are trying to authenticate to. (default '127.0.0.1')
            timeout (int) The timeout in seconds to use when waiting for the Elasticsearch server to respond. (default 60)
        Returns:
            elasticsearch.Elasticsearch: Elasticsearch connection object for reading/writing data to Elasticsearch"""
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

        Args:
            api_key (str): the Elasticsearch API key you wish to use to authenticate to Elasticsearch. (default None)
            api_id (str): the Elasticsearch API ID you wish to use to authenticate to Elasticsearch. (default None)
            elasticsearch_host (str): the Elasticsearch host you wish to connect to. make sure to specify the hostname or IP of your Elasticsearch host here. (default '127.0.0.1')
            timeout (int): set a timeout, in case you need to run queries that exceed the default timeout. (default None)
            http_user (str): set the username to use when authenticating to Elasticsearch over HTTP. (default 'elastic')
            http_password (str) set the password to use with authenticating to Elasticsearch over HTTP. (default None)
        Returns:
            dict: The Elasticsearch connection generated from specified keyword parameters"""
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

            Args:
                index (str): set the index template for which to use to read data from. (default 'qbitkit-*')
                query (str): set the query to run against the specified Elasticsearch host. (default {"query": {"match_all": {}}})
            Returns:
                dict: Response from Elasticsearch to the query you send it."""
            res = connection.search(index=index,
                                    body=query)
            return res


class es_write:
    class classic:

        def write(connection=None,
                 index=util.auto_ilm(),
                 doc=None,
                 refresh=True):
            """Sends the query to the specified Elasticsearch host, and returns the result of the indexing query we sent.

            Args:
                connection (dict): specify a connection to use when communicating with the Elasticsearch host. (default es_connect.get_connection())
                index (str): specify the index template to use when writing to Elasticsearch. (default util.auto_ilm())
                refresh (bool): when set to True, Elasticsearch will immediately refresh indices after we write to it. This makes documents available to search queries as soon as we send them to Elasticsearch. (default True)
            Returns:
                dict: the response from the query we sent Elasticsearch"""
            result = connection.index(index=index,
                                      body=doc)
            if refresh == True:
                connection.indices.refresh(index=index)
            print(result)
            return result