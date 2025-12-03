# -*- coding: utf-8 -*-
# @Time    : 2024/06/27
# @Author  : Derek

import logging
from .base import Client
from .config import ConfigurationManager
from .constants import *

config_manager = ConfigurationManager()

## add default config
config_manager.configure(name="deepnlp", endpoint="http://www.deepnlp.org/api/mcp_marketplace/v1")
config_manager.configure(name="pulsemcp", endpoint="https://api.pulsemcp.com/v0beta/servers")
config_manager.configure(name="deepnlp_tool", endpoint="http://www.deepnlp.org/api/mcp_marketplace/v1/tools")
config_manager.configure(name="deepnlp_server", endpoint="http://www.deepnlp.org/api/mcp_marketplace/v1/server")

_default_client = Client()

DEFAULT_CONFIG_NAME = "deepnlp"

def set_endpoint(config_name="", url=""):
    config = config_manager.get_config(config_name)
    if config is not None:
        _default_client.set_endpoint(config.endpoint)
    else:
        _default_client.set_endpoint(url)

def set_endpoint_from_params(params):
    """ Check if params contains config keys
    """
    if KEY_CONFIG_NAME in params or KEY_URL in params:
        config_name = params[KEY_CONFIG_NAME] if KEY_CONFIG_NAME in params else ""
        url = params[KEY_URL] if KEY_URL in params else ""
        set_endpoint(config_name, url)
    else:
        # without setting endpoint using defaujt
        set_endpoint(DEFAULT_CONFIG_NAME, "")

def get(resource_id, **params):
    set_endpoint_from_params(params)
    return _default_client.get(resource_id)

def create(data, **params):
    return _default_client.create(data)

def delete(resource_id, **params):
    set_endpoint_from_params(params)
    return _default_client.delete(resource_id)

def list(**params):
    set_endpoint_from_params(params)
    return _default_client.list(**params)

def search(**query_params):
    set_endpoint_from_params(query_params)
    print('GET Endpoint %s' % _default_client.endpoint)
    return _default_client.search(**query_params)

def search_batch(query_params_list):
    if len(query_params_list) > 0:
        set_endpoint_from_params(query_params_list[0])
    print('GET Endpoint %s' % _default_client.endpoint)        
    return _default_client.search_batch(query_params_list)

def list_tools(**params):
    """ assembly config and client
    """
    set_endpoint_from_params(params)
    print('GET Endpoint %s' % _default_client.endpoint)    
    return _default_client.list_tools(**params)

def list_tools_batch(query_params_list):
    if len(query_params_list) > 0:
        set_endpoint_from_params(query_params_list[0])
    print('GET Endpoint %s' % _default_client.endpoint)        
    return _default_client.list_tools_batch(query_params_list)

def load_config_batch(server_ids, **params):
    set_endpoint_from_params(params)
    print('GET Endpoint %s' % _default_client.endpoint)    
    return _default_client.load_config_batch(server_ids, **params)


import os
import requests
import json
import uuid
from dotenv import load_dotenv
import os

load_dotenv()

KEY_DEEPNLP_ONEKEY_ROUTER_ACCESS = "DEEPNLP_ONEKEY_ROUTER_ACCESS"
DEFAULT_ENDPOINT = "https://agent.deepnlp.org/mcp"

# --- Helper Functions (Mocking the expected JSON-RPC structure for client-side) ---
def build_rpc_payload(method: str, params: dict = None, request_id: str = None) -> dict:
    """Constructs the JSON-RPC payload for the request."""
    if request_id is None:
        # Generate a unique ID if one is not provided, mimicking the curl example's explicit IDs.
        request_id = str(uuid.uuid4()).replace('-', '')[:8]

    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "id": request_id,
    }
    if params is not None:
        payload["params"] = params

    return payload

# --- MCPOneKeyRouter Class Implementation ---
class OneKeyMCPRouter:

    def __init__(self, server_name: str="", onekey: str = None, endpoint: str = None, log_enable:bool=False):
        """
        Initializes the router client and validate if onekey has gain access or enough credit to connect to mcp server by server_name
        Args:
            onekey: The access key. Falls back to environment variable or default.
            server_name: The MCP Server Name that the Routers wants to connect, e.g. google-maps,perplexity,etc.
            endpoint: The base URL for the MCP router. Falls back to DEFAULT_ENDPOINT.
        """
        if server_name is None or server_name == "":
            print(f"MCPOneKeyRouter init MCP Server Name server_name cannot be empty.")
            return
        self.server_name = server_name
        self.endpoint = endpoint or DEFAULT_ENDPOINT
        access_key = os.getenv(KEY_DEEPNLP_ONEKEY_ROUTER_ACCESS) or onekey
        if access_key is None or access_key == "":
            raise ValueError(f"Error: MCPOneKeyRouter init OneKey access_key is missing None. Please Check Env Variable DEEPNLP_ONEKEY_ROUTER_ACCESS or parameter onekey")
        self.onekey = access_key
        self._request_id_counter = 0
        self.log_enable = log_enable
        ## Initialization
        self.initialize(self.server_name, self.onekey)

    def _get_next_id(self):
        """Generates a sequential ID for JSON-RPC requests."""
        self._request_id_counter += 1
        return str(self._request_id_counter)

    def _make_request(self, server_name: str, method: str, params: dict = None, request_id: str = None) -> dict:
        """
        Generic method to handle the POST request to the MCP endpoint.
        """

        # Build the final URL with query parameters
        final_url = f"{self.endpoint}?server_name={server_name}&onekey={self.onekey}"

        # Build the JSON-RPC payload
        payload = build_rpc_payload(
            method=method,
            params=params,
            request_id= request_id or self._get_next_id()
        )
        if self.log_enable:
            print(f"DEBUG: Initializing Request {payload}|server_name {server_name}|method {method}|params {params}|final_url {final_url}")
        try:
            # Perform the POST request
            response = requests.post(
                final_url,
                headers={"Content-Type": "application/json"},
                json=payload
            )
            response.raise_for_status()
            return {"status": True, "response": response, "message": "OK"}

        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP Error: {e.response.status_code} - {e.response.text}")
            return {"status": False, "response": None, "message": f"HTTP Error: {e.response.status_code}"}
        except requests.exceptions.RequestException as e:
            logging.error(f"Request failed: {e}")
            return {"status": False, "response": None, "message": f"Request Error: {e}"}
        except json.JSONDecodeError:
            logging.error(f"Failed to decode JSON response: {response.text}")
            return {"status": False, "response": None, "message": "Invalid JSON response from server"}
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            return {"status": False, "response": None, "message": str(e)}

    def initialize(self, server_name:str, access_key: str):
        """
        Registers the access key with the server to get a credential.
        The server code shows a special path for the 'initialize' method.

            Successfully initialized the access key.
            result:
                {"jsonrpc": "2.0", "result": {"protocolVersion": "2025-06-18", "capabilities": {"toolDiscovery": {"listTools": {"httpUrl": "/mcp?server_name=your_server_name&onekey=your_access_key"}}, "streamableHttp": true, "tools": {"listChanged": false}}, "serverInfo": {"name": "Your DeepNLP OneKey MCP Router", "version": "1.0.0"}}, "id": "1"
        """
        if self.log_enable:
            print(f"Attempting to initialize client with server_name {server_name} and key {access_key}")
        result = self._make_request(
            server_name=server_name,
            method="initialize",
            params={"access_key": access_key},  # Parameters might be ignored by server logic, but sent anyway
            request_id=self._get_next_id()  # Use a unique ID
        )
        if self.log_enable:
            print (f"Result initialize server {server_name} make request {result}")
        status = result.get("status", False)
        if status:
            response = result.get("response", None)
            if response:
                logging.info(f"POST initialize server_name {server_name} successful, response: {response.status_code}")
            else:
                logging.error(f"POST initialize server_name {server_name} failed response is None..")
        else:
            logging.error(f"POST initialize server_name {server_name} failed with error")

    def tools_list(self, server_name: str, **kwargs):
        """
        Lists available tools on the target server.
        Matches the Tool1 curl command: '{"id": "1", "method": "tools/list"}'

        Args:
            response_json: Dict, the original Json RPC Result
        """
        if self.log_enable:
            print(f"Requesting tool list for server: {server_name}")
        # The params dictionary is empty for tools/list in the curl example
        response_json = {}
        try:
            result = self._make_request(
                method="tools/list",
                server_name = server_name,
                params=kwargs,  # Pass kwargs if the user provides any, otherwise it's {}
                request_id=self._get_next_id()
            )
            status = result.get("status", False)
            if status:
                response = result.get("response", None)
                if response:
                    response_json = response.json()
                else:
                    logging.error(f"GET server_name {server_name} tool list response is None")
            else:
                response_json = {}
            return response_json

        except Exception as e:
            logging.error(f"Failed to get tool list: {e}")
            return {}

    def tools_call(self, server_name:str, tool_name: str, arguments: dict):
        """
        Performs a tool call to the router.
        Matches the tool/call curl command structure.

        Args:
            name: The name of the tool to call (e.g., 'maps_directions').
            arguments: The arguments for the tool (e.g., {'destination': '北京', ...}).
            request_id: The ID for the JSON-RPC call. Defaults to "2" to match the curl example.
        """
        if self.log_enable:
            print(f"Calling tool: {tool_name} on server: {server_name} with arguments: {arguments}")
        response_json = {}
        try:
            params = {
                "name": tool_name,
                "arguments": arguments
            }
            # The server code looks for a "params" key containing the tool details
            result = self._make_request(
                method="tools/call",
                server_name=server_name,
                params=params,
                request_id=self._get_next_id()
            )
            status = result.get("status", False)
            if status:
                if self.log_enable:
                    print(f"tools_call: {tool_name} on server: {server_name} with arguments: {arguments}")
                response = result.get("response", None)
                if response is not None:
                    response_json = response.json()
                return response_json
            else:
                return response_json
        except Exception as e:
            logging.error(f"Server {server_name} Failed to get tool call result: {e}")
            return {}

