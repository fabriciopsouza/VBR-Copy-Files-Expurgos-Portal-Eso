# 🔄 Script de Sincronização Diária de Arquivo

## Visão Geral
Este script automatiza a sincronização diária do arquivo "Expurgos 2024.xlsx", garantindo atualizações mesmo quando usuários específicos não estão online.

## 🖥️ Requisitos do Sistema
- **Sistema Operacional**: Windows 10 ou superior
- **Conexão com Internet**: Necessária para downloads e atualizações
- **Acesso**: Permissões para pastas de origem e destino
- **Direitos**: Capacidade de instalar programas e agendar tarefas

## 🐍 Instalação do Python

### Download do Python
1. Visite o site oficial do Python: [Downloads Python](https://www.python.org/downloads/windows/)
2. Baixe a versão mais recente do Python 3.x

### Etapas de Instalação
- Execute o instalador
- **Importante**: Marque "Adicionar Python 3.x ao PATH"
- Escolha "Instalação personalizada"
- Selecione "Instalar para todos os usuários"

### Verificar Instalação
```bash
python --version
```

## 📦 Configuração do Ambiente

### Criar Pasta do Projeto
```bash
mkdir C:\FileSync
cd C:\FileSync
```

## 🛠️ Instalação das Bibliotecas

### Atualizar Pip
```bash
python -m pip install --upgrade pip
```

### Instalar Bibliotecas Necessárias
```bash
pip install pywin32
```

## 📂 Preparação do Script

### Download e Configuração
1. Copie o código do script fornecido
2. Salve como `FileSync.py` em `C:\FileSync`
3. Edite os caminhos no script:
   - Verifique o caminho do arquivo de origem no OneDrive
   - Confirme o caminho da pasta de destino na rede

## 🚀 Execução Inicial

### Executar Manualmente
```bash
cd C:\FileSync
python FileSync.py
```

## ⏰ Agendamento Automático
- O script usa o Agendador de Tarefas do Windows
- Tarefa programada: `FileSyncDailyTask`
- Execução diária no horário configurado

## 🛠️ Solução de Problemas

### Verificação de Logs
- Logs de execução: `C:\Users\SeuUsuario\Documents\FileSync\FileSync.log`

## 📞 Suporte

### Equipe de TI
- **E-mail**: suporte@empresa.com.br
- **Telefone**: (XX) XXXX-XXXX

### Responsável pelo Script
- **Nome**: [Nome do Responsável]
- **E-mail**: responsavel@empresa.com.br

## ℹ️ Observações
- Guia desenvolvido para usuários sem conhecimento prévio em programação
- Siga os passos cuidadosamente
- Em caso de dúvidas, solicite suporte

**Objetivo**: Garantir a atualização diária do arquivo "Expurgos 2024.xlsx" para o bom funcionamento dos processos internos.
