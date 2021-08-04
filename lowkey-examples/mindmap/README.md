# Mindmap example

## Structure

- [/metamodel](https://github.com/david-istvan/lowkey-examples/mindmap/metamodel) - Metamodel.
- [/editor](https://github.com/david-istvan/lowkey-examples/mindmap/editor) - Simple command-line editor.

## Metamodel

<img src="https://github.com/david-istvan/lowkey/blob/main/lowkey-examples/mindmap/docs/mindmapMM.png"/>

## Running the example

- Open a terminal and start the server in [/lowkey/network](https://github.com/david-istvan/lowkey/tree/main/lowkey/network): ```python Server.py -log debug```.
- Open a number of editor clients in [/editor](https://github.com/david-istvan/lowkey-examples/mindmap/editor) in separate terminals: ```python Editor.py -log debug```.
- Refer to the command language below to start modeling.

### Command language

- ```READ``` - Returns the mindmap model in a readable form.
- ```CREATE [type] [name]``` - Creates an instance with name ```[name]``` of the domain-specific type ```[type]```.
- ```CREATE RELATIONSHIP [name] [sourceName] [targetName]``` - Creates a relationship with name ```[name]``` between the objects named ```[sourceName]``` and ```[targetName]```, respectively.
- ```UPDATE [name] [property] [value]``` - Updates property ```[property]``` in object ```[name]``` to value ```[value]```.
- ```DELETE [name]``` - Deletes object ```[name]```.

### Command language v2
- ```READ``` - Returns the mindmap model in a readable form.
- ```CREATE [type] [name]``` - Creates an instance with name ```[name]``` of the domain-specific type ```[type]```.
- ```LINK [name1] TO [name2].[link]``` - Links object ```[name1]``` under object ```[name1]``` via link ```[link]```.
