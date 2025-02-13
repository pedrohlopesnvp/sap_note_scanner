# 🔵🌟 SAP Note Scanner  

[🇺🇸 Read in English](#-sap-note-scanner) | [🇧🇷 Leia em Português](#-scanner-de-notas-sap)  

---  

## 🇺🇸 SAP Note Scanner  

If you work with SAP—whether ABAP, Fiori UI5, CAP, or any other ERP module—you’ve certainly encountered **SAP Notes**.  

SAP Notes are essential for updates and information, but they can become a nightmare when filled with **prerequisites** that are hard to track.  

### 🎯 Purpose  

This application was developed to **simplify** the work of developers and Basis teams by cataloging all prerequisites of an SAP Note.  

### 🛠️ How It Works  

- The program is built in **Python** and uses **Selenium Web Scraping** to fetch SAP Notes from the **SAP for Me** blog.  
- To execute, simply run the following command in the terminal:  

  ```sh
  py sap_note_scanner.py
  ```  

- Ensure there is a folder named **"scanner"** in the same directory.  
- The application requires **SAP credentials** and a list of notes to be analyzed.  
- At the end of execution, a **TXT file** will be generated inside the **"scanner"** folder with all the prerequisites that would take you a long time to find.

### 📌 Installation  

No manual installation is needed! The program automatically installs the required **WebDriver**. However, if needed, you can install it manually with:  

```sh
pip install --upgrade webdriver_manager
```  

### 🤝 Contribute  

Thank you for reading! I hope you **test and collaborate** with this project. 🚀  

---

## 🇧🇷 Scanner de Notas SAP  

Se você trabalha com SAP—seja ABAP, Fiori UI5, CAP ou qualquer outro módulo ERP—com certeza já se deparou com as **Notas SAP**.  

As **Notas SAP** são essenciais para atualizações e informações, mas podem ser um **pesadelo** quando vêm recheadas de **pré-requisitos** difíceis de rastrear.  

### 🎯 Objetivo  

Este aplicativo foi desenvolvido para **facilitar** o trabalho de desenvolvedores e equipes de Basis, catalogando todos os **pré-requisitos** de uma Nota SAP.  

### 🛠️ Como Funciona  

- O programa foi feito em **Python** e usa **Web Scraping com Selenium** para buscar Notas SAP no blog **SAP for Me**.  
- Para executar, basta rodar o seguinte comando no terminal:  

  ```sh
  py sap_note_scanner.py
  ```  

- Certifique-se de que há uma pasta chamada **"scanner"** no mesmo diretório.  
- O aplicativo exige **credenciais SAP** e uma lista de notas a serem analisadas.  
- Ao final da execução, um **arquivo TXT** será gerado na pasta **"scanner"** com todos os pre=requisitos que você levaria muito tempo para achar.

### 📌 Instalação  

Nenhuma instalação manual é necessária! O programa instala automaticamente o **WebDriver**. Porém, se precisar instalar manualmente, utilize:  

```sh
pip install --upgrade webdriver_manager
```  

### 🤝 Contribua  

Obrigado por ler! Espero que **teste e colabore** com este projeto. 🚀  

---
