import os
import shutil
import datetime
import logging
import sys
from pathlib import Path
import ctypes  # Para enviar notificações

class FileSync:
    def __init__(self):
        # Configurações de caminhos
        self.source_file = r"C:\Users\zdvn\OneDrive - VIBRA\NCMV - Indicador\_DataLake\3- Dados consolidados e revisados (CURATED)\AIVI Expurgos Portal ESO\Expurgos 2024.xlsx"
        self.destination_folder = r"Z:\OPER-ESO\4- Índices Limites e Batentes de Variação"
        self.destination_file = os.path.join(self.destination_folder, "Expurgos 2024.xlsx")

        # Configuração de logs
        self.user_home = str(Path.home())
        self.log_folder = os.path.join(self.user_home, "Documents", "FileSync")
        self.log_file = os.path.join(self.log_folder, "FileSync.log")
        self.last_run_file = os.path.join(self.log_folder, "last_run_time.txt")

        # Criar pasta de logs se não existir
        os.makedirs(self.log_folder, exist_ok=True)

        # Configurar logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(message)s',
            handlers=[
                logging.FileHandler(self.log_file),
                logging.StreamHandler(sys.stdout)
            ]
        )
        self.logger = logging.getLogger(__name__)

    def send_notification(self, title, message):
        """Envia uma notificação ao usuário"""
        try:
            ctypes.windll.user32.MessageBoxW(0, message, title, 0x1000)
        except Exception as e:
            self.logger.error(f"Erro ao enviar notificação: {e}")

    def get_last_run_time(self):
        """Obtém a data/hora da última execução"""
        try:
            if os.path.exists(self.last_run_file):
                with open(self.last_run_file, 'r') as f:
                    return datetime.datetime.fromisoformat(f.read().strip())
            return None
        except Exception as e:
            self.logger.error(f"Erro ao ler última execução: {e}")
            return None

    def update_last_run_time(self):
        """Atualiza a data/hora da última execução"""
        try:
            with open(self.last_run_file, 'w') as f:
                f.write(datetime.datetime.now().isoformat())
        except Exception as e:
            self.logger.error(f"Erro ao atualizar última execução: {e}")

    def copy_file(self):
        """Copia o arquivo se necessário"""
        try:
            # Verifica se o arquivo de origem existe
            if not os.path.exists(self.source_file):
                self.logger.error(f"Arquivo de origem não encontrado: {self.source_file}")
                self.send_notification("Erro", f"Arquivo de origem não encontrado: {self.source_file}")
                return False

            # Verifica se a pasta de destino existe
            if not os.path.exists(self.destination_folder):
                self.logger.error(f"Pasta de destino não encontrada: {self.destination_folder}")
                self.send_notification("Erro", f"Pasta de destino não encontrada: {self.destination_folder}")
                return False

            # Verifica a data de modificação do arquivo de destino
            if os.path.exists(self.destination_file):
                dest_mod_time = datetime.datetime.fromtimestamp(os.path.getmtime(self.destination_file))
                today = datetime.datetime.now().date()
                if dest_mod_time.date() >= today:
                    self.logger.info("O arquivo de destino já está atualizado.")
                    self.send_notification("Informação", "O arquivo já foi atualizado hoje.")
                    return True

            # Copia o arquivo
            shutil.copy2(self.source_file, self.destination_file)
            self.logger.info(f"Arquivo copiado com sucesso: {self.source_file}")
            self.send_notification("Sucesso", "O arquivo foi atualizado com sucesso.")
            return True

        except Exception as e:
            self.logger.error(f"Erro durante a cópia do arquivo: {e}")
            self.send_notification("Erro", f"Erro ao copiar o arquivo: {e}")
            return False

    def check_missed_run(self):
        """Verifica se a execução diária foi perdida e executa se necessário"""
        last_run = self.get_last_run_time()
        today = datetime.datetime.now().date()
        if last_run is None or last_run.date() < today:
            self.logger.info("Execução diária perdida ou ainda não realizada. Executando agora.")
            self.copy_file()
            self.update_last_run_time()
        else:
            self.logger.info("Execução diária já realizada.")

    def run(self):
        """Executa o processo completo"""
        self.logger.info("Iniciando processo de sincronização...")
        self.check_missed_run()

if __name__ == "__main__":
    sync = FileSync()
    sync.run()
