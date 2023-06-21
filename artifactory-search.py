import requests

base_url = 'https://your-artifactory-instance.com/artifactory'
repository_name = 'your-repository-name'
api_key = 'your-api-key'

search_url = f'{base_url}/api/search/artifact?name=*.jar&repos={repository_name}'

response = requests.get(search_url, headers={'X-JFrog-Art-Api': api_key})
search_results = response.json()

jar_files_over_100mb = []

for result in search_results['results']:
    file_url = f"{base_url}/api/storage/{repository_name}/{result['path']}"
    response = requests.get(file_url, headers={'X-JFrog-Art-Api': api_key})
    file_metadata = response.json()
    
    file_size_bytes = file_metadata['size']
    file_size_mb = file_size_bytes / (1024 * 1024)
    
    if file_size_mb > 100:
        jar_files_over_100mb.append(result['path'])

print(jar_files_over_100mb)
