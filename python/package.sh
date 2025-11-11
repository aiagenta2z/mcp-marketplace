### Test Command CLI
cd ./python
pip install -e .
pip install mcp-marketplace[mcp_tool_use] -e .


### Package


rm -r dist
python -m build

## 测试环境

## Test
twine upload --repository testpypi dist/* --verbose

## Official
twine upload --repository pypi dist/* --verbose


### Search

pip install setuptools wheel twine

python setup.py sdist bdist_wheel

twine upload dist/*
