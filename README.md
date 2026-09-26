# 📡 Encaminhador MQTT-SN (Bluetooth RFCOMM para IP / UDP)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Android](https://img.shields.io/badge/Android-Termux-green.svg)
![Protocol](https://img.shields.io/badge/Protocol-MQTT--SN%20%2F%20UDP-orange.svg)

Este repositório contém a documentação, código-fonte e validação prática de um **Encaminhador (Forwarder) MQTT-SN** transparente. O projeto estabelece uma ponte de comunicação entre um dispositivo cliente sem suporte nativo a redes IP (comunicação via Bluetooth RFCOMM) e um Gateway MQTT-SN operando sobre a pilha IP (UDP) numa rede Wi-Fi local, integrando o fluxo final num Broker MQTT (Mosquitto).

---

## 📋 Sumário
- [1. Introdução e Objetivos](#-1-introdução-e-objetivos)
- [2. Arquitetura do Sistema](#-2-arquitetura-do-sistema)
- [3. Dispositivos e Tecnologias](#-3-dispositivos-e-tecnologias)
- [4. Código-Fonte (`forwarder.py`)](#-4-código-fonte-forwarderpy)
- [5. Como Executar o Projeto](#-5-como-executar-o-projeto)
- [6. Evidências de Validação](#-6-evidências-de-validação)
- [7. Conclusão](#-7-conclusão)

---

## 🎯 1. Introdução e Objetivos

O objetivo deste projeto é implementar e validar a transmissão de dados no protocolo **MQTT-SN** através de um cenário de rede heterogênea:
- **Origem:** Dispositivo móvel cliente enviando mensagens MQTT-SN via Bluetooth.
- **Intermediário:** Dispositivo móvel atuando como Encaminhador (Forwarder) de camada de aplicação/transporte.
- **Destino:** Computador executando o Gateway MQTT-SN e um Broker MQTT Mosquitto sobre rede local IP (UDP/TCP).

---

## 🏗️ 2. Arquitetura do Sistema

### Diagrama de Fluxo de Dados

```mermaid
graph TD
    A[Dispositivo 1: Cliente Bluetooth] -->|Bluetooth RFCOMM| B[Dispositivo 2: App BT/TCP Bridge]
    B -->|Socket Loopback TCP:9000| C[Dispositivo 2: forwarder.py em Termux]
    C -->|Rede Wi-Fi UDP:1884| D[PC Windows: gateway.py]
    D -->|MQTT TCP:1883| E[PC Windows: Broker Mosquitto]


