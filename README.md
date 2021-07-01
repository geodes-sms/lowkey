<img src="https://github.com/david-istvan/lowkey/blob/main/assets/lowkey-logo.png" width="200">

A low-level and transparent framework for collaborative modeling.

[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Build Status](https://travis-ci.com/david-istvan/lowkey.svg?branch=main)](https://travis-ci.com/david-istvan/lowkey)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=david-istvan_lowkey&metric=alert_status)](https://sonarcloud.io/dashboard?id=david-istvan_lowkey)

# Repository structure

- [/lowkey](https://github.com/david-istvan/lowkey/tree/main/lowkey) - Main project.
  -  [/collabtypes](https://github.com/david-istvan/lowkey/tree/main/lowkey/collabtypes) - Type system for collaborative modeling.
  -  [/lww](https://github.com/david-istvan/lowkey/tree/main/lowkey/lww) - Low-level CRDT system.
  -  [/network](https://github.com/david-istvan/lowkey/tree/main/lowkey/network) - ZeroMQ-based distributed infrastructure.
- [/lowkey-examples](https://github.com/david-istvan/lowkey/tree/main/lowkey-examples) - Examples.

# References

## Metamodeling

<img src="https://raw.githubusercontent.com/david-istvan/collabserver-modeling/main/docs/modelverse.PNG?raw=true"/>

Source: [Van Mierlo, Barroca, Vangheluwe, Syriani, Kühne. Multi-Level Modelling in the Modelverse. Proceedings of MULTI 2014.](http://miso.es/multi/2014/proceedings_MULTI.pdf#page=89)


## CRDT specifications

[Shapiro M, Preguiça N, Baquero C, Zawirski M. A comprehensive study of convergent and commutative replicated data types (Doctoral dissertation, Inria–Centre Paris-Rocquencourt; INRIA)](https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf)

## Network

### Command language

- ```CREATE [type] [name]``` - Creates an instance with name ```[name]``` of the domain-specific type ```[type]```.
- ```CREATE association [type] [sourceName] [targetName]``` - Creates an instance of the association type ```[type]``` between the correspondingly typed objects named ```[sourceName]``` and ```[targetName]```, respectively.
  - Note, that both ```CREATE``` commands conform to the same abstract signtaure ```CREATE [logicalType] [domaintype] [namedReference..]```, where ```[domainType]``` is the reference to the domain-specific type, and ```[logicalType]``` is the reference to the logical level type (present at the API), with the added syntactic sugar of ```Entity``` being the default ```[logicalType]```. For details on domain-specific vs logical types, see [this overview](https://raw.githubusercontent.com/david-istvan/collabserver-example-mindmap/main/model/mapping.png).
- ```READ``` - Returns the mindmap model in a readable form.
- ```UPDATE [name] [property] [value]``` - Updates property ```[property]``` in object ```[name]``` to value ```[value]```.
- ```DELETE [name]``` - Deletes object ```[name]```.

### Architecture and patterns

<img src="https://raw.githubusercontent.com/david-istvan/collabserver-modeling/main/docs/zmq_pattern.PNG?raw=true"/>

Source: [ZMQ: Reliable Pub-Sub with Update republishing](https://zguide.zeromq.org/docs/chapter5/#Republishing-Updates-from-Clients)

Further pointers:
* [Ephemeral values](https://zguide.zeromq.org/docs/chapter5/#Ephemeral-Values)
* [Reactor](https://zguide.zeromq.org/docs/chapter5/#Using-a-Reactor)

## Running the components

```
python Server.py -log debug
python Editor.py -log debug
python Editor.py -log debug
```
