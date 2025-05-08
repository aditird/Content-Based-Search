from opensearchpy import OpenSearch
from opensearchpy.helpers import bulk

auth = ('<username>', '<password>')

# Initialize OpenSearch client
client = OpenSearch(
    hosts=[{'host': '<host>', 'port': '<port>'}],
    use_ssl=True,
    verify_certs=True,
    http_auth = auth,
)
def bulk_index_data(metadata):
    """
    Bulk index metadata into OpenSearch.
    """
    actions = []
    for record in metadata:
        action = {
            "_op_type": "index",
            "_index": "image_metadata",  # Index name in OpenSearch
            "_id": record['image_id'],  # Unique ID for each image
            "_source": {
                "image_id": record['image_id'],
                "label": record['label'],
                "text_detected": record['text_detected'],
                "image_url": record['image_url']
            }
        }
        actions.append(action)
    bulk(client, actions)

def search_images(query):
    """
    Search OpenSearch for images based on a query (label).
    """
    response = client.search(
        index="image_metadata",  # The index name in OpenSearch
        body={
            "query": {
                "match": {
                    "label": query  # Searching for the specified query in labels
                }
            }
        }
    )
    return response['hits']['hits']  # Return the search results
