#Guia de Instalação e Execução do Programa de Atualização Diária de Arquivo#
Este guia irá ajudá-lo a instalar todos os componentes necessários e configurar o programa para atualizar diariamente o arquivo "Expurgos 2024.xlsx" em sua máquina, garantindo que o processo ocorra mesmo que um usuário específico não esteja online.

Sumário
Requisitos do Sistema
Instalação do Python
Configuração do Ambiente
Instalação das Bibliotecas Necessárias
Download do Script
Configuração do Script
Execução Inicial do Script
Agendamento da Execução Diária Automática
Verificação e Solução de Problemas
Contato para Suporte
Requisitos do Sistema
Sistema Operacional: Windows 10 ou superior
Conexão à internet (para downloads e atualizações)
Acesso às pastas de origem e destino especificadas
Permissão para instalar programas e agendar tarefas no computador
Instalação do Python
O Python é a linguagem de programação necessária para executar o script. Siga os passos abaixo para instalá-lo:

Download do Python:

Acesse o site oficial: https://www.python.org/downloads/windows/
Clique em "Download Python 3.xx.x", onde "3.xx.x" é a versão mais recente do Python 3.
Instalação:

Execute o instalador baixado.
Importante: Na primeira tela, marque a opção "Add Python 3.xx to PATH" (Adicionar Python ao PATH).
Clique em "Customize installation" (Instalação personalizada).
Mantenha as opções padrão e clique em "Next".
Na próxima tela, marque a opção "Install for all users".
Clique em "Install" e aguarde a conclusão da instalação.
Verificação da Instalação:

Abra o Prompt de Comando:
Pressione Win + R, digite cmd e pressione Enter.
Digite python --version e pressione Enter.
Deverá aparecer a versão do Python instalada, confirmando a instalação bem-sucedida.
Configuração do Ambiente
Para facilitar a execução do script, iremos configurar uma pasta dedicada.

Criar Pasta do Projeto:

Crie uma pasta em seu computador, por exemplo: C:\FileSync.
Acessar a Pasta via Prompt de Comando:

No Prompt de Comando, digite cd C:\FileSync e pressione Enter.
Instalação das Bibliotecas Necessárias
O script utiliza algumas bibliotecas adicionais. Instale-as seguindo os passos:

Atualizar o Pip (gerenciador de pacotes do Python):

No Prompt de Comando, digite: python -m pip install --upgrade pip e pressione Enter.
Instalar Bibliotecas:

Para enviar notificações:
Digite: pip install pywin32 e pressione Enter.
Outras bibliotecas utilizadas já fazem parte da instalação padrão do Python.
Download do Script
Obter o Código do Script:

Você recebeu um arquivo de texto ou um e-mail com o código do script.
Copie todo o conteúdo do código.
Criar o Arquivo do Script:

Abra o Bloco de Notas ou outro editor de texto simples.
Cole o código copiado.
Clique em "Arquivo" > "Salvar como...".
Na janela de salvamento:
Selecione a pasta do projeto (C:\FileSync).
No campo "Nome do arquivo", digite FileSync.py.
No campo "Tipo", selecione "Todos os arquivos (*.*)".
Clique em "Salvar".
Configuração do Script
Antes de executar o script, verifique se os caminhos dos arquivos estão corretos.

Abrir o Script para Edição:

Clique com o botão direito no arquivo FileSync.py e selecione "Editar com o Bloco de Notas".
Verificar e Atualizar os Caminhos:

Arquivo de origem (self.source_file):
Certifique-se de que o caminho corresponde ao local onde o arquivo "Expurgos 2024.xlsx" está localizado em seu OneDrive.
Pasta de destino (self.destination_folder):
Verifique se o caminho corresponde ao local de destino na rede: Z:\OPER-ESO\4- Índices Limites e Batentes de Variação.
Salvar as alterações após confirmar os caminhos.
Execução Inicial do Script
A primeira execução do script irá agendar as execuções diárias automáticas.

Executar o Script Manualmente:

No Prompt de Comando, certifique-se de que está na pasta do projeto (C:\FileSync).
Digite: python FileSync.py e pressione Enter.
Resultado Esperado:

O script deverá iniciar o processo de sincronização.
Se tudo estiver correto, você receberá uma notificação informando que o arquivo foi atualizado com sucesso.
O script também irá agendar a execução diária automática no horário atual.
Agendamento da Execução Diária Automática
O script utiliza o Agendador de Tarefas do Windows para executar automaticamente todos os dias.

Verificar a Tarefa Agendada:

Abra o Agendador de Tarefas:
Pressione Win + R, digite taskschd.msc e pressione Enter.
Navegue até Biblioteca do Agendador de Tarefas.
Procure pela tarefa chamada "FileSyncDailyTask".
Verifique se a tarefa está programada para executar diariamente no horário desejado.
Alterar o Horário da Tarefa (Opcional):

Se desejar alterar o horário de execução:
Clique com o botão direito na tarefa "FileSyncDailyTask" e selecione "Propriedades".
Na aba "Disparadores", edite o horário conforme necessário.
Verificação e Solução de Problemas
Caso encontre problemas, siga os passos abaixo:

Erros de Permissão:

Certifique-se de que tem permissão para acessar as pastas de origem e destino.
Execute o Prompt de Comando como administrador:
Clique com o botão direito em cmd e selecione "Executar como administrador".
Problemas com o Mapeamento de Unidade de Rede:

Se a unidade Z: não estiver acessível:
Abra o Explorador de Arquivos e verifique se a unidade de rede está conectada.
Se necessário, remapeie a unidade:
Clique com o botão direito em "Este Computador" e selecione "Conectar unidade de rede".
Siga as instruções para mapear Z: ao caminho de rede correto.
Dependências Não Instaladas:

Se ocorrer um erro relacionado a bibliotecas não encontradas, reinstale as bibliotecas necessárias:
No Prompt de Comando, execute: pip install pywin32.
Verificar os Logs:

Os logs de execução estão localizados em: C:\Users\SeuUsuario\Documents\FileSync\FileSync.log.
Abra este arquivo para detalhes sobre erros ou mensagens do script.
Contato para Suporte
Se após seguir este guia você ainda tiver problemas, entre em contato com o suporte:

Equipe de TI Interna
E-mail: suporte@empresa.com.br
Telefone: (XX) XXXX-XXXX
Responsável pelo Script
Nome: [Nome do Responsável]
E-mail: responsavel@empresa.com.br
Observações Finais:

Este guia foi elaborado para usuários sem conhecimento prévio em programação ou uso do Python.
Siga os passos com atenção e não hesite em solicitar ajuda se necessário.
Garantir a atualização diária do arquivo "Expurgos 2024.xlsx" é essencial para o bom funcionamento dos processos internos.
