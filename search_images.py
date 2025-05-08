from opensearch_utils import search_images

def search_images_by_query(query):
    """
    Search OpenSearch for images based on a query (label or text).
    """
    search_results = search_images(query)
    return search_results

def main():
    # Example query to search for images containing the label "dog"
    query = 'group of people'
    search_results = search_images_by_query(query)

    # Print search results
    if search_results:
        for result in search_results:
            print(f"Image ID: {result['_source']['image_id']}, Image URL: {result['_source']['image_url']}")
    else:
        print("No results found.")

if __name__ == '__main__':
    main()
