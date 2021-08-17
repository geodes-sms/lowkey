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
- ```OBJECTS``` - Lists every object in the local session.
- ```CREATE [type] [name]``` - Creates an instance with name ```[name]``` of the domain-specific type ```[type]```.
- ```LINK [source].[port] TO [target]``` - Links object ```[target]``` to object ```[source]``` via port ```[port]```.
- ```UPDATE [name] [attribute] [newValue]``` - Updates attribute ```[attribute]``` in object with ```[name]``` to value ```[newValue]```.
- ```DELETE [name]``` - Deletes object ```[name]```
