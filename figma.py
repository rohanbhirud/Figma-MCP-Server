import os
import requests
from urllib.parse import urlparse, parse_qs
from dotenv import load_dotenv

load_dotenv(".env")

def parse_figma_url(url):
    parsed = urlparse(url)
    path_parts = parsed.path.strip('/').split('/')
    file_key = path_parts[1] if len(path_parts) > 1 else None
    query = parse_qs(parsed.query)
    node_id = query.get('node-id', [None])[0]
    return file_key, node_id

def get_figma_token():
    return os.getenv("FIGMA_TOKEN")

def set_figma_token(token: str):
    """Set the Figma token in the environment for the current process."""
    os.environ["FIGMA_TOKEN"] = token

def get_file(file_key: str):
    url = f"https://api.figma.com/v1/files/{file_key}"
    headers = {"X-Figma-Token": get_figma_token()}
    response = requests.get(url, headers=headers, verify=False)
    return response.json()

def get_node(file_key: str, node_id: str):
    url = f"https://api.figma.com/v1/files/{file_key}/nodes?ids={node_id}"
    headers = {"X-Figma-Token": get_figma_token()}
    response = requests.get(url, headers=headers, verify=False)
    return response.json()

def get_file_from_url(figma_url: str):
    file_key, _ = parse_figma_url(figma_url)
    return get_file(file_key)

def get_node_from_url(figma_url: str):
    file_key, node_id = parse_figma_url(figma_url)
    return get_node(file_key, node_id)
