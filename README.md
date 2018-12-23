# Krita Python Reference Plugin

A Krita plugin that displays a searchable overview of the Python API.

The reference is built at run time via Python's introspection abilities and hence always matching your Krita version. Since the API doesn't expose any doc strings or method signatures, this plugin can only list method names.

<img src="images/screenshot_full.png" alt="Screenshot" width="300"/> <img src="images/screenshot_search.png" alt="Screenshot" width="300"/>


## Installation

1. [Download the sourca as zip](https://github.com/rbreu/krita-plugin-python-reference/archive/master.zip)
2. Unzip the file
3. Go to your Krita resource folder and create the directories _actions_ and _pykrita_
4. Copy the directory plugin/python_reference into the pykrita folder
5. Copy the file plugin/python_reference.desktop into the pykrita folder
6. Copy the file plugin/python_reference.action into the action folder
7. Restart Krita
8. Go to _Settings -> Configure Krita -> Python Plugin Manager_ and enable the Python Reference Plugin.

You should then be able to access the plugin via _Tools -> Scripts -> Python Reference_.