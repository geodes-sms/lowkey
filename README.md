<img src="https://github.com/david-istvan/lowkey/blob/main/assets/lowkey-logo.png" width="200">

A low-level and transparent framework for collaborative modeling.

[![License](https://img.shields.io/badge/license-GPL--3.0-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Unit tests](https://github.com/geodes-sms/lowkey/actions/workflows/ci.yml/badge.svg)](https://github.com/geodes-sms/lowkey/actions/workflows/ci.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=david-istvan_lowkey&metric=alert_status)](https://sonarcloud.io/dashboard?id=david-istvan_lowkey)

# Repository structure

- [/lowkey](https://github.com/david-istvan/lowkey/tree/main/lowkey) - Main project.
  -  [/collabtypes](https://github.com/david-istvan/lowkey/tree/main/lowkey/collabtypes) - Type system for [collaborative modeling](#Metamodeling).
  -  [/lww](https://github.com/david-istvan/lowkey/tree/main/lowkey/lww) - Low-level [CRDT system](#CRDT-specifications).
  -  [/network](https://github.com/david-istvan/lowkey/tree/main/lowkey/network) - ZeroMQ-based distributed [network infrastructure](#Architecture-and-patterns).
- [/lowkey-examples](https://github.com/david-istvan/lowkey/tree/main/lowkey-examples) - Examples.

# Setup guide
- Clone this repository.
- Install requirements via ```pip install -r requirements.txt```.
- Install the framework as an editable local package via ```pip install -e [path_to_the_project]```. (Use ```pip uninstall lowkey``` if not needed anymore.)

# References

## Metamodeling

<img src="https://raw.githubusercontent.com/david-istvan/collabserver-modeling/main/docs/modelverse.PNG?raw=true"/>

Source: [Van Mierlo, Barroca, Vangheluwe, Syriani, Kühne. Multi-Level Modelling in the Modelverse. Proceedings of MULTI 2014.](http://miso.es/multi/2014/proceedings_MULTI.pdf#page=89)


## CRDT specifications

[Shapiro M, Preguiça N, Baquero C, Zawirski M. A comprehensive study of convergent and commutative replicated data types (Doctoral dissertation, Inria–Centre Paris-Rocquencourt; INRIA)](https://hal.inria.fr/file/index/docid/555588/filename/techreport.pdf)

## Network architecture and patterns

<img src="https://raw.githubusercontent.com/david-istvan/collabserver-modeling/main/docs/zmq_pattern.PNG?raw=true"/>

Source: [ZMQ: Reliable Pub-Sub with Update republishing](https://zguide.zeromq.org/docs/chapter5/#Republishing-Updates-from-Clients)

Further pointers:
* [Ephemeral values](https://zguide.zeromq.org/docs/chapter5/#Ephemeral-Values)
* [Reactor](https://zguide.zeromq.org/docs/chapter5/#Using-a-Reactor)

## Command language
* ```CREATE -name {name} -typedBy {type} [-attributeName {value}]*```
* ```LINK -from {fromClabject}.{associationName} -to {toClabject} [-attributeName {value}]*```
* ```UPDATE (-name {name} | -id {id}) [-attributeName {newValue}]*```
* ```DELETE (-name {name} | -id {id})```
