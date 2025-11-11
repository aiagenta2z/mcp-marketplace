import click
import sys
import os

from mcp_marketplace.app.mcp_tool_use.src.constants import LOG_ENABLE

## Add cli.py 3rd parent folder to sys path, such as /bin folder
# cli.py: /project_root/mcp_marketplace/app/mcp_tool_use/src/cli.py
# ./project_root/
current_script_path = os.path.abspath(__file__)
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_script_path)))
package_src_root = os.path.dirname(os.path.dirname(current_script_path))
package_app_parent = os.path.dirname(current_script_path)
## subfolder, fit "/web/static" path
package_app_mcp_tool_use =os.path.join(package_app_parent, "app/mcp_tool_use")
if project_root not in sys.path:
    sys.path.insert(0, project_root)
if package_src_root not in sys.path:
    sys.path.insert(0, package_src_root)
if package_app_parent not in sys.path:
    sys.path.insert(0, package_app_parent)
if package_app_mcp_tool_use not in sys.path:
    sys.path.insert(0, package_app_mcp_tool_use)

if LOG_ENABLE:
    print (f"project_root {project_root}")
    print (f"package_root {package_src_root}")
    print (f"package_app_root {package_app_parent}")
    print (f"package_app_mcp_tool_use {package_app_mcp_tool_use}")
    print (f"Staring Sys Path in cli.py: {sys.path}")

from .constants import *

# --- CLI Setup ---
@click.group()
def cli():
    """MCP Marketplace Command Line Tool."""
    pass

def validate_app_path(app_path):
    """"""
    import importlib
    try:
        module_path, app_name = app_path.split(':', 1)
        click.echo(f"验证模块路径: {module_path}")
        click.echo(f"验证应用名称: {app_name}")

        # 尝试导入模块
        module_folder = module_path.split('.')
        print (f"DEBUG: {module_folder}")

        import sys
        print(f"Starting App.py using sys.path: {sys.path}")

        cur_module_path = ""
        for i, sub_module in enumerate(module_folder):
            if i == 0:
                cur_module_path += f"{sub_module}"
            else:
                cur_module_path += f".{sub_module}"
            click.echo(f"Loading Module {cur_module_path}")
            importlib.import_module(cur_module_path)
            click.echo(f"✅ 模块导入成功 {cur_module_path}")

        module = importlib.import_module(module_path)
        click.echo("✅ 模块导入成功")

        # 检查app对象
        if hasattr(module, app_name):
            click.echo(f"✅ 找到应用对象: {app_name}")
            return True
        else:
            click.echo(f"❌ 未找到应用对象: {app_name}")
            return False

    except ImportError as e:
        click.echo(f"❌ 模块导入失败: {e}")
        return False
    except ValueError:
        click.echo(f"❌ 应用路径格式错误: {app_path}")
        return False

@cli.command()
@click.option('--port', default=5000, type=int, help='The port to run the server on.')
@click.option('--host', default='0.0.0.0', type=str, help='The host address to bind the server to.')
@click.option('--config', default='', type=str, help='The path to the mcp_config.json file that the mcp marketplace client uses when starts...')
def run(port: int, host: str, config: str):
    """
    Starts the OneKey MCP Router server (mcp_tool_use app).

    NOTE: Requires mcp-marketplace[mcp_tool_use] to be installed.
    """
    # Check if uvicorn is available (it's installed with the 'mcp_tool_use' extra)
    ## Monitor Config Dir  ./ .json file change
    local_config_dir = os.path.join(package_app_mcp_tool_use, "data/mcp/config")
    user_input_config_dir = ""
    try:
        import uvicorn
        if config and config != "":
            absolute_config_path = ""
            if os.path.isabs(config):
                absolute_config_path = config
                print(f"mcpm CLI --config using absolute path: {absolute_config_path}")
            else:
                cli_cwd = os.getcwd()
                if cli_cwd.endswith('/'):
                    cli_cwd = cli_cwd[:-1]
                absolute_config_path = os.path.abspath(os.path.join(cli_cwd, config))
                print(f"mcpm CLI  --config using absolute path: {absolute_config_path}")
            os.environ[KEY_ENV_MCP_CONFIG_PATH] = absolute_config_path
            user_input_config_dir = os.path.dirname(absolute_config_path)
        # if empty don't set environments variables
    except ImportError:
        click.echo(
                click.style("Error: The 'mcp_tool_use' server requires 'uvicorn' and 'fastapi'.\n", fg='red') +
                "Please install with: " + click.style("pip install mcp-marketplace[mcp_tool_use]", fg='green'),
                err=True
        )
        sys.exit(1)

    try:
        # The import path must reflect the new structure:
        # mcp_marketplace package -> mcp_tool_use module -> app.py file -> app object
        # app_path = "mcp_marketplace.app.mcp_tool_use.src.app:app"
        app_path = "mcp_marketplace.app.mcp_tool_use.src.app:app"
        click.echo(f"WORKING DIR: {os.getcwd()}")
        # validate_app_path(app_path)

        click.echo(f"Starting MCP Router Server (Uvicorn) at http://{host}:{port}")
        click.echo(f"Starting MCP Router Server MCP Config Admin Console at http://{host}:{port}/mcp")
        click.echo(f"Application path: {app_path}")

        # Use uvicorn.run to start the server
        uvicorn.run(app_path,
                    host=host,
                    port=port,
                    log_level="info",
                    reload=True,
                    reload_dirs=[local_config_dir, user_input_config_dir],
                    reload_includes=["*.json"]
                    )
        click.echo(f"Application Start Successfully!")

    except Exception as e:
        click.echo(click.style(f"An error occurred while starting the server: {e}", fg='red'), err=True)
        sys.exit(1)

if __name__ == '__main__':
    cli()
